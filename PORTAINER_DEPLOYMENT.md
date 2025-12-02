# SmartShopBot - Portainer Deployment Guide

## Overview

This guide explains how to deploy SmartShopBot to your Portainer instance. Portainer provides a user-friendly interface for managing Docker containers and stacks.

## Prerequisites

- Portainer installed and running
- Docker engine with Swarm mode initialized (for Swarm stacks) OR Docker Compose support
- Minimum 2GB RAM available
- Network access to your Portainer instance
- GitHub account or downloaded repository files

## Method 1: Deploy via Portainer Web UI (Recommended)

### Step 1: Access Portainer
1. Open your Portainer URL (typically `http://your-ip:9000`)
2. Login with your credentials
3. Select your Docker engine or Swarm cluster

### Step 2: Create a New Stack
1. Navigate to **Stacks** from the left sidebar
2. Click **Add Stack** button
3. Choose a deployment mode:
   - **Swarm**: For high availability and clustering
   - **Compose**: For single host deployment

### Step 3: Add Stack Content
1. Choose **Web editor** tab
2. Copy and paste the contents of `portainer-stack.yml` into the editor

Alternatively, use **Repository** tab:
```
Repository URL: https://github.com/yourusername/smart-shopping-bot.git
Compose path: portainer-stack.yml
```

### Step 4: Set Environment Variables
Before deploying, configure these environment variables in Portainer:

```env
TELEGRAM_BOT_TOKEN=your_bot_token_here
DB_USER=shopbot
DB_PASSWORD=your_secure_password_here
DB_NAME=smart_shop_bot
OPENAI_API_KEY=sk-your-openai-key
AI_PROVIDER=openai
GOOGLE_VISION_API_KEY=your-vision-key
DEFAULT_LANGUAGE=en
LOG_LEVEL=INFO
```

**Security Notes:**
- Use strong, random passwords
- Store sensitive keys in Portainer Secrets when available
- Never commit `.env` files to Git
- Rotate API keys regularly

### Step 5: Configure Resources (Optional)
In the stack editor, you can add resource limits:

```yaml
services:
  bot:
    deploy:
      resources:
        limits:
          cpus: '1'
          memory: 1G
        reservations:
          cpus: '0.5'
          memory: 512M
```

### Step 6: Deploy Stack
1. Scroll to bottom and click **Deploy the stack**
2. Wait for deployment to complete
3. Monitor stack health in the Portainer dashboard

## Method 2: Command Line Deployment

### Using Docker Stack (Swarm Mode)

```bash
# Initialize Swarm (if not already done)
docker swarm init

# Deploy stack
docker stack deploy -c portainer-stack.yml smartshopbot

# View stack status
docker stack ps smartshopbot

# View stack services
docker stack services smartshopbot

# Update stack
docker stack deploy -c portainer-stack.yml smartshopbot

# Remove stack
docker stack rm smartshopbot
```

### Using Docker Compose (Standalone)

```bash
# Pull latest code
git clone https://github.com/yourusername/smart-shopping-bot.git
cd smart-shopping-bot

# Deploy with compose
docker-compose -f portainer-stack.yml up -d

# View logs
docker-compose -f portainer-stack.yml logs -f bot

# Scale services
docker-compose -f portainer-stack.yml up -d --scale bot=3

# Stop services
docker-compose -f portainer-stack.yml down
```

## Monitoring & Management

### View Logs

In Portainer:
1. Navigate to **Containers** or **Stack Services**
2. Select the `shopbot-app` container
3. Click **Logs** tab
4. Monitor real-time output

### Access Database

```bash
# Connect to PostgreSQL
docker exec -it shopbot-db psql -U shopbot -d smart_shop_bot

# Common queries
SELECT * FROM users;
SELECT * FROM shopping_lists;
SELECT * FROM receipts;
```

### Access Redis Cache

```bash
# Connect to Redis
docker exec -it shopbot-cache redis-cli

# Check cache size
INFO memory

# Flush cache
FLUSHALL
```

### Health Check Status

```bash
# Check service health
docker ps | grep shopbot

# Manual health check
docker exec shopbot-app curl -f http://localhost:8000/health || exit 1
```

## Troubleshooting

### Stack Failed to Deploy

1. **Check Docker space**: `docker system df`
2. **Review logs**: Click Logs in Portainer
3. **Verify variables**: Ensure all required env vars are set
4. **Check networking**: `docker network ls`

### Bot Not Responding

```bash
# Restart bot service
docker service update --force smartshopbot_bot

# Or restart container
docker restart shopbot-app
```

### Database Connection Errors

```bash
# Check PostgreSQL health
docker exec shopbot-db pg_isready -U shopbot

# Verify network connectivity
docker exec shopbot-app ping postgres
```

### High Memory Usage

```bash
# Check memory stats
docker stats shopbot-app

# Reduce cache TTL in portainer-stack.yml
REDIS_TTL=1800  # Reduce from 3600 to 1800 seconds
```

## Scaling the Application

For high-traffic deployments:

```yaml
services:
  bot:
    deploy:
      replicas: 3  # Run 3 instances
      update_config:
        parallelism: 1
        delay: 10s
```

## Backup & Disaster Recovery

### Backup Database

```bash
# Create backup
docker exec shopbot-db pg_dump -U shopbot smart_shop_bot > backup.sql

# Compress backup
gzip backup.sql

# Store securely
mv backup.sql.gz /secure/backup/location/
```

### Restore from Backup

```bash
# Restore database
gunzip < backup.sql.gz | docker exec -i shopbot-db psql -U shopbot smart_shop_bot
```

### Data Persistence

Volumes are automatically created:
- `postgres_data`: PostgreSQL database files
- `redis_data`: Redis cache files

Both persist across container restarts.

## Updating the Bot

```bash
# Pull latest changes from GitHub
cd /path/to/smart-shopping-bot
git pull origin main

# Rebuild image
docker build -t smartshopbot:latest .

# Redeploy stack
docker stack deploy -c portainer-stack.yml smartshopbot
```

## Security Best Practices

1. **Use Secrets for sensitive data**
   ```bash
   echo 'your_token' | docker secret create telegram_token -
   ```

2. **Enable resource limits** (shown above)

3. **Use network isolation**
   ```yaml
   networks:
     shopbot-network:
       driver: bridge
       driver_opts:
         com.docker.network.driver.mtu: 1450
   ```

4. **Regular backups** (daily minimum)

5. **Monitor logs** for errors and anomalies

6. **Keep Docker updated** to latest stable version

## Performance Optimization

### Increase Cache TTL for More Performance
```yaml
environment:
  REDIS_TTL: 7200  # 2 hours
```

### Database Connection Pooling
```yaml
environment:
  DATABASE_POOL_SIZE: 20
  DATABASE_MAX_OVERFLOW: 40
```

### AI Service Rate Limiting
Control costs by limiting API calls (implemented in code).

## Additional Resources

- [Portainer Documentation](https://docs.portainer.io/)
- [Docker Compose Reference](https://docs.docker.com/compose/compose-file/)
- [Docker Stack Reference](https://docs.docker.com/compose/compose-file/compose-file-v3/)
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)
- [Redis Documentation](https://redis.io/documentation)

## Support

For issues:
1. Check logs in Portainer
2. Review troubleshooting section above
3. Open GitHub issue with log output
4. Contact administrators

---

**Last Updated**: 2025-12-02
**Version**: 2.0.0
