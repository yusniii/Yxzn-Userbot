import asyncio
from telethon import TelegramClient
from telethon.sessions import StringSession

# Ganti dengan API_ID dan API_HASH baru dari my.telegram.org
API_ID = 16497647
API_HASH = 'd817e14e43847d27b724181fc7c3e2a1'

# Ganti dengan nomor Telegram-mu (atau bot token untuk bot)
PHONE = '+6283179639744'

async def main():
    print("Starting TelegramClient...")
    async with TelegramClient(StringSession(), API_ID, API_HASH) as client:
        # Jika belum login, minta kode
        if not await client.is_user_authorized():
            print(f"Sending code to {PHONE}...")
            await client.send_code_request(PHONE)
            code = input("Enter the code you received: ")
            try:
                await client.sign_in(PHONE, code)
            except Exception as e:
                # Jika Telegram minta password 2FA
                password = input("Two-step verification enabled. Enter your password: ")
                await client.sign_in(password=password)

        # Tampilkan STRING_SESSION
        print("\n✅ Your STRING_SESSION:\n")
        print(client.session.save())
        print("\nSave this string somewhere safe!")

if __name__ == "__main__":
    asyncio.run(main())
