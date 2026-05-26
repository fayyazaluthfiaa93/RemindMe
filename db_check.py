#for check connection between db and py

import mysql.connector

try:
    db = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "",
        database = "remindme"
    )

    if db.is_connected():
        print("py and db are succesfully connect")
        db.close()

except Exception as e:
    print(f"connected error: {e}")