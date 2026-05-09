import logging
import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
import anthropic

TELEGRAM_TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"
ANTHROPIC_API_KEY = "YOUR_ANTHROPIC_API_KEY"

SYSTEM_PROMPT = "Sen foydali yordamchisan. O'zbek tilida javob ber."

logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)
client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)
history = {}

async def start(update, context):
    history[update.effective_user.id] = []
    await update.message.reply_text("Salom! Men AI yordamchiman. Savolingizni yozing!")

async def clear(update, context):
    history[update.effective_user.id] = []
    await update.message.reply_text("Tarix tozalandi!")

async def handle(update, context):
    uid = upd
        r = client.messages.create(model="claude-opus-4-5", max_tokens=1024, system=SYSTEM_PROMPT, messages=history[uid])
        reply = r.content[0].text
        history[uid].append({"role": "assistant", "content": reply})
        await update.message.reply_text(reply)
    except Exception as e:
        await update.message.reply_text("Xatolik yuz berdi. /start bilan qayta boshlang.")

app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("clear", clear))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle))
app.run_polling
