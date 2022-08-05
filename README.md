# calendar-helper
This script aims to automate some repetitive Google Calendar tasks that students need to complete before starting their school years. It is using the Google Calendar API.

Disclaimer: This is a very-specific use-case, and was built with my own personal use in mind. The application assumes the user is a Queen's University student, looking to add courses to a personal (primary) Google Calendar. This script acts as a proof of concept for an app idea and still requires loads of error-handling, edge-cases converage, and will not be of much use in its current state. I am working on broadening its target audience by keeping Selenium requests as general as possible, and potentially implementing a feature to detect the amount of enrolled courses automatically, as well as a feature to also create events for multiple other course types (labs, tutorials, etc...).

Check out the latest PR for sub-issues currently getting fixed.

## Getting Started
- Create Python virtual environment: `python -m venv myPythonEnvName`
- Activate the environment: `source myPythonEnvName/Scripts/activate`
- Install the required dependencies: `pip install -r requirements.txt`
- Create a OAuth 2.0 Client ID**: https://developers.google.com/identity/protocols/oauth2 and add the JSON data to `app/static/credentials.json`
- Run the application: `cd app && python main.py`

** The Client ID must have an Authorized redirect URI of `http://localhost:8080/`
