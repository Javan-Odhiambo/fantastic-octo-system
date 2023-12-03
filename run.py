import random
import requests
import time
from requests.exceptions import ConnectionError
from termcolor import cprint

from constants import LOGIN_DATA, LOGIN_HEADER, LOGIN_URL, MAIN_PAGE_URL, POST_SETTINGS_URL, SETTINGS_HEADER, settings_data
from variables import MIN_RANGE, MAX_RANGE, NO_OF_TRIALS, SECONDS_TO_WAIT_BEFORE_NEXT_TEST, NORMAL_USERNAME

if not NORMAL_USERNAME:
    print('NORMAL USERNAME MUST BE SET')
    exit(1)
else: 
    NORMAL_USERNAME = str(NORMAL_USERNAME) + "@gpon"

def check_network(username):
    try:
        requests.get('https://www.google.com')
        cprint(f"{username} WORKS", 'green')
        with open('Working.txt', 'a') as file:
            file.write(f"{username}\n")

    except ConnectionError as e:
        cprint(f"{username} DOES NOT WORK", 'red')

def set_username(session, username, cookiejar):
    main_page = session.get(MAIN_PAGE_URL, cookies=cookiejar)
    main_page_token = main_page.text[1804:1852] # TODO: Change this to use regex in order to avoid future bugs 

    data = settings_data
    data.update({'y.Username': username})
    data.update({'x.X_HW_Token': main_page_token})

    settings_response = session.post(POST_SETTINGS_URL, headers=SETTINGS_HEADER, cookies=cookiejar, data=data)
    print("TESTING", username)
    main_page = session.get('https://192.168.100.1/index.asp', cookies=cookiejar)



# Use 'with' to ensure the session context is closed after use.
with requests.Session() as session:
    session.verify = False
    login_response = requests.post(LOGIN_URL, headers=LOGIN_HEADER, cookies={'Cookie': 'body:Language:english:id=-1'}, data=LOGIN_DATA, verify=False)

    cookiejar = requests.cookies.RequestsCookieJar()
    cookiejar.set('Cookie', login_response.headers.get("Set-Cookie"))


    for i in range(NO_OF_TRIALS):
        # Set the normal username 1st
        set_username(session, NORMAL_USERNAME, cookiejar)
        time.sleep(10)

        # Generate new username and set it.
        number = random.randint(MIN_RANGE, MAX_RANGE)
        username = str(number) + '@gpon'
        set_username(session, username, cookiejar)
        time.sleep(SECONDS_TO_WAIT_BEFORE_NEXT_TEST)

        # Check for an internet connection.
        check_network(username)
