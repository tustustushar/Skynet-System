 import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
que = {}
admins = {}


   # REQUIRED
    API_ID_KEY = int(getenv("API_ID_KEY"))
    API_HASH_KEY = "54ae863723266217fa10714b1833e8f7"  
    STRING_SESSION = "1AZWarzQBu0l8Up9_Coa81-b24IAD-mQVAVVkoOPQXI-hyoqQisNr4092W5626mBTDYOW0sczHKv-idbgQ8nRtvkFY6ZF-R_W__q2m40ZCmW7KLBlc7zs71caQxP7E9Pt11e36GtVRmw3luubSaPOHP9_NVk52WJ_fLud0FL6ZjX9Z2EA68GJ1ZRSNCdEeuAVgosetDICbvtAhYe1uQOketWVYqjsukAmXb-ITWdN8ICNpzLofif5elkVSqp5Lku8jK4oJ5T0QJsEtdC0kqOLwLgOLv-WI3agssEQNsguA8rsFgV5dMHCTFlLZQErDzQG7OaEZ5ULckPUCx2jV7eBVy7Vus3hueM="
    Sibyl = ""
    ENFORCERS = "1962664022"
    Sibyl_logs = "-1001675046141"
    Sibyl_approved_logs = "-1001675046141"
    GBAN_MSG_LOGS = "-1001675046141"
