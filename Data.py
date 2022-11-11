from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
**❄️ مـرحـبـاً بـك عـزيـزي ** {},

⌯ ¦ في بــوت استـخـراج جلـسـة

⌯ ¦ استـخـراج تيرمـكـس تليثون

⌯ ¦ وبــايــروجـرام للـمـيــوزك🎧

⌯ ¦ يعمـل هـذا البـوت لمساعدتـك بطريقـة سهلـه

⌯ ¦ للحصـول على كـود تيرمكـس لتشغيل تلـيثون

⌯ ¦ والبايروجرام لتشغيل سـورس اغــاني تم انشـاء

⌯ ¦ هـذا البـوت بواسطـة : [ 𝗧𝗘𝗥𝗘𝗫 』 ](https://t.me/JJPJB)
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton("بـدء انشـاء جلسـة البـوت", callback_data="generate")],
        [InlineKeyboardButton(text=" رجــوع ", callback_data="home")]
    ]

    generate_button = [
        [InlineKeyboardButton("بـدء انشـاء جلسـة البـوت", callback_data="generate")]
    ]

    # Rest Buttons
    buttons = [
        [InlineKeyboardButton("بـدء انشـاء جلسـة البـوت", callback_data="generate")],
        
        [
            InlineKeyboardButton("مسـاعدة", callback_data="help"),
            InlineKeyboardButton("حول البوت", callback_data="about")
        ],
        
    ]

    # Help Message
    HELP = """
**- اوامـر البـوت الاخـرى ⌨:**

/about - حـول البـوت
/help - اوامـر المسـاعده
/start - بـدء تشغيـل البـوت
/generate - بـدء انشـاء جلسـه
/cancel - الغـاء
/restart - اعـادة تشغيـل
"""

    # About Message
    ABOUT = """
**- حــول البـــوت :**

**» بـوت انشـاء جلسـة البـوت واستخـراج كـود تيرمكـس التابـع لســورس تـيـركـس .. مبني ع آخـر اصـدار لـ لغـة بايثـون 3.9.7** 🌐🦾
    
**» لغة البوت 🅿️:** [Python³](https://www.python.org/)

**» مطور البـوت 🧑🏻‍💻:** [  𝗧𝗘𝗥𝗘𝗫 ](https://t.me/JJPJB)

**» قناة السورس 🌐:** [𝗦𝗢𝗨𝗥𝗖𝗘 𝗧𝗘𝗥𝗘𝗫](https://t.me/BNBRB)

**» الشـروحـات 🛂:** 
- [بـوت لـتنصيب ](https://t.me/JJPJB)
- [شروحات تنصيب](https://t.me/BNBRB)

    """
