# Operational Runbook

This runbook explains how the Teams AI Meeting Assistant operates and how to troubleshoot common issues.

---

## Normal Operation

1. Bot monitors Outlook calendar
2. Bot auto-joins Teams meetings
3. Meeting occurs
4. Meeting ends
5. Transcript is retrieved
6. Document is generated
7. Document is saved to SharePoint
8. Teams notification is sent

---

## Common Issues

### Transcript Not Available
- Cause: Transcription disabled or delayed
- Behavior: Document generation is skipped safely

### Bot Does Not Join Meeting
- Cause: Invalid join link or permission issue
- Behavior: Meeting proceeds normally without bot assistance

### SharePoint Save Failure
- Cause: Permission or service issue
- Behavior: No partial document is saved

---

## Monitoring

Recommended checks:
- Calendar detection success
- Transcript retrieval success
- Document generation success
- SharePoint write success
- Teams notification delivery

---

## Maintenance

- Review permissions periodically
- Update templates cautiously
- Keep document structure stable
