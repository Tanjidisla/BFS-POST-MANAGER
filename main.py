from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    MessageHandler,
    ContextTypes,
    filters,
)
from dotenv import load_dotenv
import os
import asyncio
load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("📢 Publish Post", callback_data="publish")],
        [InlineKeyboardButton("📝 Templates", callback_data="templates")],
        [InlineKeyboardButton("🔘 Buttons", callback_data="buttons")],
        [InlineKeyboardButton("⚙️ Settings", callback_data="settings")]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "🤖 BFS POST MANAGER\n\nএকটি অপশন নির্বাচন করুন:",
        reply_markup=reply_markup
    )

async def button_click(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "publish":
        await query.message.reply_text("📝 আপনার পোস্ট লিখুন:")

    elif query.data == "templates":
        await query.edit_message_text("📝 Template Manager")

    elif query.data == "buttons":
        await query.edit_message_text("🔘 Button Manager")

    elif query.data == "settings":
        await query.edit_message_text("⚙️ Settings")
    elif query.data == "confirm_publish":
        await query.edit_message_text("✅ পোস্ট Publish করা হয়েছে!")
    elif query.data == "cancel_publish":
        await query.edit_message_text("❌ Publish বাতিল করা হয়েছে।")    
async def receive_post(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    await update.message.reply_text(
        f"📄 আপনার পোস্ট:\n\n{text}\n\n✅ Preview System শীঘ্রই যোগ করা হবে।"
    )
app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(button_click))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, receive_post))
if __name__ == "__main__":
    asyncio.set_event_loop(asyncio.new_event_loop())
    print("BFS POST MANAGER RUNNING...")
    app.run_polling()