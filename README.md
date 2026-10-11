# Conjug

Language web application for practicing Spanish and Italian verb conjugation, with user accounts and a leaderboard. Live at [conjug.fr](https://conjug.fr).

## Repository

| Path | Content |
| --- | --- |
| `frontend/` | React, TypeScript, Vite and Tailwind CSS client, served by nginx |
| `backend/` | Flask and SQLAlchemy API on MariaDB, served by gunicorn |
| `admin/` | Administration panel (private submodule) |

## Development

```bash
cp .env.exemple .env
docker compose up --build
```

The client is served on http://localhost:5173 and the API on http://localhost:5000.

## Production

```bash
cp .env.prod.exemple .env.prod
docker compose --env-file .env.prod -f docker-compose.prod.yml up -d --build
```

The empty variables in `.env.prod` are required. No port is published: route the public domain to `user-frontend` on port 80.
