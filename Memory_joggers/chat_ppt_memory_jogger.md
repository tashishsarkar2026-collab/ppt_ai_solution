# Chat PPT Engine — Memory Jogger

## Core Product Vision

Build a local-first AI-powered PPT engine that:

- Understands infographic-heavy PPT templates
- Extracts layouts, placeholders, structures, groups, charts, and metadata
- Builds a reusable knowledge base of presentation structures
- Generates professional editable PPTs
- Suggests charts/tables/layouts automatically
- Uses local LLMs via LM Studio / Ollama
- Works fully offline if required

---

# FINAL ARCHITECTURAL DECISIONS

## Architecture Style

Final decision:

```text
Hybrid Modular Monolith
```

Meaning:

- Single deployable app initially
- Modular internal services
- FastAPI as orchestration layer
- Future-ready for microservice split

---

# MAIN PRINCIPLE

## main.py

Final decision:

```text
main.py = orchestration layer only
```

It should:

- expose APIs
- trigger services
- route requests
- manage workflows

It should NOT contain:

- extraction logic
- DB logic
- AI logic
- PPT generation logic

---

# DATABASE ARCHITECTURE

## db.py

Final decision:

```text
db.py = connector/plumbing only
```

Responsibilities:

- SQLAlchemy engine
- DB session creation
- DB existence checks
- SQLite path management

It should NOT contain:

- append logic
- extraction logic
- ingestion logic
- business logic

---

# WHY THIS MATTERS

Wrong approach:

```text
db.py becomes backend brain
```

This causes:

- spaghetti architecture
- circular imports
- debugging nightmares
- scaling issues

Correct approach:

```text
Frontend
    ↓
FastAPI Endpoint
    ↓
Service Layer
    ↓
Extractor / DB Layer
    ↓
SQLite
```

---

# SERVICE LAYER DECISION

Final decision:

```text
All business workflows go into services
```

Example future services:

```text
template_service.py
generation_service.py
chat_service.py
layout_service.py
system_state_service.py
knowledge_base_service.py
```

---

# SYSTEM STATE VS ACTIONS

CRITICAL FINAL DECISION

Do NOT mix:

```text
Actions
```

with

```text
System State
```

---

## Actions

Examples:

```text
reset_database()
append_template()
generate_ppt()
```

These DO things.

---

## System State

Examples:

```text
database_exists()
is_first_time_setup()
knowledge_base_empty()
```

These CHECK things.

---

# KNOWLEDGE BASE FLOW

## Reset Flow

```text
Frontend Toggle
        ↓
FastAPI Endpoint
        ↓
reset_database()
        ↓
DB deleted
        ↓
System state changes
        ↓
Frontend reacts
```

---

# FIRST-TIME SETUP FLOW

If DB not found:

Logs should say:

```text
Database not found
Running first-time setup
New SQLite database will be created
```

Frontend should show:

```text
Please upload templates to initialize knowledge base
```

---

# TEMPLATE INGESTION FLOW

Final decision:

```text
template_service.py handles ingestion
```

Responsibilities:

- save uploaded PPT
- extract PPT structure
- insert metadata
- insert slides
- insert shapes
- future embedding generation
- future LLM metadata enrichment

---

# FRONTEND DECISIONS

## Streamlit Tabs

### Tab 1

```text
Knowledge Base Setup
```

Responsibilities:

- upload templates
- reset knowledge base
- extraction progress
- metadata collection

---

### Tab 2

```text
PPT Generation Studio
```

Responsibilities:

- chat interface
- structured data
- AI presentation generation
- editable PPT export
- chart recommendations
- layout recommendations

---

# TEMPLATE METADATA DECISION

## Category

Final decision:

```text
Dropdown
```

Why:

- consistency
- clean filtering
- easier retrieval
- better vector search

---

## Purpose / Context

Final decision:

```text
Free text
```

Why:

- richer LLM context
- flexible semantic meaning
- future prompt enrichment

---

# INFOGRAPHIC EXTRACTION DECISION

Final decision:

```text
Convert PPT into structured machine-readable layout data
```

Extraction captures:

- shape type
- groups
- coordinates
- dimensions
- nested children
- text
- slide hierarchy

---

# MOST IMPORTANT TABLE

```text
shape_objects
```

This becomes:

```text
future layout intelligence foundation
```

---

# FUTURE AI FLOW

User gives:

- prompt
- company logo
- brand colors
- structured data
- optional template

System decides:

- layouts
- chart types
- infographic usage
- spacing
- visual hierarchy
- slide arrangement

---

# CRITICAL TRUTH ABOUT MCKINSEY-LEVEL PPTS

Final agreed truth:

AI alone will NOT create:
- strategy
- storytelling
- business insight

User provides:
- thinking
- insights
- narrative

AI handles:
- structure
- formatting
- visual arrangement
- grammar
- professional polish

---

# LOCAL-FIRST DECISION

Final decision:

Use:

```text
LM Studio / Ollama
```

instead of cloud dependency.

Reason:

- local usage
- privacy
- portability
- offline capability

---

# DATABASE DECISION

Final decision:

```text
SQLite
```

instead of PostgreSQL initially.

Reason:

- portability
- easy Mac migration
- zero setup
- local-first simplicity

---

# SQLITE PATH DECISION

Final decision:

DB MUST always stay inside:

```text
project_root/ppt_engine.db
```

Absolute paths only.

Never relative paths.

---

# GITIGNORE DECISION

Must ignore:

```text
*.db
.env
templates/raw
outputs
__pycache__
```

Reason:

Code repo != data repo

---

# LOGGING DECISION

Final decision:

Centralized logger.

```text
app/utils/logger.py
```

Logs should be:

- human readable
- stage-based
- progress-oriented

NOT raw SQL spam.

---

# EXTRACTION UX DECISION

Frontend should show:

- progress bars
- slide counts
- extraction progress
- infographic counts
- completion status

NOT raw console dumps.

---

# FUTURE VISION

Long-term system goal:

```text
AI-native editable presentation operating system
```

Capabilities:

- reusable layout intelligence
- semantic slide generation
- infographic recommendation
- editable PPT creation
- business-quality visual arrangement
- local AI workflows

---

# CURRENT PROJECT STATUS

Completed:

- project structure
- SQLite setup
- extractor
- recursive group extraction
- Streamlit frontend
- FastAPI orchestration start
- reset DB workflow
- centralized logging
- progress bars
- tab-based UI

Next likely steps:

1. template_service.py
2. system_state_service.py
3. DB insertion service layer
4. template metadata persistence
5. embedding pipeline
6. retrieval layer
7. layout recommendation engine
8. PPT generation engine
