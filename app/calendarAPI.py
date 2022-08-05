# This script calls the Google Calendar API using the objects created in main.py

from Google import Create_Service

CLIENT_SECRET_FILE = "./static/credentials.json"
API_NAME = "calendar"
API_VERSION = "v3"
SCOPES = ["https://www.googleapis.com/auth/calendar"]

def callAPI(course):
    service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)
    
    event = {
        'summary': course.name,
        'start': {
            'dateTime': course.startDateTime,
            'timeZone': 'America/New_York',
        },
        'end': {
            'dateTime': course.endDateTime,
            'timeZone': 'America/New_York',
        },
        'recurrence': [
            'RRULE:FREQ=WEEKLY;COUNT=12'
        ],
    }


    event = service.events().insert(calendarId='primary', body=event).execute()
    print('Event created: %s' % (event.get('htmlLink')))
