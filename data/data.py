from dotenv import load_dotenv
import os


load_dotenv()


class SelenoidData:
    SELENOID_LOGIN = os.getenv("SELENOID_LOGIN")
    SELENOID_PASS = os.getenv("SELENOID_PASS")
    SELENOID_URL = os.getenv("SELENOID_URL")
