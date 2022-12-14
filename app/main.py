# Script used to copy over SOLUS (Queen's University Student Center)
# course schedule information over to a personal Google Calendar.

import time
import getpass
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

from calendarAPI import callAPI

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
        driver.find_element(By.ID, "usernameError")
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

# Now, navigate through SOLUS to find Fall semester lecture times
driver.get(
    "https://saself.ps.queensu.ca/psc/saself_21/EMPLOYEE/SA/c/SSR_STUDENT_FL.SSR_MD_SP_FL.GBL"
)
time.sleep(3)
driver.find_element(By.ID, "PS_SCHEDULE_L_FL$3").click()
time.sleep(3)
driver.find_element(By.ID, "GRID_TERM_SRC5$0_row_0").click()
print("Fall courses found:")
time.sleep(3)

# this is a blueprint for a single Google API event request.
class Event:
    # event name, specific start day, both start and end dates, and start and end times must be provided
    def __init__(self, name, day, startEnd, times):
        self.name = name                                    # this is just the course name
        self.day = day.split(" ")[1].lower()                # lowercase start day (monday, tuesday...)
        self.startEnd = startEnd.split(" - ")               # start and end dates ["2020/09/05", "..."]
        startDate = self.startEnd[0].replace("/", "-")      # start/end date ISO format: "2020-09-05"
        endDate = self.startEnd[1].replace("/", "-")        
        startTime = times.split(" ")[1][:-2]                # start/end time (no AM/PM): "11:00" 
        endTime = times.split(" ")[3][:-2]                  

        # get the start and end AM/PM specification to ensure correct ISO formatting 
        startAmPm = times.split(" ")[1][len(startTime):]
        endAmPm = times.split(" ")[3][len(endTime):]

        # the adjusted variables are used in the final formatting step
        adjustedStartTime = startTime  
        adjustedEndTime = endTime

        # if the start/end time is in afternoon and is not 12, add 12 hours to it and update adjusted variables
        if startAmPm == "PM" and startTime.split(":")[0] != "12": 
            originalHour = startTime.split(":")[0]
            newHour = str(int(originalHour) + 12)
            adjustedStartTime = startTime.replace(originalHour, newHour)
        if endAmPm == "PM" and endTime.split(":")[0] != "12":
            originalHour = endTime.split(":")[0]
            newHour = str(int(originalHour) + 12)
            adjustedEndTime = endTime.replace(originalHour, newHour)

        # need to adjust the startDate with the day of week for the course
        startDay = startDate.split("-")[2]  # get the day
        # offset determined by a start day of Tuesday, as per a usual academic calendar
        if self.day == "monday":
            dayOffset = 6
        elif self.day == "tuesday":
            dayOffset = 0
        elif self.day == "wednesday":
            dayOffset = 1
        elif self.day == "thursday":
            dayOffset = 2
        elif self.day == "friday":
            dayOffset = 3

        # add offset and update original date
        startDay = str(int(startDay) + dayOffset)
        adjustedStartDate = startDate.replace(startDate.split("-")[2], startDay)

        # ISO Date Format needed for API request (EST)
        self.startDateTime = adjustedStartDate + "T" + adjustedStartTime + ":00-04:00"
        self.endDateTime = adjustedStartDate + "T" + adjustedEndTime + ":00-04:00"

    # print out object fields
    def printCourse(self):
        print("-------------- Course Information ------------------")
        print("Name: " + self.name)
        print("Start Day: " + self.day)
        print("Start Date and Time: " + self.startDateTime)
        print("End Date and Time: " + self.endDateTime)
        print("-------------- END ------------------")


# testing the first course and first lecture time
name = driver.find_element(By.ID, "DERIVED_SSR_FL_SSR_SCRTAB_DTLS$0").text
day = driver.find_element(By.ID, "DERIVED_SSR_FL_SSR_DAYS1$0").text
startEnd = driver.find_element(By.ID, "DERIVED_SSR_FL_SSR_ST_END_DT1$0").text
times = driver.find_element(By.ID, "DERIVED_SSR_FL_SSR_DAYSTIMES1$0").text
course = Event(name, day, startEnd, times)
course.printCourse()
callAPI(course)

# second lecture time
day = driver.find_element(By.ID, "DERIVED_SSR_FL_SSR_DAYS2$0").text
startEnd = driver.find_element(By.ID, "DERIVED_SSR_FL_SSR_ST_END_DT2$0").text
times = driver.find_element(By.ID, "DERIVED_SSR_FL_SSR_DAYSTIMES2$0").text
course = Event(name, day, startEnd, times)
course.printCourse()
callAPI(course)
exit()
