# Vercel Deployment

Vercel supports Django directly through its Python runtime.

## Project configuration

- Repository: `IBPS-Job-Scraper-REST-API`
- Root Directory: `ibps_api`
- Framework: Django / auto-detect
- Production branch: `main`

## Production environment variables

```env
DJANGO_SECRET_KEY=<long-random-secret>
DJANGO_DEBUG=0
DJANGO_ALLOWED_HOSTS=<your-vercel-domain>
DATABASE_URL=postgresql://...
```

Use a hosted PostgreSQL database for persistent production data. SQLite remains the local-development fallback only.

## Before first production use

Run the Django migrations against the production database:

```bash
python manage.py migrate
```

Create an admin user/token only through a secure administrative workflow; do not commit credentials.

## Verify

1. The deployment starts without Django configuration errors.
2. `/api/` responds.
3. Authenticated API requests work with the production token setup.
4. Database writes survive redeployments.
5. Scraping jobs are run intentionally rather than on every web request.
