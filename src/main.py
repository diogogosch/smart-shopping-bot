#!/usr/bin/env python3
"""Smart Shopping Bot - Main Application"""

import logging
import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, CallbackQueryHandler, filters, ContextTypes
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# In-memory storage (for testing)
user_lists = {}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Start command"""
    user_id = update.effective_user.id
    if user_id not in user_lists:
        user_lists[user_id] = []
    
    keyboard = [
        [InlineKeyboardButton("📝 My List", callback_data='view_list'), 
         InlineKeyboardButton("➕ Add Item", callback_data='add_item')],
        [InlineKeyboardButton("💡 Suggestions", callback_data='suggest'),
         InlineKeyboardButton("📈 Stats", callback_data='stats')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        '🤖 *SmartShoppingBot*\\n\\nManage your shopping list smartly!\\n\\nCommands:\\n/start - Start\\n/add <item> - Add item\\n/list - View list\\n/clear - Clear list',
        reply_markup=reply_markup,
        parse_mode='Markdown'
    )

async def add_item_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Add item via /add command"""
    user_id = update.effective_user.id
    if user_id not in user_lists:
        user_lists[user_id] = []
    
    if context.args:
        item = ' '.join(context.args)
        user_lists[user_id].append({"name": item, "bought": False})
        await update.message.reply_text(f"✅ Added: {item}")
    else:
        await update.message.reply_text("📢 Usage: /add <item_name>")

async def view_list_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """View shopping list"""
    user_id = update.effective_user.id
    if user_id not in user_lists or not user_lists[user_id]:
        await update.message.reply_text("🙄 Your list is empty!")
        return
    
    items_text = "🛒 *Your Shopping List*\\n\\n"
    for i, item in enumerate(user_lists[user_id], 1):
        status = "✅" if item["bought"] else "⬜"
        items_text += f"{status} {i}. {item['name']}\\n"
    
    await update.message.reply_text(items_text, parse_mode='Markdown')

async def clear_list_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Clear shopping list"""
    user_id = update.effective_user.id
    user_lists[user_id] = []
    await update.message.reply_text("🗑️ List cleared!")

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle button presses"""
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id
    
    if query.data == 'view_list':
        if user_id not in user_lists or not user_lists[user_id]:
            await query.edit_message_text(text="🙄 Your list is empty!")
            return
        
        items_text = "🛒 *Your Shopping List*\\n\\n"
        for i, item in enumerate(user_lists[user_id], 1):
            status = "✅" if item["bought"] else "⬜"
            items_text += f"{status} {i}. {item['name']}\\n"
        
        await query.edit_message_text(text=items_text, parse_mode='Markdown')
    
    elif query.data == 'add_item':
        await query.edit_message_text(text="🔍 Send me the item name to add.")
    
    elif query.data == 'suggest':
        suggestions = ["Milk", "Bread", "Eggs", "Cheese", "Vegetables"]
        text = "💡 *Suggested Items*\\n\\n" + "\\n".join(f"✓ {s}" for s in suggestions)
        await query.edit_message_text(text=text, parse_mode='Markdown')
    
    elif query.data == 'stats':
        if user_id in user_lists:
            total = len(user_lists[user_id])
            bought = sum(1 for item in user_lists[user_id] if item["bought"])
            text = f"📈 *Your Stats*\\n\\nTotal items: {total}\\nBought: {bought}\\nRemaining: {total - bought}"
        else:
            text = "📈 *Your Stats*\\n\\nTotal items: 0"
        await query.edit_message_text(text=text, parse_mode='Markdown')

async def handle_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle text messages"""
    user_id = update.effective_user.id
    if user_id not in user_lists:
        user_lists[user_id] = []
    
    text = update.message.text
    user_lists[user_id].append({"name": text, "bought": False})
    await update.message.reply_text(f"✅ Added: {text}")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Help command"""
    help_text = """*SmartShoppingBot Help*
    
*Commands:*
/start - Start the bot
/add <item> - Add item directly
/list - View your shopping list
/clear - Clear all items
/help - Show this help

*How to use:*
1. Click buttons or use commands
2. Send text to add items
3. Manage your shopping smartly!
    """
    await update.message.reply_text(help_text, parse_mode='Markdown')

def main():
    """Start the bot"""
    token = os.getenv('TELEGRAM_BOT_TOKEN')
    if not token:
        logger.error("TELEGRAM_BOT_TOKEN not set in environment")
        return
    
    app = Application.builder().token(token).build()
    
    # Command handlers
    app.add_handler(CommandHandler('start', start))
    app.add_handler(CommandHandler('add', add_item_command))
    app.add_handler(CommandHandler('list', view_list_command))
    app.add_handler(CommandHandler('clear', clear_list_command))
    app.add_handler(CommandHandler('help', help_command))
    
    # Callback handlers
    app.add_handler(CallbackQueryHandler(button))
    
    # Text message handler
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_text))
    
    logger.info("Starting bot...")
    app.run_polling()

if __name__ == '__main__':
    main()
