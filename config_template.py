## Times Credentials ##
cookie1 = ""
cookie2 = ""

DATE_FORMAT = '%Y-%m-%d' # date format for the sheet (ex 2023-06-25)

## Sheets Config ##
gspread_credentials = {
  "type": "service_account",
  "project_id": "",
  "private_key_id": "",
  "private_key": "",
  "client_email": "",
  "client_id": "",
  "auth_uri": "",
  "token_uri": "",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "",
  "universe_domain": "googleapis.com"
}

sheetkey =  ""
worksheetID = 0 #number

class User:
    list = [] # https://medium.com/@morevinyl/cool-python-track-all-instances-of-a-class-easily-even-2610368d7896
    def __init__(self, cookie, wsID):
        self.wsID = wsID
        self.cookie = cookie
        self.worksheet = None
        self.sheetkey = sheetkey
        self.gsc = gspread_credentials
        self.date_format = DATE_FORMAT
        User.list.append(self)

user1 = User(cookie1,685824496)
user2 = User(cookie2,92270942)