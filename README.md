# SmartShopBot v2 - Refactored

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Docker](https://img.shields.io/badge/docker-enabled-brightgreen.svg)](https://www.docker.com/)

A completely refactored Telegram bot for intelligent shopping list management with receipt OCR processing, AI-powered suggestions, and price tracking. Built with **clean architecture**, **dependency injection**, and **production-ready** patterns.

## ✨ Features

### Core Functionality
- **Smart Shopping Lists**: Add, remove, and manage items with intelligent parsing
- **Receipt OCR Processing**: Upload receipt photos for automatic item extraction
- **AI Suggestions**: Get personalized product recommendations via OpenAI or Gemini
- **Price Tracking**: Historical price tracking and cost analysis
- **Multi-Language**: Full support for English and Portuguese (Brazilian)
- **User Analytics**: View spending statistics by category and time period
- **Favorites Management**: Save frequently used stores for quick access

### Technical Highlights
- **Clean Architecture**: Clearly separated layers (presentation, application, domain, infrastructure)
- **Dependency Injection**: Loose coupling for better testability and maintainability
- **Repository Pattern**: Abstract data access for flexible storage solutions
- **Service-Oriented**: Business logic isolated in reusable services
- **Full Type Hints**: Python 3.10+ with complete type safety
- **Error Handling**: Global middleware for consistent error management
- **Comprehensive Logging**: Structured logging throughout the application
- **Docker Ready**: Production-grade Docker setup with docker-compose
- **Testable**: Unit and integration tests with pytest fixtures

## 🏗️ Architecture

```
smart-shopping-bot/
├── src/
│   ├── bot/
│   │   ├── handlers/              # Telegram request handlers
│   │   ├── middleware/             # Auth, errors, logging
│   │   └── application.py
│   ├── domain/
│   │   ├── entities/              # Business objects
│   │   ├── enums/                 # Currency, Language, Status
│   │   └─┐ exceptions/            # Domain exceptions
│   ├── application/
│   │   ├── use_cases/             # Business logic (CRUD operations)
│   │   └── dto/                   # Data transfer objects
│   ├── infrastructure/
│   │   ├── database/              # SQLAlchemy models
│   │   ├── repositories/          # Data access layer
│   │   ├── services/              # External integrations
│   │   └── config/                # Settings & configuration
│   ├── presentation/
│   │   ├── formatters/            # Message formatting
│   │   └── keyboards/             # Telegram UI elements
│   └── main.py
├── tests/
│   ├── unit/                  # Unit tests
│   ├── integration/           # Integration tests
│   └── fixtures/              # Test fixtures
├── docker/
│   ├── Dockerfile
│   └── docker-compose.yml
├── .env.example
├── .gitignore
├── requirements.txt
├── README.md
├── ARCHITECTURE.md
├── CONTRIBUTING.md
└── LICENSE
```

## 🚀 Quick Start

### Prerequisites
- Python 3.10+
- PostgreSQL 12+
- Redis 6+
- Docker & Docker Compose (optional)

### Local Setup

1. **Clone and install**:
```bash
git clone https://github.com/yourusername/smart-shopping-bot.git
cd smart-shopping-bot
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

2. **Configure environment**:
```bash
cp .env.example .env
# Edit .env with your credentials
```

3. **Set up database**:
```bash
# PostgreSQL should be running
alembic upgrade head
```

4. **Run the bot**:
```bash
python src/main.py
```

### Docker Setup

```bash
cd docker
docker-compose up -d
```

This starts:
- PostgreSQL database
- Redis cache
- Bot application

## 📋 Configuration

Create `.env` file from `.env.example`:

```env
# Telegram
TELEGRAM_BOT_TOKEN=your_token_here

# Database
DATABASE_URL=postgresql://user:password@localhost/shopbot

# Redis
REDIS_URL=redis://localhost:6379

# AI Providers (choose one)
OPENAI_API_KEY=sk-...
GEMINI_API_KEY=...
AI_PROVIDER=openai  # or 'gemini'

# OCR
GOOGLE_VISION_API_KEY=...

# Features
ENABLE_AI_SUGGESTIONS=true
ENABLE_PRICE_TRACKING=true
ENABLE_NOTIFICATIONS=true
DEFAULT_LANGUAGE=en  # 'en' or 'pt_BR'
```

## 🔌 API / Bot Commands

```
/start - Initialize or view welcome message
/help - Show all available commands
/list - View current shopping list
/add <item> - Add item to list
/remove <item> - Remove item from list
/clear - Clear entire shopping list
/receipt - Process receipt image
/suggestions - Get AI-powered suggestions
/stats - View spending analytics
/settings - Configure preferences
/currency <CODE> - Set currency (USD, EUR, BRL)
/language <LANG> - Set language (en, pt_BR)
/stores - Manage favorite stores
```

## 🛠️ Development

### Project Structure Explanation

#### `src/bot/`
**Handlers**: Entry points for Telegram events
- `base_handler.py`: Abstract base with common functionality
- `command_handler.py`: /start, /help commands
- `shopping_handler.py`: List operations
- `receipt_handler.py`: Receipt processing
- `analytics_handler.py`: Statistics

**Middleware**: Cross-cutting concerns
- `auth_middleware.py`: User validation
- `error_middleware.py`: Global error handling
- `logging_middleware.py`: Request/response logging

#### `src/domain/`
**Entities**: Core business objects with zero external dependencies
- `User`, `ShoppingList`, `Product`, `Receipt`, `PriceHistory`

**Enums**: Type-safe constants
- `Currency`, `Language`, `ProcessingStatus`

#### `src/application/`
**Use Cases**: Application business rules
- `AddItemUseCase`: Add with validation
- `ProcessReceiptUseCase`: OCR + AI extraction
- `GetStatisticsUseCase`: Analytics aggregation

#### `src/infrastructure/`
**Database**: SQLAlchemy ORM models
**Repositories**: Data access abstraction
**Services**: External integrations
- `AIService`: OpenAI/Gemini provider
- `OCRService`: Image processing
- `CacheService`: Redis caching
- `TranslationService`: Multi-language

## 🧪 Testing

```bash
# Run all tests
pytest

# With coverage
pytest --cov=src

# Specific test file
pytest tests/unit/test_shopping_service.py

# Integration tests
pytest tests/integration/
```

## 📊 Database Schema

### Users Table
```sql
- id (PK)
- telegram_id (UK)
- username
- language (en, pt_BR)
- currency (USD, EUR, BRL, etc)
- dietary_preferences (JSON)
- favorite_stores (JSON array)
- created_at, updated_at
```

### Shopping Lists
```sql
- id (PK)
- user_id (FK)
- is_active (bool)
- created_at, updated_at
```

### Products
```sql
- id (PK)
- name (UK per user)
- category
- last_price
- created_at, updated_at
```

### Receipts
```sql
- id (PK)
- user_id (FK)
- store_name
- total_amount
- ocr_confidence
- processing_status (pending, completed, failed)
- purchased_date
- created_at
```

## 🔄 Design Patterns

1. **Repository Pattern**: Abstraction over data access
2. **Dependency Injection**: Loose coupling via constructor injection
3. **Service Layer**: Business logic separated from handlers
4. **DTO Pattern**: Type-safe data transfer between layers
5. **Factory Pattern**: Service creation and configuration
6. **Command Pattern**: Actions as encapsulated objects
7. **Middleware Pattern**: Cross-cutting concerns

## 📚 Key Improvements from Original

| Aspect | Original | Refactored |
|--------|----------|----------|
| Architecture | Mixed concerns | Clean layered |
| Type Safety | Minimal hints | Full type hints |
| Testing | Limited | Unit + Integration |
| Error Handling | Scattered | Centralized |
| Configuration | Hard-coded | Environment-based |
| Dependencies | Tightly coupled | Injected |
| Documentation | Minimal | Comprehensive |
| Docker | Basic | Production-ready |
| Logging | Basic | Structured |
| Scalability | Limited | High |

## 🐛 Troubleshooting

### Database Connection Failed
```bash
# Verify PostgreSQL is running
psql -U postgres

# Check DATABASE_URL in .env
```

### Redis Connection Issues
```bash
# Ensure Redis is running
redis-cli ping
# Should return: PONG
```

### Telegram API Timeout
- Verify `TELEGRAM_BOT_TOKEN` is correct
- Check internet connection
- Verify bot is not running elsewhere

## 📖 Documentation

- **[ARCHITECTURE.md](ARCHITECTURE.md)**: Detailed architecture decisions
- **[CONTRIBUTING.md](CONTRIBUTING.md)**: Development guidelines
- **API Docs**: Generated from type hints

## 🔐 Security Considerations

- Sensitive data never logged
- API keys from environment only
- SQL injection prevention via SQLAlchemy
- Input validation at all layers
- HTTPS for Telegram webhook (if used)

## 📄 License

MIT License - see [LICENSE](LICENSE) file

## 🙏 Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## 📞 Support

For issues and questions:
- GitHub Issues: [Open an issue](../../issues)
- Discussions: [Start a discussion](../../discussions)

---

**Built with ❤️ using Python, Clean Architecture, and best practices**
