import asyncio
import time
import os
import logging
from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.errors import FloodWait, RPCError

# ================= LOGGING =================
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# ================= CONFIG =================
API_ID = int(os.environ.get("API_ID", 12345678))
API_HASH = os.environ.get("API_HASH", "YOUR_API_HASH")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "YOUR_BOT_TOKEN")
OWNER_ID = int(os.environ.get("OWNER_ID", 123456789))

# ==========================================

# Fix for Python 3.14 - Create event loop policy
try:
    asyncio.get_event_loop()
except RuntimeError:
    asyncio.set_event_loop(asyncio.new_event_loop())

app = Client(
    "FastBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    workers=100,
    parse_mode="html"
)

# ===== SUDO USERS =====
sudo_users = {OWNER_ID}

# ===== RAID SYSTEM =====
raid_tasks = {}

# ===== CUSTOM LINES =====
custom_lines = [
    
    "🔥 teri mummy ki chut!",
    "⚡ bahen k lode teri dadi ki black hairy pussy",
    "🚀 teri mummy ko ulta ltkakr taangduga aur uski chut maruga!",
    "✨ bsdk teri mummy teri dadi sb randi ki bachi h",
    "bahenklodo tumhari maa meri setting",
    "bahenklodo tumhari maa meri setting",
    "teri mummy randi h randi bsdk",
    "teri mummy ki pussy m scooter dalduga",
    "teri mummy ki pussy me cum krduga randi maa k bache",
    "tera khandan hi randiyo ka h",
    "teri dadi ki pussy me mera lund",
    "teri mummy ko chodkr ulta ltkakr uske muh me loda deduga",
    "teri mummy ko deepthroat deduga madarchod k bache",
    "✌️✌️tera papa bhi randi ki aulad h bsdk",
    "teri mummy ko yoga sikhaduga aur usko different styles me choduga",
    "tera papa hu mai teri mummy ka bf jis s vo chudkr gyi thi",
    "teri maa ki pussy me scooter dalduga bahen k lode🤣🤣",
    "teri maa ki chut me bihari gutka khakr thuk kr chale gye the🔥🔥",
    "💀💀teri maa ka bosda randi k beej",
    "✌️✌️teri maa ki chut me 2finger dekr uska paani nikalduga0",
    "🔥🔥teri maa k muh me gass pipe dekr uski gaand me fire lgakr tere baap ki gaand jalauga",
    "😂😍😍teri randi maa ko chodkr maine gb road pr beach diya tha",
    "🙌🙌teri mummy k haath divar pr lgvadiye the 10bihariyo ne",
    "𝑻𝑬𝑹𝑰 𝑴𝑨𝑨 𝑲𝑶 𝑻𝑶𝑹𝑹𝑬𝑵𝑻 𝑩𝑨𝑵𝑨𝑲𝑬 𝑺𝑬𝑬𝑫 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑴𝑨𝑨 𝑲𝑬 𝑩𝑯𝑶𝑺𝑫𝑬 𝑴𝑬 𝑭𝑰𝑹𝑬𝑾𝑨𝑳𝑳 𝑳𝑨𝑮𝑨 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑴𝑨𝑨 𝑲𝑰 𝑪𝑯𝑼𝑻 𝑴𝑬 𝑺𝑺𝑫 𝑩𝑶𝑶𝑻 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑴𝑨𝑨 𝑩𝑯𝑶𝑺𝑫𝑬 𝑴𝑬 𝑵𝑭𝑻 𝑴𝑰𝑵𝑻 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑴𝑨𝑨 𝑲𝑨 𝑳𝑼𝑵𝑫 𝑶𝑳𝑿 𝑷𝑬 𝑩𝑬𝑪𝑯 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑴𝑨𝑨 𝑲𝑰 𝑮𝑨𝑨𝑵𝑫 𝑴𝑬 𝑸𝑹 𝑪𝑶𝑫𝑬 𝑪𝑯𝑰𝑷𝑲𝑨 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑴𝑨𝑨 𝑲𝑨 𝑶𝑵𝑳𝒀𝑭𝑨𝑵𝑺 𝑳𝑰𝑽𝑬 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑳𝑨𝑮𝑬 𝑲𝑶 𝑻𝑶𝑹𝑹𝑬𝑵𝑻 𝑩𝑨𝑵𝑨𝑲𝑬 𝑺𝑬𝑬𝑫 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑳𝑨𝑮𝑬 𝑲𝑬 𝑩𝑯𝑶𝑺𝑫𝑬 𝑴𝑬 𝑭𝑰𝑹𝑬𝑾𝑨𝑳𝑳 𝑳𝑨𝑮𝑨 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑳𝑨𝑮𝑬 𝑲𝑰 𝑪𝑯𝑼𝑻 𝑴𝑬 𝑺𝑺𝑫 𝑩𝑶𝑶𝑻 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑩𝑬𝑯𝑬𝑵 𝑲𝑶 𝑻𝑶𝑹𝑹𝑬𝑵𝑻 𝑩𝑨𝑵𝑨𝑲𝑬 𝑺𝑬𝑬𝑫 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑩𝑬𝑯𝑬𝑵 𝑲𝑬 𝑩𝑯𝑶𝑺𝑫𝑬 𝑴𝑬 𝑭𝑰𝑹𝑬𝑾𝑨𝑳𝑳 𝑳𝑨𝑮𝑨 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑩𝑬𝑯𝑬𝑵 𝑲𝑰 𝑪𝑯𝑼𝑻 𝑴𝑬 𝑺𝑺𝑫 𝑩𝑶𝑶𝑻 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑩𝑬𝑯𝑬𝑵 𝑲𝑨 𝑳𝑼𝑵𝑫 𝑶𝑳𝑿 𝑷𝑬 𝑩𝑬𝑪𝑯 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑩𝑬𝑯𝑬𝑵 𝑲𝑰 𝑮𝑨𝑨𝑵𝑫 𝑴𝑬 𝑸𝑹 𝑪𝑶𝑫𝑬 𝑪𝑯𝑰𝑷𝑲𝑨 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑩𝑬𝑯𝑬𝑵 𝑲𝑨 𝑩𝑯𝑺𝑶𝑫𝑨 𝑵𝑭𝑻 𝑴𝑬 𝑴𝑰𝑵𝑻 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑩𝑬𝑯𝑬𝑵 𝑲𝑨 𝑶𝑵𝑳𝒀𝑭𝑨𝑵𝑺 𝑳𝑰𝑽𝑬 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑩𝑬𝑯𝑬𝑵 𝑲𝑶 𝒁𝑰𝑷 𝑭𝑰𝑳𝑬 𝑴𝑬 𝑪𝑶𝑴𝑷𝑹𝑬𝑺𝑺 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑩𝑬𝑯𝑬𝑵 𝑲𝑬 𝑩𝑯𝑶𝑺𝑫𝑬 𝑴𝑬 𝑷𝒀𝑻𝑯𝑶𝑵 𝑹𝑼𝑵 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑩𝑬𝑯𝑬𝑵 𝑲𝑬 𝑳𝑶𝑫𝑬 𝑲𝑶 𝑨𝑰𝑹𝑫𝑹𝑶𝑷 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑩𝑬𝑯𝑬𝑵 𝑲𝑶 𝑩𝑨𝑹𝑪𝑶𝑫𝑬 𝑳𝑨𝑮𝑨 𝑲𝑬 𝑺𝑪𝑨𝑵 𝑲𝑨𝑹𝑾𝑨𝑨 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑩𝑬𝑯𝑬𝑵 𝑲𝑶 𝑨𝑰 𝑻𝑶𝑶𝑳 𝑺𝑬 𝑼𝑷𝑺𝑪𝑨𝑳𝑬 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑩𝑨𝑨𝑷 𝑲𝑶 𝑻𝑶𝑹𝑹𝑬𝑵𝑻 𝑩𝑨𝑵𝑨𝑲𝑬 𝑺𝑬𝑬𝑫 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑩𝑨𝑨𝑷 𝑲𝑬 𝑩𝑯𝑶𝑺𝑫𝑬 𝑴𝑬 𝑭𝑰𝑹𝑬𝑾𝑨𝑳𝑳 𝑳𝑨𝑮𝑨 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑩𝑨𝑨𝑷 𝑲𝑰 𝑪𝑯𝑼𝑻 𝑴𝑬 𝑺𝑺𝑫 𝑩𝑶𝑶𝑻 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑩𝑨𝑨𝑷 𝑲𝑨 𝑳𝑼𝑵𝑫 𝑶𝑳𝑿 𝑷𝑬 𝑩𝑬𝑪𝑯 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑩𝑨𝑨𝑷 𝑲𝑰 𝑮𝑨𝑨𝑵𝑫 𝑴𝑬 𝑸𝑹 𝑪𝑶𝑫𝑬 𝑪𝑯𝑰𝑷𝑲𝑨 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑩𝑨𝑨𝑷 𝑲𝑨 𝑩𝑯𝑺𝑶𝑫𝑨 𝑵𝑭𝑻 𝑴𝑬 𝑴𝑰𝑵𝑻 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑩𝑨𝑨𝑷 𝑲𝑨 𝑶𝑵𝑳𝒀𝑭𝑨𝑵𝑺 𝑳𝑰𝑽𝑬 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑩𝑨𝑨𝑷 𝑲𝑶 𝒁𝑰𝑷 𝑭𝑰𝑳𝑬 𝑴𝑬 𝑪𝑶𝑴𝑷𝑹𝑬𝑺𝑺 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑩𝑨𝑨𝑷 𝑲𝑬 𝑩𝑯𝑶𝑺𝑫𝑬 𝑴𝑬 𝑷𝒀𝑻𝑯𝑶𝑵 𝑹𝑼𝑵 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑩𝑨𝑨𝑷 𝑲𝑬 𝑳𝑶𝑫𝑬 𝑲𝑶 𝑨𝑰𝑹𝑫𝑹𝑶𝑷 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑩𝑨𝑨𝑷 𝑲𝑶 𝑩𝑨𝑹𝑪𝑶𝑫𝑬 𝑳𝑨𝑮𝑨 𝑲𝑬 𝑺𝑪𝑨𝑵 𝑲𝑨𝑹𝑾𝑨𝑨 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑩𝑨𝑨𝑷 𝑲𝑶 𝑨𝑰 𝑻𝑶𝑶𝑳 𝑺𝑬 𝑼𝑷𝑺𝑪𝑨𝑳𝑬 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑭𝑨𝑴𝑰𝑳𝒀 𝑲𝑶 𝑻𝑶𝑹𝑹𝑬𝑵𝑻 𝑩𝑨𝑵𝑨𝑲𝑬 𝑺𝑬𝑬𝑫 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑭𝑨𝑴𝑰𝑳𝒀 𝑲𝑬 𝑩𝑯𝑶𝑺𝑫𝑬 𝑴𝑬 𝑭𝑰𝑹𝑬𝑾𝑨𝑳𝑳 𝑳𝑨𝑮𝑨 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑭𝑨𝑴𝑰𝑳𝒀 𝑲𝑰 𝑪𝑯𝑼𝑻 𝑴𝑬 𝑺𝑺𝑫 𝑩𝑶𝑶𝑻 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑭𝑨𝑴𝑰𝑳𝒀 𝑲𝑨 𝑳𝑼𝑵𝑫 𝑶𝑳𝑿 𝑷𝑬 𝑩𝑬𝑪𝑯 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑭𝑨𝑴𝑰𝑳𝒀 𝑲𝑰 𝑮𝑨𝑨𝑵𝑫 𝑴𝑬 𝑸𝑹 𝑪𝑶𝑫𝑬 𝑪𝑯𝑰𝑷𝑲𝑨 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑭𝑨𝑴𝑰𝑳𝒀 𝑲𝑨 𝑩𝑯𝑺𝑶𝑫𝑨 𝑵𝑭𝑻 𝑴𝑬 𝑴𝑰𝑵𝑻 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑭𝑨𝑴𝑰𝑳𝒀 𝑲𝑨 𝑶𝑵𝑳𝒀𝑭𝑨𝑵𝑺 𝑳𝑰𝑽𝑬 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑭𝑨𝑴𝑰𝑳𝒀 𝑲𝑶 𝒁𝑰𝑷 𝑭𝑰𝑳𝑬 𝑴𝑬 𝑪𝑶𝑴𝑷𝑹𝑬𝑺𝑺 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑭𝑨𝑴𝑰𝑳𝒀 𝑲𝑬 𝑩𝑯𝑶𝑺𝑫𝑬 𝑴𝑬 𝑷𝒀𝑻𝑯𝑶𝑵 𝑹𝑼𝑵 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑭𝑨𝑴𝑰𝑳𝒀 𝑲𝑬 𝑳𝑶𝑫𝑬 𝑲𝑶 𝑨𝑰𝑹𝑫𝑹𝑶𝑷 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑭𝑨𝑴𝑰𝑳𝒀 𝑲𝑶 𝑩𝑨𝑹𝑪𝑶𝑫𝑬 𝑳𝑨𝑮𝑨 𝑲𝑬 𝑺𝑪𝑨𝑵 𝑲𝑨𝑹𝑾𝑨𝑨 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑭𝑨𝑴𝑰𝑳𝒀 𝑲𝑶 𝑨𝑰 𝑻𝑶𝑶𝑳 𝑺𝑬 𝑼𝑷𝑺𝑪𝑨𝑳𝑬 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑲𝑼𝑻𝑻𝑬 𝑲𝑶 𝑻𝑶𝑹𝑹𝑬𝑵𝑻 𝑩𝑨𝑵𝑨𝑲𝑬 𝑺𝑬𝑬𝑫 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑲𝑼𝑻𝑻𝑬 𝑲𝑬 𝑩𝑯𝑶𝑺𝑫𝑬 𝑴𝑬 𝑭𝑰𝑹𝑬𝑾𝑨𝑳𝑳 𝑳𝑨𝑮𝑨 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑲𝑼𝑻𝑻𝑬 𝑲𝑰 𝑪𝑯𝑼𝑻 𝑴𝑬 𝑺𝑺𝑫 𝑩𝑶𝑶𝑻 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑲𝑼𝑻𝑻𝑬 𝑲𝑨 𝑳𝑼𝑵𝑫 𝑶𝑳𝑿 𝑷𝑬 𝑩𝑬𝑪𝑯 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑲𝑼𝑻𝑻𝑬 𝑲𝑰 𝑮𝑨𝑨𝑵𝑫 𝑴𝑬 𝑸𝑹 𝑪𝑶𝑫𝑬 𝑪𝑯𝑰𝑷𝑲𝑨 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑲𝑼𝑻𝑻𝑬 𝑲𝑨 𝑩𝑯𝑺𝑶𝑫𝑨 𝑵𝑭𝑻 𝑴𝑬 𝑴𝑰𝑵𝑻 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑲𝑼𝑻𝑻𝑬 𝑲𝑨 𝑶𝑵𝑳𝒀𝑭𝑨𝑵𝑺 𝑳𝑰𝑽𝑬 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑲𝑼𝑻𝑻𝑬 𝑲𝑶 𝒁𝑰𝑷 𝑭𝑰𝑳𝑬 𝑴𝑬 𝑪𝑶𝑴𝑷𝑹𝑬𝑺𝑺 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑲𝑼𝑻𝑻𝑬 𝑲𝑬 𝑩𝑯𝑶𝑺𝑫𝑬 𝑴𝑬 𝑷𝒀𝑻𝑯𝑶𝑵 𝑹𝑼𝑵 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑲𝑼𝑻𝑻𝑬 𝑲𝑬 𝑳𝑶𝑫𝑬 𝑲𝑶 𝑨𝑰𝑹𝑫𝑹𝑶𝑷 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑲𝑼𝑻𝑻𝑬 𝑲𝑶 𝑩𝑨𝑹𝑪𝑶𝑫𝑬 𝑳𝑨𝑮𝑨 𝑲𝑬 𝑺𝑪𝑨𝑵 𝑲𝑨𝑹𝑾𝑨𝑨 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑲𝑼𝑻𝑻𝑬 𝑲𝑶 𝑨𝑰 𝑻𝑶𝑶𝑳 𝑺𝑬 𝑼𝑷𝑺𝑪𝑨𝑳𝑬 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑨𝑼𝑲𝑨𝑨𝑻 𝑲𝑶 𝑻𝑶𝑹𝑹𝑬𝑵𝑻 𝑩𝑨𝑵𝑨𝑲𝑬 𝑺𝑬𝑬𝑫 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑨𝑼𝑲𝑨𝑨𝑻 𝑲𝑬 𝑩𝑯𝑶𝑺𝑫𝑬 𝑴𝑬 𝑭𝑰𝑹𝑬𝑾𝑨𝑳𝑳 𝑳𝑨𝑮𝑨 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑨𝑼𝑲𝑨𝑨𝑻 𝑲𝑰 𝑪𝑯𝑼𝑻 𝑴𝑬 𝑺𝑺𝑫 𝑩𝑶𝑶𝑻 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑨𝑼𝑲𝑨𝑨𝑻 𝑲𝑨 𝑳𝑼𝑵𝑫 𝑶𝑳𝑿 𝑷𝑬 𝑩𝑬𝑪𝑯 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑨𝑼𝑲𝑨𝑨𝑻 𝑲𝑰 𝑮𝑨𝑨𝑵𝑫 𝑴𝑬 𝑸𝑹 𝑪𝑶𝑫𝑬 𝑪𝑯𝑰𝑷𝑲𝑨 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑨𝑼𝑲𝑨𝑨𝑻 𝑲𝑨 𝑩𝑯𝑺𝑶𝑫𝑨 𝑵𝑭𝑻 𝑴𝑬 𝑴𝑰𝑵𝑻 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑨𝑼𝑲𝑨𝑨𝑻 𝑲𝑨 𝑶𝑵𝑳𝒀𝑭𝑨𝑵𝑺 𝑳𝑰𝑽𝑬 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑨𝑼𝑲𝑨𝑨𝑻 𝑲𝑶 𝒁𝑰𝑷 𝑭𝑰𝑳𝑬 𝑴𝑬 𝑪𝑶𝑴𝑷𝑹𝑬𝑺𝑺 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑨𝑼𝑲𝑨𝑨𝑻 𝑲𝑬 𝑩𝑯𝑶𝑺𝑫𝑬 𝑴𝑬 𝑷𝒀𝑻𝑯𝑶𝑵 𝑹𝑼𝑵 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑨𝑼𝑲𝑨𝑨𝑻 𝑲𝑬 𝑳𝑶𝑫𝑬 𝑲𝑶 𝑨𝑰𝑹𝑫𝑹𝑶𝑷 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑨𝑼𝑲𝑨𝑨𝑻 𝑲𝑶 𝑩𝑨𝑹𝑪𝑶𝑫𝑬 𝑳𝑨𝑮𝑨 𝑲𝑬 𝑺𝑪𝑨𝑵 𝑲𝑨𝑹𝑾𝑨𝑨 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑨𝑼𝑲𝑨𝑨𝑻 𝑲𝑶 𝑨𝑰 𝑻𝑶𝑶𝑳 𝑺𝑬 𝑼𝑷𝑺𝑪𝑨𝑳𝑬 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑴𝑼𝑴𝑴𝒀 𝑲𝑶 𝑻𝑶𝑹𝑹𝑬𝑵𝑻 𝑩𝑨𝑵𝑨𝑲𝑬 𝑺𝑬𝑬𝑫 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑴𝑼𝑴𝑴𝒀 𝑲𝑬 𝑩𝑯𝑶𝑺𝑫𝑬 𝑴𝑬 𝑭𝑰𝑹𝑬𝑾𝑨𝑳𝑳 𝑳𝑨𝑮𝑨 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑴𝑼𝑴𝑴𝒀 𝑲𝑰 𝑪𝑯𝑼𝑻 𝑴𝑬 𝑺𝑺𝑫 𝑩𝑶𝑶𝑻 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑴𝑼𝑴𝑴𝒀 𝑲𝑨 𝑳𝑼𝑵𝑫 𝑶𝑳𝑿 𝑷𝑬 𝑩𝑬𝑪𝑯 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑴𝑼𝑴𝑴𝒀 𝑲𝑰 𝑮𝑨𝑨𝑵𝑫 𝑴𝑬 𝑸𝑹 𝑪𝑶𝑫𝑬 𝑪𝑯𝑰𝑷𝑲𝑨 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑴𝑼𝑴𝑴𝒀 𝑲𝑨 𝑩𝑯𝑺𝑶𝑫𝑨 𝑵𝑭𝑻 𝑴𝑬 𝑴𝑰𝑵𝑻 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑴𝑼𝑴𝑴𝒀 𝑲𝑨 𝑶𝑵𝑳𝒀𝑭𝑨𝑵𝑺 𝑳𝑰𝑽𝑬 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑴𝑼𝑴𝑴𝒀 𝑲𝑶 𝒁𝑰𝑷 𝑭𝑰𝑳𝑬 𝑴𝑬 𝑪𝑶𝑴𝑷𝑹𝑬𝑺𝑺 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑴𝑼𝑴𝑴𝒀 𝑲𝑬 𝑩𝑯𝑶𝑺𝑫𝑬 𝑴𝑬 𝑷𝒀𝑻𝑯𝑶𝑵 𝑹𝑼𝑵 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑴𝑼𝑴𝑴𝒀 𝑲𝑬 𝑳𝑶𝑫𝑬 𝑲𝑶 𝑨𝑰𝑹𝑫𝑹𝑶𝑷 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑴𝑼𝑴𝑴𝒀 𝑲𝑶 𝑩𝑨𝑹𝑪𝑶𝑫𝑬 𝑳𝑨𝑮𝑨 𝑲𝑬 𝑺𝑪𝑨𝑵 𝑲𝑨𝑹𝑾𝑨𝑨 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑴𝑼𝑴𝑴𝒀 𝑲𝑶 𝑨𝑰 𝑻𝑶𝑶𝑳 𝑺𝑬 𝑼𝑷𝑺𝑪𝑨𝑳𝑬 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑫𝑨𝑫𝑨 𝑲𝑶 𝑻𝑶𝑹𝑹𝑬𝑵𝑻 𝑩𝑨𝑵𝑨𝑲𝑬 𝑺𝑬𝑬𝑫 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑫𝑨𝑫𝑨 𝑲𝑬 𝑩𝑯𝑶𝑺𝑫𝑬 𝑴𝑬 𝑭𝑰𝑹𝑬𝑾𝑨𝑳𝑳 𝑳𝑨𝑮𝑨 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑫𝑨𝑫𝑨 𝑲𝑰 𝑪𝑯𝑼𝑻 𝑴𝑬 𝑺𝑺𝑫 𝑩𝑶𝑶𝑻 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑫𝑨𝑫𝑨 𝑲𝑨 𝑳𝑼𝑵𝑫 𝑶𝑳𝑿 𝑷𝑬 𝑩𝑬𝑪𝑯 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑫𝑨𝑫𝑨 𝑲𝑰 𝑮𝑨𝑨𝑵𝑫 𝑴𝑬 𝑸𝑹 𝑪𝑶𝑫𝑬 𝑪𝑯𝑰ℙ𝑲𝑨 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑫𝑨𝑫𝑨 𝑲𝑨 𝑩𝑯𝑺𝑶𝑫𝑨 𝑵𝑭𝑻 𝑴𝑬 𝑴𝑰𝑵𝑻 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑫𝑨𝑫𝑨 𝑲𝑨 𝑶𝑵𝑳𝒀𝑭𝑨𝑵𝑺 𝑳𝑰𝑽𝑬 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑫𝑨𝑫𝑨 𝑲𝑶 𝒁𝑰𝑷 𝑭𝑰𝑳𝑬 𝑴𝑬 𝑪𝑶𝑴𝑷𝑹𝑬𝑺𝑺 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑫𝑨𝑫𝑨 𝑲𝑬 𝑩𝑯𝑶𝑺𝑫𝑬 𝑴𝑬 𝑷𝒀𝑻𝑯𝑶𝑵 𝑹𝑼𝑵 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
]

# ==========================================

@app.on_message(filters.private & filters.command(["start", "help"], prefixes=["/", "."]))
async def start_cmd(client, message: Message):
    try:
        text = """
🔥 <b>FAST RAID BOT</b> 🔥

<b>AVAILABLE COMMANDS :</b>

.alive = Bot Online Check
.ping = Bot Speed
.speed = Speed Message
.r = Raid Start
.stopr = Stop Raid
.add = Add Sudo
.del = Remove Sudo
.help = Show Commands

<b>EXAMPLES :</b>

.r 5 @username
.r 20 reply karke

<b>BOT READY ⚡</b>
"""
        await message.reply_text(text)
    except Exception as e:
        logger.error(f"Error in start_cmd: {e}")

# ==========================================

def is_sudo(user_id):
    return user_id in sudo_users

async def sudo_error(message):
    try:
        await message.reply_text("❌ <b>SUDO NEHI HAI JAKE SUDO LE</b> ❌")
    except Exception as e:
        logger.error(f"Error in sudo_error: {e}")

# ==========================================

@app.on_message(filters.command("alive", prefixes="."))
async def alive_cmd(client, message: Message):
    if not is_sudo(message.from_user.id):
        return await sudo_error(message)
    try:
        await message.reply_text("✅ <b>BOT IS ALIVE AND READY</b> ✅")
    except Exception as e:
        logger.error(f"Error in alive_cmd: {e}")

# ==========================================

@app.on_message(filters.command("speed", prefixes="."))
async def speed_cmd(client, message: Message):
    if not is_sudo(message.from_user.id):
        return await sudo_error(message)
    try:
        await message.reply_text("⚡ <b>SUPER FAST BOT</b> ⚡")
    except Exception as e:
        logger.error(f"Error in speed_cmd: {e}")

# ==========================================

@app.on_message(filters.command("ping", prefixes="."))
async def ping_cmd(client, message: Message):
    if not is_sudo(message.from_user.id):
        return await sudo_error(message)
    try:
        start = time.time()
        msg = await message.reply_text("🏓 <b>Pinging...</b>")
        end = time.time()
        ping = round((end - start) * 1000)
        await msg.edit_text(f"🏓 <b>PONG :</b> <code>{ping} ms</code>")
    except Exception as e:
        logger.error(f"Error in ping_cmd: {e}")

# ==========================================

@app.on_message(filters.command("add", prefixes="."))
async def add_sudo(client, message: Message):
    if message.from_user.id != OWNER_ID:
        return
    try:
        if not message.reply_to_message:
            return await message.reply_text("❌ <b>Kisi ko reply karke .add karo</b> ❌")
        user_id = message.reply_to_message.from_user.id
        user_name = message.reply_to_message.from_user.first_name
        sudo_users.add(user_id)
        await message.reply_text(f"✅ <b>{user_name}</b> <b>ADDED IN SUDO</b> ✅")
        logger.info(f"User {user_id} added to sudo by owner")
    except Exception as e:
        logger.error(f"Error in add_sudo: {e}")

# ==========================================

@app.on_message(filters.command("del", prefixes="."))
async def del_sudo(client, message: Message):
    if message.from_user.id != OWNER_ID:
        return
    try:
        if not message.reply_to_message:
            return await message.reply_text("❌ <b>Kisi ko reply karke .del karo</b> ❌")
        user_id = message.reply_to_message.from_user.id
        user_name = message.reply_to_message.from_user.first_name
        if user_id in sudo_users:
            sudo_users.remove(user_id)
        await message.reply_text(f"❌ <b>{user_name}</b> <b>REMOVED FROM SUDO</b> ❌")
        logger.info(f"User {user_id} removed from sudo by owner")
    except Exception as e:
        logger.error(f"Error in del_sudo: {e}")

# ==========================================

@app.on_message(filters.command("r", prefixes="."))
async def raid_cmd(client, message: Message):
    if not is_sudo(message.from_user.id):
        return await sudo_error(message)
    try:
        args = message.text.split()
        if len(args) < 2:
            return await message.reply_text("❌ <b>USE : .r 5</b> ❌")
        if not message.reply_to_message:
            return await message.reply_text("❌ <b>SIR KISI KO TAG KARO</b> ❌")
        try:
            count = int(args[1])
            if count <= 0 or count > 500:
                return await message.reply_text("❌ <b>NUMBER 1-500 KE BEECH MEIN DO</b> ❌")
        except ValueError:
            return await message.reply_text("❌ <b>VALID NUMBER DO</b> ❌")
        target = message.reply_to_message.from_user
        mention = target.mention
        chat_id = message.chat.id
        raid_tasks[chat_id] = False
        await asyncio.sleep(0.5)
        raid_tasks[chat_id] = True
        raid_msg = await message.reply_text(f"🚀 <b>RAID STARTED ON {mention}</b> 🚀\n<b>COUNT:</b> <code>{count}</code>")
        for i in range(count):
            if not raid_tasks.get(chat_id):
                break
            try:
                line = custom_lines[i % len(custom_lines)]
                await message.reply_text(f"{mention} {line}")
                await asyncio.sleep(0.5)
            except FloodWait as e:
                logger.warning(f"Flood wait for {e.x} seconds")
                await asyncio.sleep(e.x)
            except Exception as e:
                logger.error(f"Error in raid loop: {e}")
                continue
        raid_tasks[chat_id] = False
        await raid_msg.edit_text(f"✅ <b>RAID COMPLETED ON {mention}</b> ✅")
    except Exception as e:
        logger.error(f"Error in raid_cmd: {e}")
        await message.reply_text(f"❌ <b>ERROR:</b> <code>{str(e)[:100]}</code> ❌")

# ==========================================

@app.on_message(filters.command("stopr", prefixes="."))
async def stop_raid(client, message: Message):
    if not is_sudo(message.from_user.id):
        return await sudo_error(message)
    try:
        chat_id = message.chat.id
        if chat_id in raid_tasks and raid_tasks[chat_id]:
            raid_tasks[chat_id] = False
            await message.reply_text("✅ <b>RAID STOPPED SUCCESSFULLY</b> ✅")
        else:
            await message.reply_text("⚠️ <b>NO ACTIVE RAID IN THIS CHAT</b> ⚠️")
    except Exception as e:
        logger.error(f"Error in stop_raid: {e}")

# ==========================================

@app.on_error()
async def error_handler(client, update, error):
    logger.error(f"Error occurred: {error}")

# ==========================================

async def main():
    logger.info("Starting bot...")
    await app.start()
    logger.info("Bot started successfully!")
    await asyncio.Event().wait()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("Bot stopped by user")
    except Exception as e:
        logger.error(f"Fatal error: {e}")
