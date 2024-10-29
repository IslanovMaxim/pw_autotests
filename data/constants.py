import os

class Constants:
    try:
        login_test = os.getenv('AUTH_LOGIN')
        #login_own = os.getenv('AUTH_LOGIN_OWN') #возможно пригодится
        code = os.getenv('AUTH_CODE')
        drug_name = os.getenv('DRUG_NAME')
        drug_name_less_50 = os.getenv('DRUG_NAME_LESS_50')
        drug_name_set_2_1 = os.getenv('DRUG_NAME_SET_2_1')
        drug_name_set_discount_on_second = os.getenv('DRUG_NAME_SET_DISCOUNT_ON_SECOND')
        #path_for_screenshot = os.getenv('PATH')
    except KeyError:
        print("LOGIN OR PW WASN'T FOUND")