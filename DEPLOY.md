# Smart Shopping Bot - Complete Deployment Guide

## Overview

A production-ready Telegram bot with AI-powered shopping list management, OCR receipt scanning, and price tracking. Built with Clean Architecture, async Python, and containerized deployment.

## Features

✅ **Telegram Integration**
- Full-featured bot with command handling
- Inline keyboard UI for seamless interaction
- Real-time message updates

✅ **Shopping List Management**
- Add/remove items with quantities
- Mark items as purchased
- Clear lists
- Persistent storage

✅ **AI Capabilities**
- Smart item suggestions based on shopping history
- Receipt text extraction via OCR
- Natural language processing
- Multi-provider AI (OpenAI, Google Gemini)

✅ **Receipt Processing**
- Photo upload and automatic OCR
- Intelligent item and price extraction
- Store name detection
- Purchase history tracking

✅ **Multi-Language Support**
- English (EN)
- Portuguese-Brazilian (PT-BR)
- Easy to extend

✅ **Production Architecture**
- Clean Architecture pattern
- Dependency injection
- Async/await throughout
- PostgreSQL persistence
- Redis caching (optional)
- Docker containerization
- Comprehensive error handling
- Logging and monitoring

## Quick Start (5 minutes)

### Prerequisites
- Python 3.10+
- PostgreSQL 12+
- Docker & Docker Compose (optional)
- Telegram Bot Token (from @BotFather)
- OpenAI or Google Gemini API key

### Installation

1. **Clone Repository**
```bash
git clone https://github.com/diogogosch/smart-shopping-bot.git
cd smart-shopping-bot
```

2. **Install Dependencies**
```bash
pip install -r requirements.txt
```

3. **Configure Environment**
```bash
cp .env.example .env
# Edit .env with your credentials:
# - TELEGRAM_BOT_TOKEN
# - DATABASE_URL (PostgreSQL connection)
# - OPENAI_API_KEY or GEMINI_API_KEY
# - GOOGLE_APPLICATION_CREDENTIALS (for OCR)
```

4. **Initialize Database**
```bash
python -m alembic upgrade head
```

5. **Run Bot**
```bash
python src/main.py
```

## Docker Deployment

### Using Docker Compose (Recommended)

```bash
# Start all services (bot, PostgreSQL, Redis)
docker-compose up -d

# View logs
docker-compose logs -f bot

# Stop services
docker-compose down
```

### Manual Docker Build

```bash
# Build image
docker build -t smart-shopping-bot .

# Run container
docker run -d \
  --name shopping-bot \
  --env-file .env \
  -v shopping-data:/data \
  smart-shopping-bot
```

## Configuration

### Environment Variables (.env)

```env
# Telegram
TELEGRAM_BOT_TOKEN=your_token_here

# Database
DATABASE_URL=postgresql://user:pass@localhost:5432/shopbot

# AI Provider (openai or gemini)
AI_PROVIDER=openai
OPENAI_API_KEY=sk-...
GEMINI_API_KEY=...

# OCR
GOOGLE_APPLICATION_CREDENTIALS=/path/to/credentials.json

# Caching
REDIS_URL=redis://localhost:6379/0

# Logging
LOG_LEVEL=INFO
```

### API Keys Setup

#### Telegram Bot Token
1. Message @BotFather on Telegram
2. Use `/newbot` command
3. Follow prompts and copy your token

#### OpenAI API Key
1. Visit https://platform.openai.com/api-keys
2. Create new secret key
3. Add to .env

#### Google Cloud Vision (for OCR)
1. Create Google Cloud project
2. Enable Vision API
3. Create service account
4. Download JSON credentials
5. Set `GOOGLE_APPLICATION_CREDENTIALS` path

## Project Structure

```
smart-shopping-bot/
├── src/
│   ├── domain/                 # Business logic
│   │   ├── entities.py         # Data models
│   │   ├── enums.py            # Enumerations
│   │   └── ports.py            # Interfaces
│   ├── infrastructure/          # External services
│   │   ├── config/
│   │   │   └── settings.py     # Configuration
│   │   ├── database/
│   │   │   ├── db.py           # Connection
│   │   │   └── models.py       # SQLAlchemy models
│   │   ├── repositories/       # Data access
│   │   │   ├── user_repository.py
│   │   │   └── shopping_repository.py
│   │   └── services/           # External APIs
│   │       ├── ai_service.py
│   │       └── ocr_service.py
│   ├── application/             # Use cases
│   │   └── use_cases/
│   │       └── manage_list.py
│   ├── presentation/            # UI components
│   │   └── keyboards.py        # Telegram keyboards
│   ├── bot/                     # Bot logic
│   │   ├── middleware/
│   │   │   └── auth.py
│   │   └── handlers/
│   │       ├── command_handler.py
│   │       ├── shopping_handler.py
│   │       └── receipt_handler.py
│   └── main.py                  # Entry point
├── requirements.txt             # Python dependencies
├── Dockerfile                   # Container image
├── docker-compose.yml           # Multi-container setup
└── README.md                    # Project documentation
```

## Bot Commands

### User Commands

| Command | Usage | Description |
|---------|-------|-------------|
| `/start` | `/start` | Initialize bot |
| `/list` | `/list` | View shopping list |
| `/add` | `/add 2 Milk` | Add item with quantity |
| `/suggestions` | `/suggestions` | Get AI recommendations |
| `/stats` | `/stats` | View shopping stats |
| `/clear` | `/clear` | Clear all items |

### Special Actions

- **Send Photo** → Bot extracts items using OCR
- **Click Items** → Toggle purchased/unpurchased
- **Inline Buttons** → Navigate and manage list

## Development

### Running Tests

```bash
# Install test dependencies
pip install pytest pytest-asyncio pytest-cov

# Run all tests
pytest

# Run with coverage
pytest --cov=src

# Run specific test file
pytest tests/test_shopping_handler.py
```

### Database Migrations

```bash
# Create migration
alembic revision --autogenerate -m "Add users table"

# Apply migrations
alembic upgrade head

# Rollback
alembic downgrade -1
```

### Code Quality

```bash
# Format code
black src/

# Lint
flake8 src/

# Type checking
mypy src/
```

## Deployment to Production

### Local Server Deployment

```bash
# Using systemd service
sudo cp smart-shopping-bot.service /etc/systemd/system/
sudo systemctl enable smart-shopping-bot
sudo systemctl start smart-shopping-bot

# View status
sudo systemctl status smart-shopping-bot
```

### Cloud Deployment (AWS EC2)

```bash
# SSH into instance
ssh -i key.pem ec2-user@instance-ip

# Install Docker
sudo yum install docker -y
sudo systemctl start docker

# Clone and run
git clone https://github.com/diogogosch/smart-shopping-bot.git
cd smart-shopping-bot
docker-compose up -d
```

### Portainer Deployment

1. Open Portainer UI
2. Go to **Stacks**
3. **Add Stack**
4. Paste docker-compose.yml content
5. Add environment variables
6. **Deploy**

## Troubleshooting

### Bot Not Responding

```bash
# Check logs
docker-compose logs -f bot

# Verify token
echo $TELEGRAM_BOT_TOKEN

# Test connection
curl -X GET "https://api.telegram.org/bot$TOKEN/getMe"
```

### Database Connection Error

```bash
# Check PostgreSQL is running
sudo systemctl status postgresql

# Test connection
psql $DATABASE_URL

# Reset database
psql -c "DROP DATABASE shopbot;"
psql -c "CREATE DATABASE shopbot;"
alembic upgrade head
```

### OCR Not Working

```bash
# Verify credentials
ls -la $GOOGLE_APPLICATION_CREDENTIALS

# Test Vision API
python -c "from google.cloud import vision; print('OK')"
```

## Performance Optimization

### Enable Redis Caching

```env
REDIS_URL=redis://localhost:6379/0
```

### Database Tuning

```sql
-- Create indexes
CREATE INDEX idx_user_telegram_id ON users(telegram_id);
CREATE INDEX idx_items_list_id ON shopping_items(list_id);
```

### Connection Pooling

Configured automatically in settings.py with SQLAlchemy pool size optimization.

## Security Best Practices

✅ Never commit .env files
✅ Rotate API keys regularly
✅ Use environment variables for secrets
✅ Enable HTTPS for production
✅ Keep dependencies updated
✅ Review logs regularly
✅ Implement rate limiting
✅ Validate user input

## Monitoring

### Logs

```bash
# Real-time logs
docker-compose logs -f

# Save logs
docker-compose logs > bot.log
```

### Metrics

- Active users
- Daily commands
- Receipt processing success rate
- AI API response times
- Database query performance

## Support & Contributing

For issues, feature requests, or contributions:
1. Open GitHub issue
2. Provide clear description
3. Include error logs
4. Submit pull request

## License

MIT License - See LICENSE file

## Author

Diogo Gosch - [@diogogosch](https://github.com/diogogosch)

---

**Ready to deploy?** Start with the Quick Start section above!
