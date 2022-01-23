import os

import dotenv

dotenv.load_dotenv(".env.dev")

SECRET_KEY = os.environ["SECRET_KEY"]  # django secret key from django settings
