# GenZ Productivity Agent — Devpost Submission

## Project Title
**GenZ Productivity Agent**: AI Multi-Agent Productivity System for the Always-Online Generation

## Tagline
Focus mode → anti-procrastination → vibe check → content drop. All in one slash command.

## The Problem
Gen-Z workers face a unique productivity paradox: hyper-connected, highly capable, yet chronically distracted. Traditional productivity tools were designed for a different era — linear, text-heavy, and devoid of dopamine. Meanwhile, Gen-Z has to manage school/work tasks, social media presence, and mental bandwidth all at once.

## Our Solution
**GenZ Productivity Agent** is a multi-agent API that combines task decomposition, anti-procrastination interventions, mood-adaptive work modes, and platform-native content generation — all running in parallel.

Three core pipelines:
1. **Productivity Pipeline** (`POST /productivity`): Breaks any task into micro-actions (focus_agent), detects procrastination patterns (anti_procrastination_agent), and reads your vibe (vibe_check_agent) — 3 agents running via asyncio.gather()
2. **Content Pipeline** (`POST /content`): Generates platform-native content for TikTok, Instagram, LinkedIn, Twitter
3. **Health check** (`GET /health`): Service monitoring

## Tech Stack
- Python, FastAPI, asyncio, Pydantic v2
- Multi-agent architecture (3 parallel agents)
- Deployable locally or on any cloud

## GitHub
https://github.com/Turbo31150/genz-can-hack

## Team
Turbo31150 — Multi-agent systems engineer. Solo hacker.
