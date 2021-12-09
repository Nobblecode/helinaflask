import mysql.connector

mydb = mysql.connector.connect(
    host = 'localhost',
    database = 'tombra',
    user = 'root',
    password = ''
)


mycursor = mydb.cursor(dictionary=True)



mycursor.execute(
    """CREATE TABLE IF NOT EXISTS customers(
        ID INT NOT NULL AUTO_INCREMENT,
        name VARCHAR(255),
        address VARCHAR(255),
        age INT,
        PRIMARY KEY(ID)
    )
    """
)





