import os
from dotenv import load_dotenv

load_dotenv('.env')

PROJECT_TITLE = os.getenv('PROJECT_TITLE', 'Community Blog')
PROJECT_DESCRIPTION = os.getenv('PROJECT_DESCRIPTION', 'A community-driven blog and mobile app')
PROJECT_VERSION = os.getenv('PROJECT_VERSION', '1.0.0')
