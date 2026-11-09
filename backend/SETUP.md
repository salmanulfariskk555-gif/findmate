# FindMate API — local setup

## Run locally
1. Create a Python virtual environment and install the packages in requirements.txt.
2. Set DJANGO_SECRET_KEY and DJANGO_DEBUG=true for local development.
3. Run python manage.py migrate.
4. Run python manage.py createsuperuser.
5. Run python manage.py runserver.

## API endpoints
- POST /api/auth/register/ — username, password, display_name, birth_date (18+ only).
- POST /api/auth/login/ — username, password.
- GET/PATCH /api/me/ — retrieve or update your profile.
- DELETE /api/account/delete/ — send the current password in JSON to confirm permanent account deletion.
- GET /api/discover/ — approved and visible profiles only.
- POST /api/like/{user_id}/ — like an eligible profile.
- GET /api/matches/ — mutual likes.
- POST /api/block/{user_id}/ — block a member and remove likes between both accounts.
- POST /api/report/{user_id}/ — submit a report with a 10–300 character reason.

Use Authorization: Token <token> for authenticated endpoints.

## Admin moderation
The Django admin allows staff to approve profiles, hide profiles from discovery, and review submitted reports. Only trusted staff should receive admin access.

## Important launch limitations
This is an early development foundation, not production-ready. Registration currently trusts a self-reported birth date and does not verify email or phone. Authentication tokens do not expire automatically. There is no chat, photo upload/moderation, payment system, OTP, account export, or production hosting yet. Complete security, privacy, abuse-prevention, legal and operational reviews before accepting real users.
