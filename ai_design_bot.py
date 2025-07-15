
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "7952626376:AAHXYNRvQPo716K98zZuvwd89m393DvC2R4"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Привет! Я AI-дизайн-ассистент. Вот что я умею:\n"
        "/services — мои услуги\n"
        "/guide — бесплатный гайд\n"
        "/portfolio — посмотреть портфолио\n"
        "/order — оформить заказ"
    )

async def services(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🎨 Услуги AI-дизайна:\n"
        "• Баннер — 1500₽\n"
        "• Карусель — 2500₽\n"
        "• LoRA под ключ — от 3000₽"
    )

async def guide(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📘 Гайд: https://telegra.ph/aidesign-guide")

async def portfolio(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📂 Портфолио: https://behance.net/aisydesign")

async def order(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✏️ Чтобы оформить заказ, напиши сюда: @aisylu")

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("services", services))
app.add_handler(CommandHandler("guide", guide))
app.add_handler(CommandHandler("portfolio", portfolio))
app.add_handler(CommandHandler("order", order))

print("Бот запущен...")
app.run_polling()
