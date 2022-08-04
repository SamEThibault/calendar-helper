# Script used to copy over SOLUS (Queen's University Student Center) Course schedule information over to a personal Google Calendar.
import time
import getpass
from Google import Create_Service
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

CLIENT_SECRET_FILE = "./static/credentials.json"
API_NAME = "calendar"
API_VERSION = "v3"
SCOPES = ["https://www.googleapis.com/auth/calendar"]

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

driver = webdriver.Chrome(ChromeDriverManager().install())
time.sleep(2)
# Logging in to MS Live account procedure
# Need to do some assertions throughout the redirects to ensure that no errors have occured
driver.get("https://portal.office.com")

# prompt user to enter email, populate input field, try to submit the form.
while True:
    try:
        print("Enter your Queen's Email: ")
        email = input().lower()

        emailField = driver.find_element(By.ID, "i0116")
        emailField.send_keys(email)
        nextButton = driver.find_element(By.ID, "idSIButton9").click()
        time.sleep(2)

        # check to see if an error was thrown, if so, try again
        driver.find_element(By.ID, 'usernameError')
        print("The email you've entered is incorrect.")
        emailField.clear()
    except:
        # if no usernameError element exists, we assume email input was successful
        break

# prompt user to enter password, populate input field, try to submit form
while True:
    try:
        print("Enter your password: ")
        password = getpass.getpass()
        pwField = driver.find_element(By.ID, "i0118")
        pwField.send_keys(password)
        del password
        driver.find_element(By.ID, "idSIButton9").click()
        time.sleep(2)

        # check to see if we're at the right page, if so, break out of loop
        driver.find_element(By.ID, "idDiv_SAOTCAS_Title")
        break
        
    except:
        # If authentication page does not show up, try pw again
        print("The password you've entered is incorrect.")
        driver.find_element(By.ID, "i0118").clear()
        
# assuming 2FA enabled (required), prompt user to accept request
print("Please authenticate the login through the Authenticator")
print("When you are finished, press enter...")
input()
print("logging you in...")
driver.find_element(By.ID, "idSIButton9").click()
time.sleep(2)

print("You are now logged in.\nFinding your Fall courses...")

###############

# Now, navigate through SOLUS to find Fall/Winter semester lecture times
driver.get(
    "https://saself.ps.queensu.ca/psc/saself_21/EMPLOYEE/SA/c/SSR_STUDENT_FL.SSR_MD_SP_FL.GBL"
)
time.sleep(3)
driver.find_element(By.ID, "PS_SCHEDULE_L_FL$3").click()
time.sleep(3)
driver.find_element(By.ID, "GRID_TERM_SRC5$0_row_0").click()
print("Fall courses found:")
time.sleep(10)


# btn = driver.find_element(By.ID, "GRID_TERM_SRC$0_row_0")
# manageClasses = btn.click()
# print(manageClasses)


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
