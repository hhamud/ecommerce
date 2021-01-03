
from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
# /home/user/Documents/PythonScripts/ecommerce/backend/shop_backend

BACKEND_DIR = os.path.join(BASE_DIR, '..')
FRONTEND_DIR = os.path.join(BACKEND_DIR, '..', 'frontend')

print(FRONTEND_DIR)