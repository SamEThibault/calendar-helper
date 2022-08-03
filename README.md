# calendar-helper
This script aims to automate some repetitive Google Calendar tasks that students need to complete before starting their school years. It is using the Google Calendar API.

## Getting Started
- Create Python virtual environment: `python3 -m venv myPythonEnvName`
- Activate the environment: `source myPythonEnvName/Scripts/activate`
- Install the required dependencies: `pip install -r requirements.txt`
- Create a OAuth 2.0 Client ID**: https://developers.google.com/identity/protocols/oauth2 and add the JSON data to `app/static/credentials.json`
- Run the application: `cd app && python main.py`

** The Client ID must have an Authorized redirect URI of `http://localhost:8080/`
