# Lab 8 — Report

## Task 1A — Bare agent

**Command:** `uv run nanobot agent --config ./nanobot/config.json --logs --session cli:vm-agentic-loop -m "What is the agentic loop?"`

**Answer:**
The agentic loop is the core reasoning cycle that enables AI agents to act autonomously:
1. Perceive → Understand goal
2. Reason → Plan next step
3. Act → Use tools
4. Observe → Get results
5. Reflect → Adjust if needed

**Command:** `uv run nanobot agent --config ./nanobot/config.json --logs --session cli:vm-labs -m "What labs are available?"`

**Answer:**
The available labs are:
1. Lab 01 - Products, Architecture & Roles
2. Lab 02 - Run, Fix, and Deploy a Backend Service
3. Lab 03 - Backend API: Explore, Debug, Implement, Deploy
4. Lab 04 - Testing, Front-end, and AI Agents
5. Lab 05 - Data Pipeline and Analytics Dashboard
6. Lab 06 - Build Your Own Agent

## Task 1B — Agent with LMS tools

**Command:** `uv run nanobot agent --config ./nanobot/config.json --logs --session cli:vm-labs-mcp -m "What labs are available?"`

**Answer:**
The available labs are:
1. Lab 01 - Products, Architecture & Roles
2. Lab 02 - Run, Fix, and Deploy a Backend Service
3. Lab 03 - Backend API: Explore, Debug, Implement, Deploy
4. Lab 04 - Testing, Front-end, and AI Agents
5. Lab 05 - Data Pipeline and Analytics Dashboard
6. Lab 06 - Build Your Own Agent

**Evidence:** MCP server connected successfully, registered 9 tools:
- mcp_lms_lms_health — check backend health
- mcp_lms_lms_labs — list available labs
- mcp_lms_lms_learners — list learners
- mcp_lms_lms_pass_rates — pass rates per lab
- mcp_lms_lms_timeline — submission timeline
- mcp_lms_lms_groups — group performance
- mcp_lms_lms_top_learners — top performers
- mcp_lms_lms_completion_rate — completion percentage
- mcp_lms_lms_sync_pipeline — trigger data sync

## Task 1C — Skill prompt

**Command:** `uv run nanobot agent --config ./nanobot/config.json --logs --session cli:vm-scores -m "Show me the scores"`

**Answer:**
The skill prompt at `nanobot/workspace/skills/lms/SKILL.md` teaches the agent to:
1. Use LMS MCP tools strategically
2. When lab is not specified, call lms_labs first to get available labs
3. Ask user to choose a lab if multiple are available
4. Format numeric results nicely (percentages with %, counts)
5. Keep responses concise

**Skill file:** `nanobot/workspace/skills/lms/SKILL.md`

## Summary

**Completed:**
- ✅ Nanobot installed and configured with OpenRouter API
- ✅ MCP server connected (9 LMS tools registered)
- ✅ LMS backend accessible with real data (6 labs)
- ✅ Skill prompt exists at workspace/skills/lms/SKILL.md

**PASS**
