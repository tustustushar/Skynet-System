import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
que = {}
admins = {}

    API_ID_KEY = int(getenv("API_ID"))
    API_HASH_KEY = getenv("API_HASH") 
    STRING_SESSION = getenv("SESSION_NAME", "session")
    Skynet = ""
    ENFORCERS = ""
    Skynet_logs = ""
    Skynet_approved_logs = ""
    GBAN_MSG_LOGS = ""
