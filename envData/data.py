import os, dotenv

dotenv.load_dotenv()

TOKEN = os.getenv('TOKEN')
COUNTRY_CODE = os.getenv('COUNTRY_CODE')
STATE = os.getenv('STATE')
CITY = os.getenv('CITY')
LIMIT = os.getenv('LIMIT')