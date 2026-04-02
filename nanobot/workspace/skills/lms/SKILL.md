---
name: lms
description: Use LMS MCP tools for live course data
always: true
---

# LMS Skill

You have access to LMS (Learning Management System) tools via MCP. Use them to provide accurate, real-time information about the course.

## Available Tools

- `mcp_lms_lms_health` — Check if the LMS backend is healthy and get item count
- `mcp_lms_lms_labs` — List all available labs
- `mcp_lms_lms_learners` — List all enrolled learners
- `mcp_lms_lms_pass_rates` — Get pass rates for a specific lab
- `mcp_lms_lms_timeline` — Get submission timeline for a specific lab
- `mcp_lms_lms_groups` — Get group performance for a specific lab
- `mcp_lms_lms_top_learners` — Get top performing learners for a specific lab
- `mcp_lms_lms_completion_rate` — Get completion rate for a specific lab
- `mcp_lms_lms_sync_pipeline` — Trigger data sync from the autochecker API

## Strategy Rules

### When user asks about scores, pass rates, completion, groups, timeline, or top learners WITHOUT naming a lab:

1. First call `mcp_lms_lms_labs` to get the list of available labs
2. If multiple labs exist, ask the user to choose one
3. Present lab titles as user-facing labels (e.g., "lab-01", "lab-02")
4. Let the shared structured-ui skill decide how to present the choice on supported channels

### When user asks "what can you do?":

Explain your current capabilities clearly:
- You can check LMS backend health
- You can list available labs
- You can provide analytics for specific labs: pass rates, completion rates, timeline, group performance, top learners
- You can trigger data sync if the backend data is stale

### Formatting Guidelines

- Format percentages with % symbol (e.g., "75%")
- Format counts with numbers (e.g., "15 learners")
- Keep responses concise and structured
- Use bullet points for lists
- Always mention the data source when presenting analytics ("According to LMS data...")

### Error Handling

- If the LMS backend is unhealthy, inform the user and suggest triggering sync
- If a tool fails, explain what went wrong and suggest alternatives
- If no data is available for a lab, say so clearly rather than guessing

## Example Interactions

**User:** "Show me the scores"
**You:** (Call `mcp_lms_lms_labs` first) → "Which lab would you like to see scores for? We have: lab-01, lab-02"

**User:** "What labs are available?"
**You:** (Call `mcp_lms_lms_labs`) → "There are X labs available: [list them]"

**User:** "Is the system healthy?"
**You:** (Call `mcp_lms_lms_health`) → "The LMS backend is healthy/unhealthy. [details]"
