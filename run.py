import sys
import subprocess
from time import sleep


subprocess.run(['pip', 'install', '-r', 'req.txt'])
sleep(3)
subprocess.run(['alembic', 'revision', '--autogenerate', '-m', 'first_db'])
sleep(3)
subprocess.run(['alembic', 'upgrade', 'head'])
sleep(3)
subprocess.run([sys.executable, "spacex/upload_data.py"])
