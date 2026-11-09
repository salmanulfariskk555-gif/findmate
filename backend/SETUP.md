# FindMate API — local setup
1. Create Python virtual environment and install requirements.
2. Copy .env.example to .env and export environment variables (Django does not load .env automatically).
3. Run `python manage.py makemigrations members`.
4. Run `python manage.py migrate`.
5. Run `python manage.py createsuperuser`.
6. Run `python manage.py runserver`.

## Endpoints
- POST /api/auth/register/ (username, password, display_name, birth_date)
- POST /api/auth/login/ (username, password)
- GET/PATCH /api/me/ (Authorization: Token ...)
- GET /api/discover/
- POST /api/like/{user_id}/
- GET /api/matches/
- POST /api/block/{user_id}/
- POST /api/report/{user_id}/ (reason)

## Important
This is an early backend implementation, not production-ready. Add verified email/phone, account deletion, rate limits per endpoint, stronger anti-abuse systems, moderation policies, profile photo safety, token revocation, privacy/legal review, audit logging, tests and secure deployment before accepting real users. The age gate currently checks a self-reported birth date, not identity verification. Login tokens are long-lived. Do not launch publicly yet.
