"""
Tests for calendar_monitor module.

These tests validate basic behavior of the calendar monitor logic.
"""

from src.calendar_monitor import list_upcoming_meetings


def test_list_upcoming_meetings_returns_expected_fields():
    sample_events = [
        {
            "subject": "Test Meeting",
            "start": "2026-03-26T10:00:00",
            "end": "2026-03-26T10:30:00",
            "location": "Microsoft Teams Meeting",
        }
    ]

    meetings = list_upcoming_meetings(sample_events)

    assert len(meetings) == 1
    assert meetings[0]["subject"] == "Test Meeting"
    assert meetings[0]["location"] == "Microsoft Teams Meeting"
