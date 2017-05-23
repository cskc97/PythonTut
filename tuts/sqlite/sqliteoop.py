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
        self._db.execute("INSERT INTO {} VALUES(?,?)".format(self._dbName),(studentName,studentAge))

    def allRows(self):
        cursor = self._db.execute("SELECT * FROM {}".format(self._dbName))
        for row in cursor:
            print(row)

    def getTupleByName(self,studentName):

            cursor = self._db.execute("SELECT * FROM {} WHERE name=?".format(self._dbName),(studentName,))
            print(cursor.fetchone())










dbManager = DatabaseManager(dbname="dbmanager",tablename="students");
dbManager.insertInDB("Santhosh",19)
dbManager.allRows()
dbManager.getTupleByName("Santhosh")




