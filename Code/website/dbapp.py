import mysql.connector
from .models import User


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
        myresults = mycursor.fetchall()

        if (len(myresults)) == 0:

            return False
        else:
            user = {"email": myresults[0][0], "firstname": myresults[0][1],
                    "password": myresults[0][2]}
            return user

    except:
        print("Nincs DB")
        return False


def backuser(email):
    try:  # ha nincs db vagy nem sikerul csatlakozni akor except
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            database="famtree"

        )

        mycursor = mydb.cursor()
        sql = f"SELECT * FROM `users` WHERE `users`.`email` = '{email}';"
        mycursor.execute(sql)
        myresults = mycursor.fetchall()

        if (len(myresults)) == 0:

            return False
        else:
            user = User(myresults[0][0], myresults[0][1], myresults[0][2])
            return user

    except:
        print("Nincs DB")
        return False


def listpersonforevent():
    try:  # ha nincs db vagy nem sikerul csatlakozni akor except
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            database="famtree"

        )

        mycursor = mydb.cursor()
        sql = f"SELECT * FROM `Person` where `dateofdeth` is null order by `dateofbirth` asc;"
        mycursor.execute(sql)
        myresults = mycursor.fetchall()

        return myresults

    except:
        print("Nincs DB")
        return False

def eventofperso(personid):
    try:  # ha nincs db vagy nem sikerul csatlakozni akor except
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            database="famtree"

        )

        mycursor = mydb.cursor()
        sql = f"SELECT * FROM `EVENTTABLE` WHERE personid={personid} order by eventdate ASC;"
        mycursor.execute(sql)
        myresults = mycursor.fetchall()

        return myresults

    except:
        print("Nincs DB")
        return False

def getid(string):
    id = ""
    for i in range(len(string)):
        if string[i] != ",":
            if i > 0:
                id += string[i]
        else:
            break
    return id
def persondrawM2(id):
    retval=0
    try:  # ha nincs db vagy nem sikerul csatlakozni akor except
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            database="famtree"

        )

        mycursor = mydb.cursor()
        sql = f"SELECT personid FROM `Person` where personid=(SELECT fatherid FROM `Person` WHERE personid={id});"
        mycursor.execute(sql)
        myresults = mycursor.fetchall()
        retval=myresults[0][0]
        return retval
    except:
        print("Nincs DB")
        return retval
def persondrawF2(id):
    retval = 0
    try:  # ha nincs db vagy nem sikerul csatlakozni akor except
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            database="famtree"

        )

        mycursor = mydb.cursor()
        sql = f"SELECT personid FROM `Person` where personid=(SELECT motherid FROM `Person` WHERE personid={id});"
        mycursor.execute(sql)
        myresults = mycursor.fetchall()
        retval = myresults[0][0]
        return retval
    except:
        print("Nincs DB")
        return retval
def persondrawMM3(id):
    retval = 0
    try:  # ha nincs db vagy nem sikerul csatlakozni akor except
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            database="famtree"

        )

        mycursor = mydb.cursor()
        sql = f"SELECT personid FROM `Person` where personid=(SELECT fatherid FROM `Person` WHERE personid=((SELECT fatherid FROM `Person` WHERE personid={id})));"
        mycursor.execute(sql)
        myresults = mycursor.fetchall()
        retval = myresults[0][0]
        return retval
    except:
        print("Nincs DB")
        return retval
def persondrawMF3(id):
    retval = 0
    try:  # ha nincs db vagy nem sikerul csatlakozni akor except
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            database="famtree"

        )

        mycursor = mydb.cursor()
        sql = f"SELECT personid FROM `Person` where personid=(SELECT motherid FROM `Person` WHERE personid=((SELECT fatherid FROM `Person` WHERE personid={id})));"
        mycursor.execute(sql)
        myresults = mycursor.fetchall()
        retval = myresults[0][0]
        return retval
    except:
        print("Nincs DB")
        return retval
def persondrawFM3(id):
    retval = 0
    try:  # ha nincs db vagy nem sikerul csatlakozni akor except
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            database="famtree"

        )

        mycursor = mydb.cursor()
        sql = f"SELECT personid FROM `Person` where personid=(SELECT fatherid FROM `Person` WHERE personid=((SELECT motherid FROM `Person` WHERE personid={id})));"
        mycursor.execute(sql)
        myresults = mycursor.fetchall()
        retval = myresults[0][0]
        return retval
    except:
        print("Nincs DB")
        return retval
def persondrawFF3(id):
    retval = 0
    try:  # ha nincs db vagy nem sikerul csatlakozni akor except
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            database="famtree"

        )

        mycursor = mydb.cursor()
        sql = f"SELECT personid FROM `Person` where personid=(SELECT motherid FROM `Person` WHERE personid=((SELECT motherid FROM `Person` WHERE personid={id})));"
        mycursor.execute(sql)
        myresults = mycursor.fetchall()
        retval = myresults[0][0]
        return retval
    except:
        print("Nincs DB")
        return retval
def perosndrawMMM4(id):
    retval = 0
    try:  # ha nincs db vagy nem sikerul csatlakozni akor except
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            database="famtree"

        )

        mycursor = mydb.cursor()
        sql = f"SELECT personid FROM `Person` where personid=(SELECT fatherid FROM `Person` where personid=(SELECT fatherid FROM `Person` WHERE personid=(SELECT fatherid FROM `Person` WHERE personid={id})));"
        mycursor.execute(sql)
        myresults = mycursor.fetchall()
        retval = myresults[0][0]
        return retval
    except:
        print("Nincs DB")
        return retval
def perosndrawMMF4(id):
    retval = 0
    try:  # ha nincs db vagy nem sikerul csatlakozni akor except
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            database="famtree"

        )

        mycursor = mydb.cursor()
        sql = f"SELECT personid FROM `Person` where personid=(SELECT motherid FROM `Person` where personid=(SELECT fatherid FROM `Person` WHERE personid=(SELECT fatherid FROM `Person` WHERE personid={id})));"
        mycursor.execute(sql)
        myresults = mycursor.fetchall()
        retval = myresults[0][0]
        return retval
    except:
        print("Nincs DB")
        return retval
def perosndrawMFM4(id):
    retval = 0
    try:  # ha nincs db vagy nem sikerul csatlakozni akor except
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            database="famtree"

        )

        mycursor = mydb.cursor()
        sql = f"SELECT personid FROM `Person` where personid=(SELECT fatherid FROM `Person` where personid=(SELECT motherid FROM `Person` WHERE personid=(SELECT fatherid FROM `Person` WHERE personid={id})));"
        mycursor.execute(sql)
        myresults = mycursor.fetchall()
        retval = myresults[0][0]
        return retval
    except:
        print("Nincs DB")
        return retval
def persondrawMFF4(id):
    retval = 0
    try:  # ha nincs db vagy nem sikerul csatlakozni akor except
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            database="famtree"

        )

        mycursor = mydb.cursor()
        sql = f"SELECT personid FROM `Person` where personid=(SELECT motherid FROM `Person` where personid=(SELECT motherid FROM `Person` WHERE personid=(SELECT fatherid FROM `Person` WHERE personid={id})));"
        mycursor.execute(sql)
        myresults = mycursor.fetchall()
        retval = myresults[0][0]
        return retval
    except:
        print("Nincs DB")
        return retval
def persondrawFMM4(id):
    retval = 0
    try:  # ha nincs db vagy nem sikerul csatlakozni akor except
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            database="famtree"

        )

        mycursor = mydb.cursor()
        sql = f"SELECT personid FROM `Person` where personid=(SELECT fatherid FROM `Person` where personid=(SELECT fatherid FROM `Person` WHERE personid=(SELECT motherid FROM `Person` WHERE personid={id})));"
        mycursor.execute(sql)
        myresults = mycursor.fetchall()
        retval = myresults[0][0]
        return retval
    except:
        print("Nincs DB")
        return retval
def persondrawFMF4(id):
    retval = 0
    try:  # ha nincs db vagy nem sikerul csatlakozni akor except
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            database="famtree"

        )

        mycursor = mydb.cursor()
        sql = f"SELECT personid FROM `Person` where personid=(SELECT motherid FROM `Person` where personid=(SELECT fatherid FROM `Person` WHERE personid=(SELECT motherid FROM `Person` WHERE personid={id})));"
        mycursor.execute(sql)
        myresults = mycursor.fetchall()
        retval = myresults[0][0]
        return retval
    except:
        print("Nincs DB")
        return retval
def persondrawFFM4(id):
    retval = 0
    try:  # ha nincs db vagy nem sikerul csatlakozni akor except
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            database="famtree"

        )

        mycursor = mydb.cursor()
        sql = f"SELECT personid FROM `Person` where personid=(SELECT fatherid FROM `Person` where personid=(SELECT motherid FROM `Person` WHERE personid=(SELECT motherid FROM `Person` WHERE personid={id})));"
        mycursor.execute(sql)
        myresults = mycursor.fetchall()
        retval = myresults[0][0]
        return retval
    except:
        print("Nincs DB")
        return retval
def persondrawFFF4(id):
    retval = 0
    try:  # ha nincs db vagy nem sikerul csatlakozni akor except
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            database="famtree"

        )

        mycursor = mydb.cursor()
        sql = f"SELECT personid FROM `Person` where personid=(SELECT motherid FROM `Person` where personid=(SELECT motherid FROM `Person` WHERE personid=(SELECT motherid FROM `Person` WHERE personid={id})));"
        mycursor.execute(sql)
        myresults = mycursor.fetchall()
        retval = myresults[0][0]
        return retval
    except:
        print("Nincs DB")
        return retval

def getname(id):
    try:  # ha nincs db vagy nem sikerul csatlakozni akor except
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            database="famtree"

        )

        mycursor = mydb.cursor()
        sql = f"SELECT `name` FROM `Person` WHERE personid={id} ;"
        mycursor.execute(sql)
        myresults = mycursor.fetchall()
        # print(myresults[0][0])
        return myresults[0][0]

    except:
        print("Nincs DB")
        return "No person"

def createrelationship(person1,person2,rname):
    try:  # ha nincs db vagy nem sikerul csatlakozni akor except
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            database="famtree"

        )

        mycursor = mydb.cursor()
        sql = f"INSERT INTO `Relationship` (`RelationshipID`, `Person1`, `Person2`, `RelationshipName`) VALUES (NULL, '{person1}', '{person2}', '{rname}');"
        mycursor.execute(sql)
        mydb.commit()
        return True


    except:
        print("Nincs DB")
        return False


def deleterelationship(id):
    try:  # ha nincs db vagy nem sikerul csatlakozni akor except
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            database="famtree"

        )

        mycursor = mydb.cursor()
        sql = f"DELETE FROM `Relationship` WHERE `Relationship`.`RelationshipID` = {id};"
        mycursor.execute(sql)
        mydb.commit()
        return True


    except:
        print("Nincs DB")
        return False


def createmariage(person1,person2,rname):
    try:  # ha nincs db vagy nem sikerul csatlakozni akor except
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            database="famtree"

        )

        mycursor = mydb.cursor()
        sql = f"INSERT INTO `Relationship` (`RelationshipID`, `Person1`, `Person2`, `RelationshipName`) VALUES (NULL, '{person1}', '{person2}', '{rname}');"
        mycursor.execute(sql)
        mydb.commit()
        return True


    except:
        print("Nincs DB")
        return False

def modifymariage(id,value):
    try:  # ha nincs db vagy nem sikerul csatlakozni akor except
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            database="famtree"

        )

        mycursor = mydb.cursor()
        sql = f" UPDATE `Mariage` SET `stillgoingon` = '{value}' WHERE `Mariage`.`MariageID` = {id};"
        mycursor.execute(sql)
        mydb.commit()
        return True


    except:
        print("Nincs DB")
        return False

def weddinganniversary():
    try:  # ha nincs db vagy nem sikerul csatlakozni akor except
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            database="famtree"

        )

        mycursor = mydb.cursor()
        sql = f" SELECT MIN(EVENTTABLE.eventdate),name,EVENTTABLE.eventname from EVENTTABLE,Mariage,Person WHERE DAY(Mariage.MariageDate)=DAY(EVENTTABLE.eventdate) and EVENTTABLE.personid=Mariage.Person1;"
        mycursor.execute(sql)
        myresults = mycursor.fetchall()
        # print(myresults)
        ret=[myresults[0][2],myresults[0][1],myresults[0][0]]
        return ret

    except:
        print("Nincs DB")
        return ["no event","no event"]


def createevent(person,date,name):
    try:  # ha nincs db vagy nem sikerul csatlakozni akor except
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            database="famtree"

        )

        mycursor = mydb.cursor()
        if name=="":
            name="Birth day"
        sql = f"INSERT INTO `EVENTTABLE` (`eventid`, `personid`, `eventdate`, `eventname`) VALUES (NULL, '{person}', '{date}', '{name}')"
        # INSERT INTO `EVENTTABLE` (`eventid`, `personid`, `eventdate`, `eventname`) VALUES (NULL, '{person}', '{date}', 'Birth day')
        mycursor.execute(sql)
        mydb.commit()
        return True
    except:
        print("Nincs DB")
        return False

def deleteoldevents():
    try:  # ha nincs db vagy nem sikerul csatlakozni akor except
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            database="famtree"

        )

        mycursor = mydb.cursor()
        sql = f"DELETE FROM `EVENTTABLE` WHERE eventdate<CURRENT_DATE;"
        mycursor.execute(sql)
        mydb.commit()
        return True


    except:
        print("Nincs DB")
        return False

def addmarriage(firstperson,secondperson,marriage_date):
    try:  # ha nincs db vagy nem sikerul csatlakozni akor except
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            database="famtree"

        )

        mycursor = mydb.cursor()
        sql = f"INSERT INTO `Mariage` (`MariageID`, `Person1`, `Person2`, `MariageDate`, `stillgoingon`) VALUES (NULL, '{firstperson}', '{secondperson}', '{marriage_date}', '1');"
        mycursor.execute(sql)
        mydb.commit()
        return True
    except:
        print("Nincs DB")
        return False


def inmariage():
    try:  # ha nincs db vagy nem sikerul csatlakozni akor except
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            database="famtree"

        )

        mycursor = mydb.cursor()
        sql = f"SELECT Person.name FROM `Person`,Mariage WHERE Mariage.Person1=personid or Mariage.Person2=personid  ORDER  by Person.gender,Person.dateofbirth;"
        mycursor.execute(sql)
        myresults = mycursor.fetchall()
        # print(myresults)
        ret=[]
        for i in myresults:
            ret.append(i[0])
        # print(ret)
        return ret

    except:
        print("Nincs DB")
        return ["no person"]

def relationshipofperso(personid):
    try:  # ha nincs db vagy nem sikerul csatlakozni akor except
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            database="famtree"

        )

        mycursor = mydb.cursor()
        sql = f"SELECT * FROM `Relationship` WHERE Person1={personid} ORDER by RelationshipName asc;"
        mycursor.execute(sql)
        myresults = mycursor.fetchall()

        return myresults

    except:
        print("Nincs DB")
        return False

def createuser(personid,name,father,mother,dateofbirth,gender):
    try:  # ha nincs db vagy nem sikerul csatlakozni akor except
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            database="famtree"

        )

        mycursor = mydb.cursor()
        sql = f"INSERT INTO `Person` (`personid`, `fatherid`, `motherid`, `name`, `dateofbirth`, `dateofdeth`, `gender`) VALUES ('{personid}', '{father}', '{mother}', '{name}', '{dateofbirth}', NULL, '{str(gender)}');"
        mycursor.execute(sql)
        mydb.commit()
        return True
    except:
        print("Nincs DB")
        return False


def alivepersons():
    try:  # ha nincs db vagy nem sikerul csatlakozni akor except
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            database="famtree"

        )

        mycursor = mydb.cursor()
        sql = f"SELECT gender,count(*) FROM `Person` WHERE dateofdeth is null GROUP by gender order by COUNT(*) DESC;"
        mycursor.execute(sql)
        myresults = mycursor.fetchall()
        # print(myresults)
        ret={"Male":0,"Female":0}
        for i in myresults:
            if i[0]==1:
                ret["Male"]=i[1]
            else:
                ret["Female"]=i[1]
        return ret

    except:
        print("Nincs DB")
        ret = {"Male": 0, "Female": 0}
        return ret