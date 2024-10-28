import os

class Constants:
    try:
        login = os.getenv('AUTH_LOGIN')
        code = os.getenv('AUTH_CODE')
        drug_name = os.getenv('DRUG_NAME')
        drug_name_less_50 = os.getenv('DRUG_NAME_LESS_50')
        drug_name_set_2_1 = os.getenv('DRUG_NAME_SET_2_1')
        drug_name_set_discount_on_second = os.getenv('DRUG_NAME_SET_DISCOUNT_ON_SECOND')
    except KeyError:
        print("LOGIN OR PW WASN'T FOUND")