import os
from dotenv import load_dotenv

load_dotenv()


class Links:

    HOST = os.getenv("HOST", "http://host.docker.internal:8000/")
    REGISTER_PAGE = HOST
    LOGIN_PAGE = f"{HOST}login"
    TEST_SQLI = f"{HOST}checkuser"