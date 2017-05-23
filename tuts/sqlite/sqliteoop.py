import sqlite3

class DatabaseManager:
    def __init__(self,**kwargs):
        self._dbName = kwargs["dbname"]
        self._db = sqlite3.connect(self._dbName);
        self._tableName = kwargs.get("tablename","unknown");
        self._db.execute("DROP TABLE IF EXISTS {}".format(self._dbName))
        self._db.execute("CREATE TABLE {}(name TEXT, age INT)".format(self._dbName));
        self._db.commit()

    def insertInDB(self,studentName,studentAge):
        




dbManager = DatabaseManager(dbname="dbmanager",tablename="students");




