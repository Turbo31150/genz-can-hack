# GenZ Productivity Agent

Multi-agent AI productivity system for Gen-Z workflows.

## Quick Start
```bash
pip install fastapi uvicorn pydantic
uvicorn main:app --reload --port 8000
```

## Endpoints
- `POST /productivity` — full productivity pipeline (3 parallel agents)
- `POST /content` — platform-native content generation
- `GET /health` — service health check

## Built for GenZ Can Hack 2026
