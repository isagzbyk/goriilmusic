from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

BOT_TOKEN = getenv("BOT_TOKEN", None)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "180"))

OWNER_ID = int(getenv("OWNER_ID"))

PING_IMG = getenv("PING_IMG", "https://telegra.ph/goril-04-21.jpg")
START_IMG = getenv("START_IMG", "https://telegra.ph/goril-04-21.jpg")

SESSION = getenv("SESSION", None)
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/dertkonagi")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/muasdkasdjadjmajdmaowd")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "").split()))

MUSIC_BOT_NAME = getenv("MUSIC_BOT_NAME", "✨𝗚𝗼𝗿𝗶𝗹 𝗠𝘂𝘇𝗶𝗸✨")  

FAILED = "https://telegra.ph/goril-04-21.jpg"
