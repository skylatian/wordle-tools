from runner import runnerd
from config import *


for users in User.list:
    COOKIE = users.cookie
    wsID = users.wsID
    runnerd(users)