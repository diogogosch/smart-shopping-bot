# 🚀 Smart Shopping Bot - Quick Start (5 Minutes)

## Get Started Immediately

This guide will have your bot running in 5 minutes!

### Step 1: Get Telegram Bot Token (2 minutes)

1. Open Telegram and message **@BotFather**
2. Send: `/newbot`
3. Choose a name: `SmartShoppingBot`
4. Choose a username: `smart_shopping_bot_YOURNAME`
5. Copy the token you receive

### Step 2: Clone Repository (1 minute)

```bash
git clone https://github.com/diogogosch/smart-shopping-bot.git
cd smart-shopping-bot
```

### Step 3: Setup Environment (1 minute)

```bash
cp .env.example .env
```

**Edit `.env` and add:**
```env
TELEGRAM_BOT_TOKEN=YOUR_TOKEN_HERE
DATABASE_URL=postgresql://user:pass@localhost:5432/shopbot
OPENAI_API_KEY=sk-...
```

### Step 4: Install & Run (1 minute)

```bash
pip install -r requirements.txt
python src/main.py
```

**That's it!** Your bot is running!

---

## Using Your Bot

### Commands
- `/start` - Initialize bot
- `/list` - View your shopping list
- `/add 2 Milk` - Add item with quantity
- `/suggestions` - Get AI recommendations
- **Send Photo** - Extract items using OCR

---

## Docker Setup (Alternative)

```bash
docker-compose up -d
```

---

## Need Help?

- **Full Setup Guide**: See `DEPLOY.md`
- **Architecture**: See `IMPLEMENTATION_GUIDE.md`
- **Issues**: Check GitHub Issues

---

**Next**: Read `DEPLOY.md` for production deployment!
