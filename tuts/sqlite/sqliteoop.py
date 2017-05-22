import sqlite3

class DatabaseManager:
    def __int__(self,**kwargs):
        self._dbName = kwargs["dbname"]
        self._db = sqlite3.connect(self._dbName);
        self._tableName = kwargs.get("tablename","unknown.db");

    

