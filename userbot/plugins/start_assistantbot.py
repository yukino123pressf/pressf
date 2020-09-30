# Copyright (C) Midhun KM 
# 
# Please Don't Kang Without Credits
# A Plugin For Assistant Bot 


from telethon import events, custom, Button
from telethon.tl.types import (
    Channel,
    Chat,
    User
)
from telethon.utils import get_display_name
from userbot.utils import admin_cmd, sudo_cmd
from userbot.uniborgConfig import Config
from telethon import events
from datetime import datetime
from userbot.utils import admin_cmd, edit_or_reply, sudo_cmd
import time
from userbot import Lastupdate

@tgbot.on(events.NewMessage(pattern="^/start"))
async def start(event):
    vent = event.chat_id
    starttext = ("Hi! This Bot is Part of @FridayOT \nThis Bot is Used For "
                 "Some Features That Can Be Used Via Bot. \nIf you want your"
                 "Own Assistant Bot Then Deploy From Button Bellow")
    if event.from_id == bot.uid:
        await tgbot.send_message(
           vent,
           message="Hi Master, It's Me Your Assistant.",
           buttons = [
           [Button.url("Repo 🛡️", "https://github.com/StarkGang/FridayUserbot")],
           [Button.url("Join Channel 📃", "t.me/Fridayot")]
            ]
           )
    else:
        await tgbot.send_message(
           event.chat_id,
           message=starttext,
           link_preview=False,
           buttons = [
           [Button.url("Repo 🛡️", "https://github.com/StarkGang/FridayUserbot")],
           [Button.url("Join Channel 📃", "t.me/Fridayot")]
       ]
      )



def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "

    time_list.reverse()
    ping_time += ":".join(time_list)

    return ping_time

@tgbot.on(events.NewMessage(pattern="^/ping"))
async def _(event):
    start = datetime.now()
    vent = event.chat_id
    starttext = ("Hi! This Bot is Part of @FridayOT \nThis Bot is Used For "
                 "Some Features That Can Be Used Via Bot. \nIf you want your"
                 "Own Assistant Bot Then Deploy From Button Bellow")
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    uptime = get_readable_time((time.time() - Lastupdate))
    if event.from_id == bot.uid:
        await tgbot.send_message(event.chat_id, f"**█▀█ █▀█ █▄░█ █▀▀ █ \n█▀▀ █▄█ █░▀█ █▄█ ▄**\n ➲ `{ms}` \n ➲ `{uptime}`")
    else:
        await tgbot.send_message(
           event.chat_id,
           message=starttext,
           link_preview=False,
           buttons = [
           [Button.url("Repo 🛡️", "https://github.com/StarkGang/FridayUserbot")],
           [Button.url("Join Channel 📃", "t.me/Fridayot")]
      ]
     )



import emoji
from googletrans import Translator

from userbot.utils import admin_cmd, edit_or_reply, sudo_cmd


@tgbot.on(events.NewMessage(pattern="^/tr ?(.*)"))
async def _(event):
    if "trim" in event.raw_text:
        # https://t.me/c/1220993104/192075
        return
    input_str = event.pattern_match.group(1)
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        text = previous_message.message
        lan = input_str or "gu"
    elif "|" in input_str:
        lan, text = input_str.split("|")
    else:
        await tgbot.send_message(event.chat_id, "`.tr LanguageCode` as reply to a message")
        return
    text = emoji.demojize(text.strip())
    lan = lan.strip()
    translator = Translator()
    try:
        translated = translator.translate(text, dest=lan)
        after_tr_text = translated.text
        # TODO: emojify the :
        # either here, or before translation
        output_str = """**Translated By Friday Assistant Bot** 
         Source **( {} )**
         Translation **( {} )**
         {}""".format(
            translated.src, lan, after_tr_text
        )
    if event.from_id = bot.uid:
        await tgbot.send_message(event.chat_id, output_str)
    else:
        await tgbot.send_message(event.chat_id, "You Can't Access Me")
    except Exception as exc:
        await tgbot.send_message(event.chat_id, str(exc))
