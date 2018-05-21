# Added ~/pasa_api/posa_api to $PYTHONPATH

from sqlalchemy import create_engine

engine = create_engine('postgresql://postgres:yuiyui@localhost/posa_db')

conn = engine.connect()
conn.execute("commit")
# conn.execute("drop database test")
# conn.close()

