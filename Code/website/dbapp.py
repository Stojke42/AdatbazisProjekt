import mysql.connector


def conect_to_db():
    try:  # ha nincs db vagy nem sikerul csatlakozni akor except
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            database="famtree"

        )
        mycursor = mydb.cursor()
        email = "aleksandarfax@gmail.com"
        sql = f"SELECT * FROM users WHERE users.email='{email}';"
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        print(myresult)
        for x in myresult:
            print(x)
            print(type(x))
            print(myresult)
            # ----------------------------------------------------------------
        return 0

    except:
        print("Nincs DB")
        return "NODB"


def existuser(email):
    try:  # ha nincs db vagy nem sikerul csatlakozni akor except
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            database="famtree"

        )
        mycursor = mydb.cursor()
        sql = f"SELECT * FROM users WHERE users.email='{email}';"
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        if len(myresult) != 0:
            # ----------------------------------------------------------------
            return True
        else:
            return False


    except:
        print("Nincs DB")
        return "NODB"


def addnewuser(newuser):
    try:  # ha nincs db vagy nem sikerul csatlakozni akor except
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            database="famtree"

        )
        mycursor = mydb.cursor()
        if (type(newuser) == dict):
            email = newuser["email"]
            fname = newuser["firstName"]
            password = newuser["password"]
            sql = f"INSERT INTO `users` (`email`, `firstname`, `password`) VALUES ('{email}','{fname}','{password}');"
            mycursor.execute(sql)
            mydb.commit()
            return True
        else:
            return False


    except:
        print("Nincs DB")
        return False


def loginuser(email):
    try:  # ha nincs db vagy nem sikerul csatlakozni akor except
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            database="famtree"

        )

        mycursor = mydb.cursor()
        sql = f"SELECT * FROM `users` WHERE `users`.`email` = '{email}';"
        mycursor.execute(sql)
        myresults=mycursor.fetchall()
        print(len(myresults))
        if (len(myresults)) == 0:
            print("dibije false")
            return False
        else:
            user = {"email": myresults[0][0], "firstname": myresults[0][1],
                    "password": myresults[0][2]}
            return user

    except:
        print("Nincs DB")
        return False
