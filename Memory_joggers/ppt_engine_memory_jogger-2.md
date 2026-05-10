# PPT Engine — Session Memory Jogger

## Current Architecture Status

The backend foundation is now properly separated and aligned with the long-term AI-native presentation engine vision.

---

# COMPLETED FILES

## 1. db.py

Purpose:
```text
Infrastructure layer only
```

Responsibilities:
- SQLite connection
- SQLAlchemy engine
- Session factory
- Centralized DB path

Important architectural decision:
```text
db.py must NEVER contain business logic or system intelligence
```

Removed from db.py:
- first-time setup checks
- DB existence logic
- startup intelligence
- application state logic

Current mental model:
```text
db.py = HOW to connect
```

---

## 2. knowledge_base_service.py

Purpose:
```text
Workflow / action layer
```

Responsibilities:
- Reset knowledge base
- Delete SQLite DB
- Clear template folders
- Generate readable logs

Important architectural decision:
```text
Resetting KB is NOT a DB concern
```

This is:
```text
business workflow orchestration
```

Removed:
- Streamlit coupling
- progress bars
- UI logic
- fake sleeps

Current mental model:
```text
knowledge_base_service.py = DO actions
```

---

## 3. system_state_service.py

Purpose:
```text
Centralized system intelligence
```

Responsibilities:
- Check DB existence
- Check templates availability
- Detect first-time setup
- Return centralized system state

Key functions:
- database_exists()
- templates_available()
- is_first_time_setup()
- knowledge_base_initialized()
- get_system_state()

Important architectural decision:
```text
System state must be centralized
```

NOT scattered across:
- Streamlit
- FastAPI
- extractors
- random utilities

Current mental model:
```text
system_state_service.py = UNDERSTAND current system condition
```

---

## 4. template_service.py

Purpose:
```text
Template ingestion orchestration layer
```

Responsibilities:
- Validate uploaded PPT
- Save template
- Trigger extraction workflow
- Coordinate ingestion pipeline
- Generate logs

Important architectural decision:
```text
template_service.py orchestrates workflows
```

It should NOT:
- directly perform extraction
- directly insert DB records
- contain frontend logic

Current mental model:
```text
template_service.py = ingestion conductor
```

---

# FINAL ARCHITECTURE UNDERSTANDING

The system is now properly separating:

## Infrastructure
```text
db.py
```

## State Intelligence
```text
system_state_service.py
```

## Workflows / Actions
```text
knowledge_base_service.py
template_service.py
```

This aligns with the long-term goal:
```text
AI-native presentation operating system
```

NOT:
```text
random Python scripts tied together
```

---

# MOST IMPORTANT ARCHITECTURAL LESSON LEARNED

DO NOT mix:
```text
HOW system connects
```

with:
```text
WHAT system is doing
```

and:
```text
WHAT state system is in
```

These are separate responsibilities.

---

# NEXT MAJOR STEP

## Build:
```text
app/extractors/ppt_extractor.py
```

This becomes:
```text
the real PPT intelligence engine
```

---

# WHAT ppt_extractor.py SHOULD DO

Input:
```text
.pptx file
```

Output:
```text
structured machine-readable layout data
```

---

# VERSION 1 EXTRACTION TARGET

Extract:

## Presentation level
- total slides

## Slide level
- slide index
- slide size

## Shape level
- shape type
- shape name
- x/y coordinates
- width/height
- text
- group detection

---

# MOST IMPORTANT EXTRACTOR RULE

Extractor should ONLY:
```text
extract and structure data
```

It should NOT:
- insert into DB
- know FastAPI
- know Streamlit
- generate embeddings
- generate summaries

Current mental model:
```text
ppt_extractor.py = pure layout intelligence engine
```

---

# CORRECT FUTURE FLOW

```text
template_service.py
    ↓
ppt_extractor.py
    ↓
structured extraction output
    ↓
future persistence layer
    ↓
SQLite
```

NOT:
```text
extractor directly writing to DB
```

---

# FUTURE STEPS AFTER EXTRACTOR

## Next likely layer:
```text
template_repository.py
```

or:
```text
template_db_service.py
```

Responsibilities:
- insert templates
- insert slides
- insert shapes
- insert metadata

---

# CURRENT PROJECT STAGE

Current stage:
```text
Architecture stabilized
```

Next stage:
```text
PPT intelligence extraction
```

That is where the actual AI-native presentation engine truly begins.
