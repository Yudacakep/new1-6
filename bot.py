#(©)Codexbotz

from aiohttp import web
from plugins import web_server

import pyromod.listen
from pyrogram import Client
from pyrogram.enums import ParseMode
import sys
from datetime import datetime

from config import API_HASH, APP_ID, LOGGER, TG_BOT_TOKEN, TG_BOT_WORKERS, FORCE_SUB_CHANNEL, CHANNEL_ID, PORT, FORCE_SUB_1, FORCE_SUB_2, FORCE_SUB_3, FORCE_SUB_4, FORCE_SUB_5, FORCE_SUB_6, OWNER
)


class Bot(Client):
    def __init__(self):
        super().__init__(
            "Bot",
            api_hash=API_HASH,
            api_id=APP_ID,
            plugins={"root": "plugins"},
            workers=TG_BOT_WORKERS,
            bot_token=TG_BOT_TOKEN,
        )
        self.LOGGER = LOGGER

    async def start(self):
        try:
            await super().start()
            usr_bot_me = await self.get_me()
            self.username = usr_bot_me.username
            self.namebot = usr_bot_me.first_name
            self.LOGGER(__name__).info(
                f"TG_BOT_TOKEN detected!\n┌ First Name: {self.namebot}\n└ Username: @{self.username}\n——"
            )
        except Exception as a:
            self.LOGGER(__name__).warning(a)
            self.LOGGER(__name__).info(
                "Bot Berhenti. Gabung Group https://t.me/SharingUserbot untuk Bantuan"
            )
            sys.exit()

        if FORCE_SUB_1:
            try:
                var = "FORCE_SUB_1"
                info = await self.get_chat(FORCE_SUB_1)
                link = info.invite_link
                if not link:
                    await self.export_chat_invite_link(FORCE_SUB_1)
                    link = info.invite_link
                self.invitelink = link
                self.LOGGER(__name__).info(
                    f"{var} detected!\n┌ Title: {info.title}\n└ Chat ID: {info.id}\n——"
                )
            except Exception as a:
                self.LOGGER(__name__).warning(a)
                self.LOGGER(__name__).warning(
                    f"Bot tidak dapat Mengambil link invite dari {var}!"
                )
                self.LOGGER(__name__).info(
                    f"Pastikan @{self.username} adalah admin di Channel/Group Force Subs Tersebut, Chat ID Saat Ini: {FORCE_SUB_1}"
                )
                self.LOGGER(__name__).info(
                    "Bot Berhenti. Gabung Group https://t.me/SharingUserbot untuk Bantuan"
                )
                sys.exit()

        if FORCE_SUB_2:
            try:
                var = "FORCE_SUB_2"
                info = await self.get_chat(FORCE_SUB_2)
                link = info.invite_link
                if not link:
                    await self.export_chat_invite_link(FORCE_SUB_2)
                    link = info.invite_link
                self.invitelink2 = link
                self.LOGGER(__name__).info(
                    f"{var} detected!\n┌ Title: {info.title}\n└ Chat ID: {info.id}\n——"
                )
            except Exception as a:
                self.LOGGER(__name__).warning(a)
                self.LOGGER(__name__).warning(
                    f"Bot tidak dapat Mengambil link invite dari {var}!"
                )
                self.LOGGER(__name__).info(
                    f"Pastikan @{self.username} adalah admin di Channel/Group Force Subs Tersebut, Chat ID Saat Ini: {FORCE_SUB_2}"
                )
                self.LOGGER(__name__).info(
                    "Bot Berhenti. Gabung Group https://t.me/SharingUserbot untuk Bantuan"
                )
                sys.exit()

        if FORCE_SUB_3:
            try:
                var = "FORCE_SUB_3"
                info = await self.get_chat(FORCE_SUB_3)
                link = info.invite_link
                if not link:
                    await self.export_chat_invite_link(FORCE_SUB_3)
                    link = info.invite_link
                self.invitelink3 = link
                self.LOGGER(__name__).info(
                    f"{var} detected!\n┌ Title: {info.title}\n└ Chat ID: {info.id}\n——"
                )
            except Exception as a:
                self.LOGGER(__name__).warning(a)
                self.LOGGER(__name__).warning(
                    f"Bot tidak dapat Mengambil link invite dari {var}!"
                )
                self.LOGGER(__name__).info(
                    f"Pastikan @{self.username} adalah admin di Channel/Group Force Subs Tersebut, Chat ID Saat Ini: {FORCE_SUB_3}"
                )
                self.LOGGER(__name__).info(
                    "Bot Berhenti. Gabung Group https://t.me/SharingUserbot untuk Bantuan"
                )
                sys.exit()

        if FORCE_SUB_4:
            try:
                var = "FORCE_SUB_4"
                info = await self.get_chat(FORCE_SUB_4)
                link = info.invite_link
                if not link:
                    await self.export_chat_invite_link(FORCE_SUB_4)
                    link = info.invite_link
                self.invitelink4 = link
                self.LOGGER(__name__).info(
                    f"{var} detected!\n┌ Title: {info.title}\n└ Chat ID: {info.id}\n——"
                )
            except Exception as a:
                self.LOGGER(__name__).warning(a)
                self.LOGGER(__name__).warning(
                    f"Bot tidak dapat Mengambil link invite dari {var}!"
                )
                self.LOGGER(__name__).info(
                    f"Pastikan @{self.username} adalah admin di Channel/Group Force Subs Tersebut, Chat ID Saat Ini: {FORCE_SUB_4}"
                )
                self.LOGGER(__name__).info(
                    "Bot Berhenti. Gabung Group https://t.me/SharingUserbot untuk Bantuan"
                )
                sys.exit()

        if FORCE_SUB_5:
            try:
                var = "FORCE_SUB_5"
                info = await self.get_chat(FORCE_SUB_5)
                link = info.invite_link
                if not link:
                    await self.export_chat_invite_link(FORCE_SUB_5)
                    link = info.invite_link
                self.invitelink5 = link
                self.LOGGER(__name__).info(
                    f"{var} detected!\n┌ Title: {info.title}\n└ Chat ID: {info.id}\n——"
                )
            except Exception as a:
                self.LOGGER(__name__).warning(a)
                self.LOGGER(__name__).warning(
                    f"Bot tidak dapat Mengambil link invite dari {var}!"
                )
                self.LOGGER(__name__).info(
                    f"Pastikan @{self.username} adalah admin di Channel/Group Force Subs Tersebut, Chat ID Saat Ini: {FORCE_SUB_5}"
                )
                sys.exit()

        if FORCE_SUB_6:
            try:
                var = "FORCE_SUB_6"
                info = await self.get_chat(FORCE_SUB_6)
                link = info.invite_link
                if not link:
                    await self.export_chat_invite_link(FORCE_SUB_6)
                    link = info.invite_link
                self.invitelink6 = link
                self.LOGGER(__name__).info(
                    f"{var} detected!\n┌ Title: {info.title}\n└ Chat ID: {info.id}\n——"
                )
            except Exception as a:
                self.LOGGER(__name__).warning(a)
                self.LOGGER(__name__).warning(
                    f"Bot tidak dapat Mengambil link invite dari {var}!"
                )
                self.LOGGER(__name__).info(
                    f"Pastikan @{self.username} adalah admin di Channel/Group Force Subs Tersebut, Chat ID Saat Ini: {FORCE_SUB_6}"
                )
                self.LOGGER(__name__).info(
                    "Bot Berhenti. Gabung Group https://t.me/SharingUserbot untuk Bantuan"
                )
                sys.exit()

        try:
            db_channel = await self.get_chat(CHANNEL_ID)
            self.db_channel = db_channel
            test = await self.send_message(chat_id=db_channel.id, text="Test Message", disable_notification=True)
            await test.delete()
            self.LOGGER(__name__).info(
                f"CHANNEL_ID Database detected!\n┌ Title: {db_channel.title}\n└ Chat ID: {db_channel.id}\n——"
            )
        except Exception as e:
            self.LOGGER(__name__).warning(e)
            self.LOGGER(__name__).warning(
                f"Pastikan @{self.username} adalah admin di Channel DataBase anda, CHANNEL_ID Saat Ini: {CHANNEL_ID}"
            )
            self.LOGGER(__name__).info(
                "Bot Berhenti. Gabung Group https://t.me/SharingUserbot untuk Bantuan"
            )
            sys.exit()

        self.set_parse_mode("html")
        self.LOGGER(__name__).info(
            f"[🔥 BERHASIL DIAKTIFKAN! 🔥]"
        )
 
        self.username = usr_bot_me.username
        #web-response
        app = web.AppRunner(await web_server())
        await app.setup()
        bind_address = "0.0.0.0"
        await web.TCPSite(app, bind_address, PORT).start()
    

    async def stop(self, *args):
        await super().stop()
        self.LOGGER(__name__).info("Bot stopped.")
