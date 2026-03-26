# Teams AI Meeting Assistant
**Microsoft Teams–native AI meeting assistant with SharePoint system of record**

---

## Project Status

This project is in early active development.

Current focus:
- Repository setup and documentation
- Defining the system architecture
- Planning calendar-driven auto-join and post-meeting processing

Code will be added incrementally as each phase is implemented.

---

## Overview

This project implements a Microsoft Teams–native AI meeting assistant that:

- Automatically joins Microsoft Teams meetings on the user’s calendar
- Acts as a visible meeting participant for transparency
- Supports accountability during meetings (action items, decisions)
- Generates one structured document per meeting after the meeting ends
- Saves meeting records to SharePoint under existing governance
- Sends the meeting owner a Teams message with the document link

The goal is to eliminate manual note-taking and missed follow-ups while creating a reliable system of record for meetings.

---

## What This Project Is

- A Teams-native automation
- A calendar-driven meeting assistant
- A post-meeting documentation pipeline
- A SharePoint-governed system of record

---

## What This Project Is Not

- Not a recording tool
- Not an audio capture system
- Not a background or hidden listener
- Not a third-party SaaS meeting bot

No audio or video is recorded or stored.

---

## High-Level Architecture
- Outlook Calendar
- Calendar Monitor
- Teams Meeting Bot (auto-join)
- Meeting Ends
- Transcript Retrieval (Microsoft Graph)
- AI Analysis
- Document Generation (DOCX)
- SharePoint Storage
- Teams Notification

---

## Core Capabilities

### During the Meeting

- Bot auto-joins as a visible participant
- Provides real-time prompts for:
  - Action item ownership
  - Due dates
  - Decision confirmation
- All in-meeting analysis is ephemeral and discarded

### After the Meeting

- Retrieves the official Microsoft Teams transcript
- Generates a structured meeting summary
- Creates a single DOCX document per meeting
- Saves the document to SharePoint
- Notifies the meeting owner via Teams

---

## Meeting Document Structure

Each meeting generates one SharePoint document containing:

1. Meeting header (title, date, organizer, attendees)
2. Executive summary
3. Decisions made
4. Action items with owners and due dates
5. Key discussion points
6. Open questions or parking-lot items

The format is consistent across all meetings.

---

## Governance and Compliance

- No meetings are recorded
- No live audio or captions are stored
- Persistent documentation is generated only from official Teams transcript artifacts
- All outputs are stored in SharePoint with standard access controls
- The bot is visible in meetings for transparency

---

## Planned Technology Stack

- Microsoft Teams
- Microsoft Graph (Calendar, Meetings, Transcripts)
- SharePoint Online
- Azure Functions or equivalent compute
- Azure-approved LLM endpoint for summarization

No third-party meeting capture tools are used.

---

## Development Roadmap (High Level)

1. Calendar monitoring and meeting detection
2. Teams bot auto-join and presence
3. Post-meeting transcript retrieval
4. AI-based meeting analysis
5. SharePoint document generation
6. Teams notification workflow
7. Optional real-time in-meeting assistance

---

## Final Notes

This project prioritizes reliability, governance, and transparency over novelty.

The intent is to ensure time spent in meetings reliably results in documented decisions and accountable follow-through.
