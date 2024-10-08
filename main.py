import os
import yt_dlp
import subprocess
from telegram import Update, ForceReply, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackContext, MessageHandler, filters
from flask import Flask, send_from_directory
from tqdm import tqdm
import uuid

# Flask app for hosting video temporarily
app = Flask(__name__)

# Your Telegram bot token from environment variables
BOT_TOKEN = os.getenv("BOT_TOKEN")
TEMP_DIR = "/tmp/videos/"
MAX_FILE_SIZE = 10 * 1024 * 1024 * 5  # 5 MB

# Create temporary directory if it doesn't exist
os.makedirs(TEMP_DIR, exist_ok=True)

# Flask route to serve the video file
@app.route('/download/<filename>', methods=['GET'])
def download_file(filename):
    return send_from_directory(TEMP_DIR, filename)

@app.route('/')
def index():
    return "Bot is running!"

# Function to track progress using tqdm
def progress_hook(d):
    if d['status'] == 'downloading':
        total_size = d.get('total_bytes', 1)
        downloaded_size = d.get('downloaded_bytes', 0)
        print(f"Downloaded {downloaded_size / total_size * 100:.2f}%")
    elif d['status'] == 'finished':
        print("Download completed!")

# Async function to start bot interaction
async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text('Welcome! Send a Moj app link to download the video.', reply_markup=ForceReply(selective=True))

# Async function to download and process video
async def download_video(update: Update, context: CallbackContext) -> None:
    url = update.message.text
    video_filename = f"{TEMP_DIR}{uuid.uuid4()}.%(ext)s"
    
    # yt-dlp download options
    ydl_opts = {
        'outtmpl': video_filename,
        'format': 'best',
        'progress_hooks': [progress_hook]
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            downloaded_filename = ydl.prepare_filename(info)
            
            # Process with FFmpeg for video correction
            corrected_filename = f"{downloaded_filename}_fixed.mp4"
            cmd = f"ffmpeg -i '{downloaded_filename}' -c:v copy -c:a copy '{corrected_filename}'"
            subprocess.run(cmd, shell=True)

            # Generate temporary hosted link
            hosted_url = f"https://{os.environ['RENDER_EXTERNAL_URL']}/download/{os.path.basename(corrected_filename)}"
            await update.message.reply_text(f"Your video is ready! Download it here: {hosted_url}")

    except Exception as e:
        await update.message.reply_text(f"Error occurred: {str(e)}")

# Function to create inline buttons for more options
async def options(update: Update, context: CallbackContext) -> None:
    keyboard = [
        [InlineKeyboardButton("Download Video", callback_data='download')],
        [InlineKeyboardButton("Help", callback_data='help')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text('Choose an option:', reply_markup=reply_markup)

# Function to handle callbacks from inline buttons
async def button_handler(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    await query.answer()
    if query.data == 'download':
        await query.edit_message_text(text="Send me a link to download the video.")
    elif query.data == 'help':
        await query.edit_message_text(text="This bot allows you to download videos from the Moj app. Just send the link!")

# Main function to initialize bot and start listening for updates
def main():
    # Create application instance with bot token
    application = ApplicationBuilder().token(BOT_TOKEN).build()

    # Add handlers for start command, options, and button callbacks
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, download_video))
    application.add_handler(MessageHandler(filters.COMMAND, options))
    application.add_handler(MessageHandler(filters.ALL, button_handler))

    # Start polling for updates
    application.run_polling()

if __name__ == '__main__':
    main()
    app.run(host='0.0.0.0', port=8080)
