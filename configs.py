from os import path, getenv
import os, time 

class Config:
    API_ID = int(getenv("API_ID", "21418386"))
    API_HASH = getenv("API_HASH", "aeac46b1d123e82fe6dcb43b6a26cfae")
    BOT_TOKEN = getenv("BOT_TOKEN", "7746109405:AAEt5sIJPunBLSw7Cq4CpwMtHLooJqrF2Ks")
 
    ADMIN = list(map(int, getenv("ADMIN", "5496176944").split()))
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002440247365"))
    FORCE_SUB = int(getenv("FORCE_SUB", "Aero_Bots_tm"))

    # database configs
    DB_URL = os.environ.get("DB_URL", "mongodb+srv://TaktAsahina99:TaktAsahina99@cluster0.iq3cx2j.mongodb.net/?retryWrites=true&w=majority")
    DB_NAME = os.environ.get("DB_NAME", "Shanbot")
    
    #web response 
    WEBHOOK = bool(os.environ.get("WEBHOOK", True))
    BOT_UPTIME  = time.time()
    PORT = os.environ.get("PORT", "8080")

rkn1 = Config()
