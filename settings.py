import os
from pathlib import Path

import environ

ROOT_PATH = Path(__file__).parent.absolute()

env = environ.Env()
environ.Env.read_env(os.path.join(ROOT_PATH, ".env"))


BOT_TOKEN = env.str("BOT_TOKEN")
