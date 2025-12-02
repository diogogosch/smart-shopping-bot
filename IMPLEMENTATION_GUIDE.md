# SmartShopBot v2 - Implementation Guide

## Project Status: Foundation Complete ✅

The core infrastructure and deployment configuration for SmartShopBot v2 is complete. This guide outlines the remaining implementation work to create a fully functional production-ready bot.

## Completed Components

### ✅ Foundation Layer
- `src/main.py` - Application entry point
- `src/infrastructure/config/settings.py` - Configuration management
- `Dockerfile` - Multi-stage production Docker build
- `docker-compose.yml` - Local development orchestration
- `portainer-stack.yml` - Production Portainer deployment
- `.env.example` - Configuration template
- `requirements.txt` - Python dependencies
- `README.md` - Project overview
- `PORTAINER_DEPLOYMENT.md` - Deployment guide
- `LICENSE` - MIT License
- `src/domain/exceptions/__init__.py` - Custom exceptions

### ✅ Portainer-Ready Deployment
- Full docker-compose support for Portainer stacks
- Environment variable injection
- Health checks for all services
- Volume persistence
- Network isolation
- Resource limit configuration

## Remaining Implementation Work

### Phase 1: Domain Layer (2-3 hours)

**Create Enums:**
```
src/domain/enums/
  __init__.py
  currency.py      # Enum for supported currencies
  language.py      # Enum for languages
  processing_status.py  # Enum for receipt statuses
```

**Create Entities:**
```
src/domain/entities/
  __init__.py
  user.py          # User domain object
  shopping_list.py # Shopping list domain object
  product.py       # Product domain object
  receipt.py       # Receipt domain object
  price_history.py # Price history domain object
```

Each entity should:
- Be a Pydantic BaseModel or dataclass
- Have full type hints
- Include validation logic
- Have descriptive docstrings

### Phase 2: Infrastructure Layer (3-4 hours)

**Database Models (SQLAlchemy):**
```
src/infrastructure/database/
  __init__.py
  connection.py    # Database connection setup
  session.py       # Session management
  models/
    __init__.py
    user_model.py
    shopping_list_model.py
    product_model.py
    receipt_model.py
    price_history_model.py
```

**Repositories:**
```
src/infrastructure/repositories/
  __init__.py
  base_repository.py    # Abstract base class
  user_repository.py
  product_repository.py
  shopping_list_repository.py
  receipt_repository.py
  price_history_repository.py
```

**Services:**
```
src/infrastructure/services/
  __init__.py
  cache_service.py       # Redis caching
  ocr_service.py        # Google Vision OCR
  ai_service.py         # OpenAI/Gemini integration
  translation_service.py # i18n support
  notification_service.py# Telegram notifications
  price_service.py      # Price tracking
```

### Phase 3: Application Layer (2-3 hours)

**Use Cases (Business Logic):**
```
src/application/use_cases/
  __init__.py
  shopping/
    __init__.py
    add_item.py
    remove_item.py
    list_items.py
    clear_list.py
  receipt/
    __init__.py
    process_receipt.py
  analytics/
    __init__.py
    get_statistics.py
  user/
    __init__.py
    update_preferences.py
```

**DTOs (Data Transfer Objects):**
```
src/application/dto/
  __init__.py
  shopping_dto.py
  receipt_dto.py
  stats_dto.py
  user_dto.py
```

### Phase 4: Bot Handler Layer (2-3 hours)

**Handlers:**
```
src/bot/handlers/
  __init__.py
  base_handler.py        # Abstract handler
  command_handler.py     # /start, /help, /settings
  shopping_handler.py    # /add, /list, /remove, /clear
  receipt_handler.py     # Receipt photo processing
  settings_handler.py    # User preferences
  analytics_handler.py   # /stats command
  suggestion_handler.py  # AI suggestions
```

**Middleware:**
```
src/bot/middleware/
  __init__.py
  auth_middleware.py     # User authentication
  error_middleware.py    # Global error handling
  logging_middleware.py  # Request/response logging
```

### Phase 5: Presentation Layer (1-2 hours)

**Formatters:**
```
src/presentation/formatters/
  __init__.py
  message_formatter.py   # Format bot messages
  list_formatter.py      # Format shopping lists
  stats_formatter.py     # Format statistics
```

**Keyboards:**
```
src/presentation/keyboards/
  __init__.py
  main_menu.py           # Main menu keyboard
  inline_buttons.py      # Inline buttons
```

### Phase 6: Tests (2-3 hours)

```
tests/
  __init__.py
  conftest.py            # Pytest fixtures
  unit/
    __init__.py
    test_shopping_service.py
    test_user_repository.py
    test_ai_service.py
  integration/
    __init__.py
    test_shopping_workflow.py
    test_receipt_processing.py
  fixtures/
    __init__.py
    factories.py         # Test data factories
    mocks.py             # Mock services
```

## Implementation Priority

### Must-Have (MVP)
1. ✅ Infrastructure layer (database, repositories)
2. ✅ User management
3. ✅ Shopping list CRUD operations
4. ✅ Receipt OCR processing
5. ✅ Basic handlers

### Should-Have
6. AI suggestions integration
7. Price tracking
8. User analytics
9. Multi-language support

### Nice-To-Have
10. Advanced analytics
11. Notification scheduling
12. Favorites management

## Development Workflow

### 1. Setup Development Environment
```bash
git clone https://github.com/diogogosch/smart-shopping-bot.git
cd smart-shopping-bot
python -m venv venv
source venv/bin/activate  # or: venv\Scripts\activate on Windows
pip install -r requirements.txt
```

### 2. Database Setup
```bash
# Start PostgreSQL and Redis
docker-compose up -d postgres redis

# Create database
alembic init alembic
# Create initial migration
alembic revision --autogenerate -m "Initial schema"
alembic upgrade head
```

### 3. Configure Environment
```bash
cp .env.example .env
# Edit .env with your values
export $(cat .env | xargs)
```

### 4. Implement Each Module
- Start with domain layer (entities)
- Move to infrastructure (database, repositories)
- Then application (use cases)
- Then bot handlers
- Finally presentation layer

### 5. Test Each Component
```bash
# Run tests
pytest

# With coverage
pytest --cov=src

# Watch mode
pytest-watch
```

### 6. Local Testing
```bash
# Run the bot locally
python src/main.py

# In another terminal, test with Telegram
# Send commands to your bot
```

## Deployment Steps

### Local Docker Compose
```bash
docker-compose up -d
```

### Portainer Stack Deployment
1. Access Portainer at `http://your-ip:9000`
2. Go to Stacks → Add Stack
3. Copy `portainer-stack.yml` content
4. Set environment variables
5. Deploy

See `PORTAINER_DEPLOYMENT.md` for detailed instructions.

## Code Quality Standards

### Type Hints
- All functions must have type hints
- Use `from __future__ import annotations` for forward references
- Use `Optional[T]` for nullable types

### Documentation
- Module docstrings explaining purpose
- Function docstrings with Args, Returns, Raises
- Complex logic should have inline comments

### Error Handling
- Use custom exceptions from `src/domain/exceptions`
- Handle errors at appropriate layers
- Log errors with context

### Testing
- Unit tests for business logic
- Integration tests for workflows
- Minimum 80% code coverage

## File Structure Checklist

Use this to track implementation:

- [ ] Domain Layer Complete
  - [ ] Entities created
  - [ ] Enums defined
  - [ ] Exceptions implemented
- [ ] Infrastructure Layer Complete
  - [ ] Database models created
  - [ ] Repositories implemented
  - [ ] Services implemented
- [ ] Application Layer Complete
  - [ ] Use cases implemented
  - [ ] DTOs created
- [ ] Bot Layer Complete
  - [ ] Handlers implemented
  - [ ] Middleware implemented
- [ ] Presentation Layer Complete
  - [ ] Formatters created
  - [ ] Keyboards designed
- [ ] Tests Complete
  - [ ] Unit tests written
  - [ ] Integration tests written
  - [ ] Coverage >80%
- [ ] Documentation Complete
  - [ ] Code documented
  - [ ] ARCHITECTURE.md written
  - [ ] CONTRIBUTING.md created

## Troubleshooting

### Import Errors
- Ensure all `__init__.py` files exist
- Check Python path includes `src/`
- Verify relative imports are correct

### Database Errors
- Verify PostgreSQL is running
- Check DATABASE_URL in .env
- Run migrations: `alembic upgrade head`

### Telegram Bot Not Responding
- Verify TELEGRAM_BOT_TOKEN is correct
- Check bot is not running elsewhere
- Review logs for errors

## Resources

- [python-telegram-bot docs](https://docs.python-telegram-bot.org/)
- [SQLAlchemy ORM](https://docs.sqlalchemy.org/)
- [Pydantic](https://docs.pydantic.dev/)
- [Docker Compose](https://docs.docker.com/compose/)
- [Portainer Docs](https://docs.portainer.io/)

## Next Steps

1. **Implement Domain Layer** - Create all entity and enum files
2. **Setup Database** - Create SQLAlchemy models and migrations
3. **Implement Repositories** - CRUD operations for all models
4. **Create Services** - External integrations (AI, OCR, cache)
5. **Build Handlers** - Telegram command handlers
6. **Add Tests** - Unit and integration tests
7. **Deploy** - Test in Portainer

---

**Estimated Total Time**: 15-20 hours of development
**Difficulty**: Intermediate to Advanced
**Key Skills Needed**: Python, async/await, SQL, Docker, Telegram API

**Last Updated**: 2025-12-02
