# Script used to copy over SOLUS (Queen's University Student Center) Course schedule information over to a personal Google Calendar.
from Google import Create_Service
import datetime

CLIENT_SECRET_FILE = './static/credentials.json'
API_NAME = 'calendar'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/calendar']

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

# Call the Calendar API
now = datetime.datetime.utcnow().isoformat() + 'Z'
print(now)
print('Getting the upcoming 10 events...')
events_result = service.events().list(calendarId='primary', timeMin=now,
                                              maxResults=10, singleEvents=True,
                                              orderBy='startTime').execute()
events = events_result.get('items', [])

if not events:
    print('No upcoming events found.')
    exit()

# Prints the start and name of the next 10 events
for event in events:
    start = event['start'].get('dateTime', event['start'].get('date'))
    print(start, event['summary'])
