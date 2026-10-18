---
name: quiz
description: Quiz the user on concepts they're studying (MCP, Claude API, agents, skills). Use when the user asks to be quizzed, tested, or to review what they learned.
---

Topic: $ARGUMENTS (if empty, pick from notes/learning-log.md, favoring weak spots)

1. Read notes/learning-log.md to see topics covered and past mistakes.
2. Ask ONE question at a time. Mix the types:
   - Concept ("When would you expose data as a resource instead of a tool?")
   - Write-the-code ("Write an @mcp.tool that edits a doc by find/replace")
   - Predict/debug (show a snippet with a bug, ask what breaks)
3. Wait for my answer before revealing anything. Grade it, explain the gaps.
4. After 5 questions, append a dated summary to notes/learning-log.md:
   what I got right, what I missed, and what to review next.
