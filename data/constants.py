import os

class Constants:
    try:
        login = os.getenv('AUTH_LOGIN')
        code = os.getenv('AUTH_CODE')
    except KeyError:
        print("LOGIN OR PW WASN'T FOUND")