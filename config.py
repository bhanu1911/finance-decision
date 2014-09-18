
class Config(object):
    def __init__(self):
        pass


allowed_countries = ['United Kingdom']
age_limit_bottom = 18
age_limit_top = 65

status_description = {0: 'reject', 1: 'accept'}

http_headers = ['Expires: 0', 'Cache-Control: no-cache', 'Content-Type: text/json']

input_vars_mapping = {'first_name': str, 'surname': str, 'age': int, 'address': str, 'country': str, 'account': int};

