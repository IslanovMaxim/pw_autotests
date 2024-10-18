import os

class Constants:
    try:
        login = os.getenv('AUTH_LOGIN')
        code = os.getenv('AUTH_CODE')
        drug_name = os.getenv('DRUG_NAME')
        drug_name_less_50 = os.getenv('DRUG_NAME_LESS_50')
    except KeyError:
        print("LOGIN OR PW WASN'T FOUND")