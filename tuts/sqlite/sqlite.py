import sqlite3

def main():
    db = sqlite3.connect("test.db");
    #Adding db.row_factory = sqlite3.Row will return row objects instead of
    #values in the row. And you can use it as a dictionary if required also


    db.execute("DROP TABLE IF EXISTS Students")
    db.execute("CREATE TABLE Students(name TEXT, age INT)")
    db.execute("INSERT INTO Students VALUES (?,?)",("Santhosh",19))
    db.execute("INSERT INTO Students VALUES (\'Another Santhosh\',19)")

    db.commit()

    cursor = db.execute("SELECT * FROM Students")
    for row in cursor:
        print(row)
        print(row[0],row[1])
        print("Name - {}".format(row[0]))
        print("Age - {}".format(row[1]))


main()

