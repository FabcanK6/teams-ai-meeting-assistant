# Architecture

This document describes the architecture of the Teams AI Meeting Assistant.

The system is Microsoft-native, modular, and designed with enterprise governance in mind.

---

## Design Principles

- No audio or video recording
- No persistent live transcription
- Official Microsoft Teams transcript is the system of record
- SharePoint governs access, retention, and audit
- Bot presence is visible and transparent
- Ephemeral processing is separated from persistent data

---

## High-Level Flow

Outlook Calendar
↓
Calendar Monitor
↓
Teams Meeting Bot (auto-join)
↓
Meeting Ends
↓
Transcript Retrieval (Microsoft Graph)
↓
AI Analysis
↓
Document Generation (DOCX)
↓
SharePoint Storage
↓
Teams Notification

---

## Components

### Calendar Monitor
Detects Microsoft Teams meetings on the user’s Outlook calendar and extracts meeting metadata.

### Teams Meeting Bot
Automatically joins meetings as a visible participant and provides in-meeting prompts.

### Transcript Retriever
Retrieves the official Teams transcript after the meeting ends.

### AI Analysis Engine
Converts transcript text into structured summaries, decisions, and action items.

### Document Generator
Creates a DOCX meeting summary using a fixed template.

### SharePoint Writer
Stores the document in SharePoint with standard permissions.

### Teams Notifier
Sends the meeting owner a Teams message with the document link.
