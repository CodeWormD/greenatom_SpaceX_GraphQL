import sys
import subprocess
from time import sleep
import os



# cmd = '/venv/Scripts/activate'

# x = subprocess.Popen(['python', '-m', 'venv', 'venv'])
# x.wait()
# # x = subprocess.Popen(['source /venv/Scripts/activate'])
# # x.wait()
x = subprocess.Popen(['python.exe -m pip install --upgrade pip'])
x.wait()
x = subprocess.Popen(['pip', 'install', '-r', 'req.txt'])
x.wait()
x = subprocess.Popen(['alembic', 'revision', '--autogenerate', '-m', 'first_db'])
x.wait()
x = subprocess.Popen(['alembic', 'upgrade', 'head'])
x.wait()
x = subprocess.Popen([sys.executable, "spacex/upload_data.py"])
x.wait()