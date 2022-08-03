# Script used to copy over SOLUS (Queen's University Student Center) Course schedule information over to a personal Google Calendar.
from Google import Create_Service
import datetime
import webbrowser

CLIENT_SECRET_FILE = './static/credentials.json'
API_NAME = 'calendar'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/calendar']

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

# Prompt user to login to SOLUS
print("Once you are logged into your Queen's account, Type: \"ready\"")
webbrowser.open("https://login.microsoftonline.com/")

ans = input().lower()
if ans is not "ready": exit()





# Call the Calendar API
# now = datetime.datetime.utcnow().isoformat() + 'Z'
# print(now)
# print('Getting the upcoming 10 events...')
# events_result = service.events().list(calendarId='primary', timeMin=now,
#                                               maxResults=10, singleEvents=True,
#                                               orderBy='startTime').execute()
# events = events_result.get('items', [])

# if not events:
#     print('No upcoming events found.')
#     exit()

# # Prints the start and name of the next 10 events
# for event in events:
#     start = event['start'].get('dateTime', event['start'].get('date'))
#     print(start, event['summary'])

######################################

# post a new event to the Calendar:
# event = {
#   'summary': 'Google I/O 2015',
#   'location': '800 Howard St., San Francisco, CA 94103',
#   'description': 'A chance to hear more about Google\'s developer products.',
#   'start': {
#     'dateTime': '2022-08-04T09:00:00-07:00',
#     'timeZone': 'America/Los_Angeles',
#   },
#   'end': {
#     'dateTime': '2022-08-04T17:00:00-07:00',
#     'timeZone': 'America/Los_Angeles',
#   },
# }

# event = service.events().insert(calendarId='primary', body=event).execute()
# print('Event created: %s' % (event.get('htmlLink')))
