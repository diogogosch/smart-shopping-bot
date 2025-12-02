"""SmartShopBot - Main application entry point."""
import logging
import asyncio
from pathlib import Path

from telegram.ext import Application, CommandHandler, MessageHandler, filters

from src.infrastructure.config.settings import settings
from src.infrastructure.database.connection import init_db
from src.bot.handlers.command_handler import start_command, help_command
from src.bot.handlers.shopping_handler import add_item_handler, list_handler

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=getattr(logging, settings.LOG_LEVEL)
)
logger = logging.getLogger(__name__)


async def main() -> None:
    """Start the bot."""
    logger.info("Starting SmartShopBot v2...")
    
    # Initialize database
    await init_db()
    logger.info("Database initialized")
    
    # Create bot application
    application = Application.builder().token(settings.TELEGRAM_BOT_TOKEN).build()
    
    # Register command handlers
    application.add_handler(CommandHandler("start", start_command))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("list", list_handler))
    
    # Register message handlers
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, add_item_handler))
    
    logger.info("Bot handlers registered")
    
    # Start polling
    await application.run_polling()


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("Bot stopped by user")
    except Exception as e:
        logger.error(f"Fatal error: {e}", exc_info=True)
