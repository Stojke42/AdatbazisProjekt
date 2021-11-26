import mysql.connector
def conect_to_db():
    try:  # ha nincs db vagy nem sikerul csatlakozni akor except
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                database="famtree"

            )
            mycursor = mydb.cursor()
            return mycursor

    except:
        print("Nincs DB")
        return "NODB"


def existuser(mydb,email):
    mydb.execute("Show tables;")

    myresult = mydb.fetchall()

    for x in myresult:
        print(x[0])
    return True

