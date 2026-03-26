# Security and Governance

This document outlines security, privacy, and governance controls for the Teams AI Meeting Assistant.

---

## Data Handling

### Data Never Collected or Stored
- Audio
- Video
- Live captions
- Bot-generated live transcripts

### Data That Is Stored
- AI-generated summaries derived from official Teams transcript artifacts
- Structured meeting documents (DOCX)

---

## Source of Truth

- Persistent documentation is generated only from Microsoft Teams transcript artifacts
- Transcripts are governed by Microsoft 365 policies

---

## Storage and Access Control

- All documents are stored in SharePoint Online
- SharePoint enforces permissions, retention, and audit logging
- No local or external storage is used

---

## Bot Transparency

- The bot joins meetings as a visible participant
- No background or hidden operation

---

## AI Usage

- AI is used only for summarization and structuring
- No model training on company data
- No data is shared with unapproved services

---

## Summary

The system prioritizes data minimization, transparency, and enterprise-safe automation.
