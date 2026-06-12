import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from flask import Flask
from threading import Thread

# تشغيل سيرفر ويب وهمي لإبقاء المنصة مستيقظة 24 ساعة
app = Flask('')

@app.route('/')
def home():
    return "Bot is running 24/7!"

def run_web_server():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run_web_server)
    t.start()

TOKEN = "8211820774:AAFZ8iZ7QpHkzWv1Wo0y02AESw3kUzXhzTo"
SUPPORT_USER = "@soso100gam"

bot = telebot.TeleBot(TOKEN)
user_status = {}

def main_menu():
    markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    markup.add(KeyboardButton("📋 خيارات التسريب"))
    markup.add(KeyboardButton("📊 تنتيج"), KeyboardButton("🎓 بيع شهادات"))
    markup.add(KeyboardButton("📢 قناتنا"), KeyboardButton("🛠️ الدعم الفني"))
    return markup

def leak_menu():
    markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    markup.add(KeyboardButton("📝 تسريبات تاسع"))
    markup.add(KeyboardButton("🔬 تسريبات بكالوريا علمي"))
    markup.add(KeyboardButton("📚 تسريبات بكالوريا ادبي"))
    markup.add(KeyboardButton("🔙 العودة للقائمة الرئيسية"))
    return markup

def send_payment_msg(message, item_name, price):
    msg = f"🔴 طلبك: {item_name}\n"
    msg += f"💰 السعر: {price}\n\n"
    msg += f"📥 يرجى التواصل هنا لأخذ بيانات الإيداع: {SUPPORT_USER}"
    bot.send_message(message.chat.id, msg)

@bot.message_handler(func=lambda message: True)
def handle_messages(message):
    user_id = message.from_user.id
    text = message.text

    if text == "/start":
        user_status[user_id] = False
        markup = ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(KeyboardButton("🔄 تحقق من الاشتراك"))
        bot.send_message(user_id, f"⚠️ عذراً! يجب عليك الانضمام إلى مجموعتنا أولاً لاستخدام البوت:\nhttps://t.me", reply_markup=markup)
        return

    elif text == "🔄 تحقق من الاشتراك":
        user_status[user_id] = True
        bot.send_message(user_id, "✅ تم التحقق من الاشتراك بنجاح!")
        bot.send_message(user_id, "👋 أهلاً بك في البوت! اختر من القائمة أدناه:", reply_markup=main_menu())
        return

    if not user_status.get(user_id, False):
        markup = ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(KeyboardButton("🔄 تحقق من الاشتراك"))
        bot.send_message(user_id, f"⚠️ عذراً! يجب عليك الانضمام إلى مجموعتنا أولاً لاستخدام البوت:\nhttps://t.me", reply_markup=markup)
        return

    if text == "🔙 العودة للقائمة الرئيسية":
        bot.send_message(user_id, "👋 اختر من القائمة أدناه:", reply_markup=main_menu())
    elif text == "📢 قناتنا":
        bot.send_message(user_id, "📢 أهلاً وسهلاً في قناتنا:\nhttps://t.me")
    elif text == "🛠️ الدعم الفني":
        bot.send_message(user_id, f"🛠️ يرجى إرسال رسالة واحدة بالمطلوب للدعم الفني:\n{SUPPORT_USER}")
    elif text == "📋 خيارات التسريب":
        bot.send_message(user_id, "اختر القسم المطلوب:", reply_markup=leak_menu())

    # --- علمي ---
    elif text == "🔬 تسريبات بكالوريا علمي":
        markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        markup.add(KeyboardButton("📦 علمي: كامل المواد"), KeyboardButton("📐 علمي: رياضيات"))
        markup.add(KeyboardButton("🧬 علمي: علوم"), KeyboardButton("🧪 علمي: كيمياء"))
        markup.add(KeyboardButton("📝 علمي: عربي"), KeyboardButton("🌍 علمي: فرنسي"))
        markup.add(KeyboardButton("🇷🇺 علمي: روسي"), KeyboardButton("🕌 علمي: ديانة"))
        markup.add(KeyboardButton("📋 خيارات التسريب"))
        bot.send_message(user_id, "اختر المادة المطلوبة (فرع علمي):", reply_markup=markup)
    elif text == "📦 علمي: كامل المواد": send_payment_msg(message, text, "350$")
    elif text in ["📐 علمي: رياضيات", "🧬 علمي: علوم", "📝 علمي: عربي"]: send_payment_msg(message, text, "100$")
    elif text in ["🧪 علمي: كيمياء", "🌍 علمي: فرنسي", "🇷🇺 علمي: روسي", "🕌 علمي: ديانة"]: send_payment_msg(message, text, "75$")

    # --- ادبي ---
    elif text == "📚 تسريبات بكالوريا ادبي":
        markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        markup.add(KeyboardButton("📦 ادبي: كامل المواد"), KeyboardButton("📝 ادبي: عربي"))
        markup.add(KeyboardButton("🗺️ ادبي: جغرافيا"), KeyboardButton("⏳ ادبي: تاريخ"))
        markup.add(KeyboardButton("🕌 ادبي: ديانة"), KeyboardButton("🌍 ادبي: فرنسي"))
        markup.add(KeyboardButton("🇷🇺 ادبي: روسي"), KeyboardButton("📋 خيارات التسريب"))
        bot.send_message(user_id, "اختر المادة المطلوبة (فرع أدبي):", reply_markup=markup)
    elif text == "📦 ادبي: كامل المواد": send_payment_msg(message, text, "350$")
    elif text in ["📝 ادبي: عربي", "🗺️ ادبي: جغرافيا", "⏳ ادبي: تاريخ"]: send_payment_msg(message, text, "100$")
    elif text in ["🕌 ادبي: ديانة", "🌍 ادبي: فرنسي", "🇷🇺 ادبي: روسي"]: send_payment_msg(message, text, "75$")

    # --- تأسع ---
    elif text == "📝 تسريبات تاسع":
        markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        markup.add(KeyboardButton("📦 تاسع: كامل المواد"), KeyboardButton("📐 تاسع: رياضيات"))
        markup.add(KeyboardButton("📝 تاسع: عربي"), KeyboardButton("🕌 تاسع: ديانة"))
        markup.add(KeyboardButton("🌍 تاسع: فرنسي"), KeyboardButton("🇷🇺 تاسع: روسي"))
        markup.add(KeyboardButton("📋 خيارات التسريب"))
        bot.send_message(user_id, "اختر المادة المطلوبة (تاسع):", reply_markup=markup)
    elif text == "📦 تاسع: كامل المواد": send_payment_msg(message, text, "250$")
    elif text == "📐 تاسع: رياضيات": send_payment_msg(message, text, "100$")
    elif text in ["📝 تاسع: عربي", "🕌 تاسع: ديانة", "🌍 تاسع: فرنسي", "🇷🇺 تاسع: روسي"]: send_payment_msg(message, text, "75$")

    # --- تنتيج ---
    elif text == "📊 تنتيج":
        markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        markup.add(KeyboardButton("📊 تنتيج كل المواد"), KeyboardButton("📑 تنتيج مادة واحدة"))
        markup.add(KeyboardButton("🔙 العودة للقائمة الرئيسية"))
        bot.send_message(user_id, "اختر خيار التنتيج المتاح:", reply_markup=markup)
    elif text == "📊 تنتيج كل المواد": send_payment_msg(message, text, "1500$")
    elif text == "📑 تنتيج مادة واحدة": send_payment_msg(message, text, "300$")

    # --- شهادات ---
    elif text == "🎓 بيع شهادات":
        markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        markup.add(KeyboardButton("📜 شراء شهادة تاسع"), KeyboardButton("📜 شراء شهادة بكالوريا"))
        markup.add(KeyboardButton("🔙 العودة للقائمة الرئيسية"))
        bot.send_message(user_id, "اختر نوع الشهادة:", reply_markup=markup)
    elif text == "📜 شراء شهادة تاسع": send_payment_msg(message, text, "1800$")
    elif text == "📜 شراء شهادة بكالوريا": send_payment_msg(message, text, "2000$")

if __name__ == "__main__":
    keep_alive() # تشغيل السيرفر لحماية البوت من النوم
    bot.infinity_polling()
  
