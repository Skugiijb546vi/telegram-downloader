import os
import sys
import asyncio
from pyrogram import Client

async def main():
    api_id = os.environ.get("API_ID")
    api_hash = os.environ.get("API_HASH")
    bot_token = os.environ.get("BOT_TOKEN")
    chat_id = os.environ.get("CHAT_ID")
    video_path = sys.argv[1]

    if not all([api_id, api_hash, bot_token, chat_id, video_path]):
        print("Missing required environment variables or file path.")
        sys.exit(1)

    print(f"Starting Pyrogram client to upload: {video_path}")
    
    app = Client(
        "my_bot",
        api_id=int(api_id),
        api_hash=api_hash,
        bot_token=bot_token
    )

    async with app:
        print("Uploading to Telegram...")
        await app.send_video(
            chat_id=chat_id,
            video=video_path,
            caption="🎥 **فیلمەکەت ئامادەیە!**\n\nئەپلۆد کرا لە ڕێگەی گیتھەب ئەکشنزەوە.",
            supports_streaming=True
        )
        print("Upload completed successfully!")

if __name__ == "__main__":
    asyncio.run(main())
