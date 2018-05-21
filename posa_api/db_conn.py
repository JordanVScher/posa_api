# Added ~/pasa_api/posa_api to $PYTHONPATH
from sqlalchemy import create_engine
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

import os
database_password = os.getenv("database_password")
print(database_password)

engine = create_engine('postgresql://postgres:' + database_password + '@localhost/')

conn = engine.connect()
conn.execute("commit")
# conn.execute("drop database test")
# conn.close()

