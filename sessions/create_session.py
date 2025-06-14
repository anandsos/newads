from telethon.sync import TelegramClient

api_id = 21288986
api_hash = '5b6b0150ae015f05fb82b265ae2e04e5'

with TelegramClient('sessions/session1', api_id, api_hash) as client:
    print("✅ New session generated.")
