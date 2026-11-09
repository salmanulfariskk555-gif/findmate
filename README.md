# FindMate

A privacy-first matchmaking platform for adults seeking serious relationships and marriage.

## Project packages
- `web/` — responsive React + Vite landing-page foundation
- `mobile/` — Expo React Native Android starter
- `backend/` — Django REST API foundation

## Implemented foundation
- Premium responsive landing page and mobile starter screen
- Django project configuration and REST API routes
- Adult (18+) self-reported birth-date validation at registration
- Private-by-default profiles and admin approval gate for discovery
- Profile editing, discover list, likes, mutual-match listing
- Block and report endpoints
- Initial registration and safety endpoint tests

## Not yet implemented / not production-ready
Email/phone verification and OTP, photo upload and moderation, private real-time messaging, advanced compatibility filters, subscription billing, payment webhooks, account deletion/export, full admin moderation workflow, Android release build, hosting and production monitoring.

## Local development
See `web/README.md`, `mobile/README.md`, and `backend/SETUP.md`.

## Safety
FindMate is intended for adults 18+ only. Birth date is currently self-reported, not identity-verified. Do not onboard real users until verification, privacy controls, moderation, abuse response, account deletion, security testing and applicable legal review are complete. Never commit secrets, access tokens or real user data.
