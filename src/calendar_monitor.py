"""
Calendar Monitor

Initial stub for detecting calendar events.
This will later integrate with Microsoft Graph.
"""

from typing import List, Dict

def list_upcoming_meetings(events: List[Dict]) -> List[Dict]:
    """
    Convert raw calendar events into simplified meeting metadata.

    Args:
        events: List of calendar events

    Returns:
        List of simplified meeting dictionaries
    """
    meetings = []

    for event in events:
        meetings.append({
            "subject": event.get("subject"),
            "start": event.get("start"),
            "end": event.get("end"),
            "location": event.get("location"),
        })

    return meetings
