"""Tests for GenZ Productivity Agent API."""

import pytest
from httpx import AsyncClient, ASGITransport
from main import app


@pytest.mark.asyncio
async def test_health():
    async with AsyncClient(
        transport=ASGITransport(app=app), base_url="http://test"
    ) as c:
        r = await c.get("/health")
    assert r.status_code == 200
    assert r.json()["status"] == "ok"


@pytest.mark.asyncio
async def test_productivity_pipeline():
    async with AsyncClient(
        transport=ASGITransport(app=app), base_url="http://test"
    ) as c:
        r = await c.post(
            "/productivity",
            json={"task": "build my hackathon project", "vibe": "focused"},
        )
    assert r.status_code == 200
    data = r.json()
    assert data["agents_run"] == 3
    assert "focus_plan" in data
    assert "anti_procrastination" in data
    assert "vibe_check" in data


@pytest.mark.asyncio
async def test_content_pipeline():
    async with AsyncClient(
        transport=ASGITransport(app=app), base_url="http://test"
    ) as c:
        r = await c.post("/content", json={"topic": "AI agents", "platform": "tiktok"})
    assert r.status_code == 200
    data = r.json()
    assert "draft" in data
    assert "hashtags" in data
    assert data["platform"] == "tiktok"


@pytest.mark.asyncio
async def test_content_all_platforms():
    platforms = ["tiktok", "instagram", "linkedin", "twitter"]
    async with AsyncClient(
        transport=ASGITransport(app=app), base_url="http://test"
    ) as c:
        for p in platforms:
            r = await c.post("/content", json={"topic": "productivity", "platform": p})
            assert r.status_code == 200, f"Platform {p} failed"
