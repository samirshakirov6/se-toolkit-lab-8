---
name: observability
description: Use observability MCP tools to investigate errors, logs, and traces
always: true
---

# Observability Skill

You have access to observability tools that let you query VictoriaLogs and VictoriaTraces for the LMS backend.

## Available Tools

- mcp_obs_logs_error_count - Count errors for a service over a time window
- mcp_obs_logs_search - Search logs using LogsQL to find specific entries and trace IDs
- mcp_obs_traces_list - List recent traces for a service
- mcp_obs_traces_get - Fetch a specific trace by ID

## Triggers

These messages MUST trigger full automatic investigation with NO clarifying questions:
- What went wrong?
- What happened?
- Check system health
- Investigate the failure
- Why is it broken?

## Investigation Flow for trigger messages

Execute ALL steps in order WITHOUT stopping:

1. Call mcp_obs_logs_error_count with service=Learning Management Service and minutes=10
2. If errors exist, call mcp_obs_logs_search with query `_time:10m severity:ERROR event:db_query` and limit=5
3. Extract the FIRST trace_id from results
4. Call mcp_obs_traces_get with that trace_id
5. Output the template below

## Response Template for trigger messages

Investigation results for the Learning Management Service:

Log evidence: N errors in last 10m. Error type: X. Affected operation: Y.

Trace evidence: Trace Z shows failure in span W at operation V.

Root cause: Service A failed during operation B. HTTP response reported code C but logs/traces show real error is D.

Conclusion: One sentence summary.

## Rules

- NEVER ask follow-up questions for trigger messages
- ALWAYS call all three tools before answering
- Highlight discrepancies between HTTP response and log/trace evidence
- Never dump raw JSON

## For other error queries

Call error_count, then logs_search if errors exist, then traces_get for a trace_id. Summarize concisely.

## Response Style

- Plain language summaries
- No raw JSON dumps
- Say clearly if no errors found
