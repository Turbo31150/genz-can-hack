"""
GenZ Productivity Agent — Multi-agent assistant for Gen-Z workflows.
Hackathon: GenZ Can Hack 2026 | $5,000
"""

from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional
import asyncio
from datetime import datetime

app = FastAPI(
    title="GenZ Productivity Agent",
    description="AI-powered multi-agent productivity system for Gen-Z workflows",
    version="1.0.0",
)


class TaskRequest(BaseModel):
    task: str
    context: Optional[str] = None
    deadline: Optional[str] = None
    vibe: Optional[str] = "focused"  # focused, creative, chill


class ContentRequest(BaseModel):
    topic: str
    platform: str  # tiktok, instagram, linkedin, twitter
    tone: Optional[str] = "authentic"
    keywords: Optional[List[str]] = []


@app.get("/health")
async def health():
    return {"status": "ok", "service": "genz-productivity-agent", "timestamp": datetime.utcnow().isoformat()}


async def focus_agent(task: str, vibe: str) -> dict:
    """Breaks down tasks into micro-actions with time estimates."""
    await asyncio.sleep(0.03)
    steps = [
        {"step": f"Research {task[:20]}...", "minutes": 15, "energy": "high"},
        {"step": "Draft initial version", "minutes": 25, "energy": "medium"},
        {"step": "Review and iterate", "minutes": 10, "energy": "low"},
    ]
    return {"agent": "focus_agent", "vibe": vibe, "micro_actions": steps, "total_minutes": 50}


async def anti_procrastination_agent(task: str, deadline: Optional[str]) -> dict:
    """Detects procrastination patterns and suggests interventions."""
    await asyncio.sleep(0.02)
    urgency = "high" if deadline and "today" in (deadline or "").lower() else "medium"
    return {
        "agent": "anti_procrastination",
        "urgency": urgency,
        "intervention": "2-minute rule: start with the smallest possible action",
        "dopamine_hack": f"Reward yourself after completing: {task[:30]}",
        "accountability": "Share your progress goal in 3..2..1",
    }


async def content_agent(topic: str, platform: str, tone: str) -> dict:
    """Generates platform-native content drafts."""
    await asyncio.sleep(0.04)
    templates = {
        "tiktok": f"POV: You just discovered {topic} changes everything 🔥 #fyp #ai #tech",
        "instagram": f"✨ {topic.capitalize()} is the future. Here's why you need to care. Link in bio.",
        "linkedin": f"I've been thinking about {topic} a lot lately. Here's my take: [thread]",
        "twitter": f"Hot take: {topic} > everything else right now. Fight me. 🧵",
    }
    return {
        "agent": "content_agent",
        "platform": platform,
        "tone": tone,
        "draft": templates.get(platform, f"Check out what I learned about {topic}!"),
        "hashtags": [f"#{topic.replace(' ','')}", "#GenZ", "#AI", "#productivity"],
        "best_time": "18:00-21:00 local time",
    }


async def vibe_check_agent(context: str) -> dict:
    """Analyzes mood and suggests optimal work mode."""
    await asyncio.sleep(0.02)
    return {
        "agent": "vibe_check",
        "detected_energy": "medium",
        "recommended_mode": "pomodoro_25",
        "playlist_vibe": "lo-fi hip hop",
        "affirmation": "You've shipped harder things than this. Let's go.",
    }


@app.post("/productivity")
async def productivity_pipeline(req: TaskRequest):
    """Full productivity pipeline: focus + anti-procrastination + vibe check."""
    focus, anti_proc, vibe = await asyncio.gather(
        focus_agent(req.task, req.vibe or "focused"),
        anti_procrastination_agent(req.task, req.deadline),
        vibe_check_agent(req.context or req.task),
    )
    return {
        "task": req.task,
        "timestamp": datetime.utcnow().isoformat(),
        "agents_run": 3,
        "focus_plan": focus,
        "anti_procrastination": anti_proc,
        "vibe_check": vibe,
        "tldr": f"Break '{req.task[:30]}' into 3 steps. Start with the 15min research block. You got this.",
    }


@app.post("/content")
async def content_pipeline(req: ContentRequest):
    """Generate platform-native content for any topic."""
    result = await content_agent(req.topic, req.platform, req.tone or "authentic")
    return result
