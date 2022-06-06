#    This file is part of the CompressorBot distribution.
#    Copyright (c) Binary Tech
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, version 3.
#
#    This program is distributed in the hope that it will be useful, but
#    WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
#    General Public License for more details.



from .worker import *


async def up(event):
    if not event.is_private:
        return
    stt = dt.now()
    ed = dt.now()
    v = ts(int((ed - uptime).seconds) * 1000)
    ms = (ed - stt).microseconds / 1000
    p = f"🌋Pɪɴɢ = {ms}ms"
    await event.reply(v + "\n" + p)


async def start(event):
    ok = await event.client(GetFullUserRequest(event.sender_id))
    await event.reply(
       Fayl "<string>", 18-qator
    f"Assalomu alaykum! ☘️ `{ok.user.first_name}`\n\nBu Video CompressorBot.🎯\nMen ham namunalar/skrinshotlar yaratishim mumkin.\n\nTanlovlarni olish uchun shunchaki videoni yoʻnaltiring\nPowered by @gucci_obbo",
        buttons=[
            [Button.inline("𝐇𝐄𝐋𝐏", data="ihelp")],
            [
                Button.url("𝐒𝐎𝐔𝐑𝐂𝐄 𝐂𝐎𝐃𝐄", url="t.mr/gucci_obbo"),
                Button.url("𝐒𝐔𝐏𝐏𝐎𝐑𝐓 𝐆𝐑𝐎𝐔𝐏", url="t.me/Uzbekchaa_Anime"),
            ],
        ],
    )


async def help(event):
    await event.reply(
         "**☘️ Video CompressorBot**\n\n+Ushbu bot arzimagan sifatdagi videolarni siqib chiqaradi.\n+Namunali siqilgan video va skrinshotlar yarating\n-Sifat sozlamalari tufayli bot siqish uchun vaqt oladi.\nVideolarni birma-bir yuboring. Tugallagandan keyin bittasi.\n\nVideoni tanlash uchun faqat yoʻnaltiring”,
    )


async def ihelp(event):
    await event.edit(
        "**☘️ Video CompressorBot**\n\n+Ushbu bot arzimagan sifatdagi videolarni siqib chiqaradi.\n+Namunali siqilgan video va skrinshotlar yarating\n-Sifat sozlamalari tufayli bot siqish uchun vaqt oladi.\nVideolarni birma-bir yuboring. Tugallagandan keyin bittasi.\n\nVideoni tanlash uchun faqat yoʻnaltiring”,
        buttons=[Button.inline("BACK", data="beck")],
    )


async def beck(event):
    ok = await event.client(GetFullUserRequest(event.sender_id))
    await event.edit(
        Fayl "<string>", 18-qator
    Fayl "<string>", 18-qator
    f"Assalomu alaykum! ☘️ `{ok.user.first_name}`\n\nBu Video CompressorBot.🎯\nMen ham namunalar/skrinshotlar yaratishim mumkin.\n\nTanlovlarni olish uchun shunchaki videoni yoʻnaltiring\nPowered by @gucci_obbo",
        buttons=[
            [Button.inline("𝐇𝐄𝐋𝐏", data="ihelp")],
            [
                Button.url("𝐒𝐎𝐔𝐑𝐂𝐄 𝐂𝐎𝐃𝐄", url="t.me/gucci_obbo"),
                Button.url("𝐒𝐔𝐏𝐏𝐎𝐑𝐓 𝐆𝐑𝐎𝐔𝐏", url="t.me/Uzbekchaa_Anime"),
            ],
        ],
    )


async def sencc(e):
    key = e.pattern_match.group(1).decode("UTF-8")
    await e.edit(
        "Choose Mode",
        buttons=[
            [
                Button.inline("Default Compress", data=f"encc{key}"),
                Button.inline("Custom Compress", data=f"ccom{key}"),
            ],
            [Button.inline("Back", data=f"back{key}")],
        ],
    )


async def back(e):
    key = e.pattern_match.group(1).decode("UTF-8")
    await e.edit(
        "☘️  **Nima qilish kerak** ☘️",
        buttons=[
            [
                Button.inline("GENERATE SAMPLE", data=f"gsmpl{key}"),
                Button.inline("SCREENSHOTS", data=f"sshot{key}"),
            ],
            [Button.inline("COMPRESS", data=f"sencc{key}")],
        ],
    )


async def ccom(e):
    await e.edit("Send Ur Custom Name For That File🙂")
    wah = e.pattern_match.group(1).decode("UTF-8")
    wh = decode(wah)
    out, dl, thum, dtime = wh.split(";")
    chat = e.sender_id
    async with e.client.conversation(chat) as cv:
        reply = cv.wait_event(events.NewMessage(from_users=chat))
        repl = await reply
        if "." in repl.text:
            q = repl.text.split(".")[-1]
            g = repl.text.replace(q, "mkv")
        else:
            g = repl.text + ".mkv"
        outt = f"encode/{chat}/{g}"
        x = await repl.reply(
            f"Custom File Name : {g}\n\nSend Thumbnail Picture For it.🙂"
        )
        replyy = cv.wait_event(events.NewMessage(from_users=chat))
        rep = await replyy
        if rep.media:
            tb = await e.client.download_media(rep.media, f"thumb/{chat}.jpg")
        elif rep.text and not (rep.text).startswith("/"):
            url = rep.text
            os.system(f"wget {url}")
            tb = url.replace("https://telegra.ph/file/", "")
        else:
            tb = thum
        omk = await rep.reply(f"Thumbnail {tb} Setted Successfully🙂")
        hehe = f"{outt};{dl};{tb};{dtime}"
        key = code(hehe)
        await customenc(omk, key)
