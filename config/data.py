import os
from dotenv import load_dotenv
import uuid

load_dotenv()

class Data:

    def __init__(self):
        base_username = os.getenv("TEST_USERNAME", "user")
        self.username = f"{base_username}_{uuid.uuid4().hex[:8]}"
        self.password = os.getenv("TEST_PASSWORD")
