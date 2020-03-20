import sqlite3
from datetime import datetime
class dbconnect:
    def __init__(self,dbname):
        self.dbname=dbname
    def connection(self):
        conn = sqlite3.connect(self.dbname)
        cur = conn.cursor()

        cmd = """
        CREATE TABLE IF NOT EXISTS station_status (
        	id INTEGER PRIMARY key AUTOINCREMENT,
        	station_id INT,
        	last_date TEXT,
        	alarm1 INT,
        	alarm2 INT   
        );
        """
        cur.execute(cmd)
        conn.commit()
        conn.close()
    def insert(self,id,alarm1,alarm2):
        conn = sqlite3.connect(self.dbname)
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO station_status (station_id,last_date,alarm1,alarm2) VALUES (?,?,?,?)",(id, str(datetime.now()), alarm1, alarm2,))
        conn.commit()
        conn.close()



