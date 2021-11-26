import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME", "Hinata")
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
OWNER_NAME = getenv("OWNER_NAME", "Amaterasu91")
ALIVE_NAME = getenv("ALIVE_NAME", "Levina")
BOT_USERNAME = getenv("BOT_USERNAME", "HinataSuperbot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "cleo_invida")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "WeebsGC")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "weebsgcstorage")
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://images.alphacoders.com/603/603505.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/levina-lab/video-stream")
IMG_1 = getenv("IMG_1", "https://images3.alphacoders.com/687/687231.jpg")
IMG_2 = getenv("IMG_2", "https://images7.alphacoders.com/356/356127.jpg")
IMG_3 = getenv("IMG_3", "https://images4.alphacoders.com/245/245426.jpg")
