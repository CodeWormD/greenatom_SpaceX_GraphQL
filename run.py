import sys
import subprocess
from time import sleep

x = subprocess.Popen(['python', '-m', 'venv', 'venv'])
x.wait()
x = subprocess.Popen(['pip', 'install', '--upgrade', 'pip'])
x.wait()
x = subprocess.Popen(['pip', 'install', '-r', 'req.txt'])
x.wait()
x = subprocess.Popen(['alembic', 'revision', '--autogenerate', '-m', 'first_db'])
x.wait()
x = subprocess.Popen(['alembic', 'upgrade', 'head'])
x.wait()
x = subprocess.Popen([sys.executable, "spacex/upload_data.py"])
x.wait()