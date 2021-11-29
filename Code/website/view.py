# standard routs for pages
from flask import Blueprint, render_template,url_for, request,flash
from flask_login import login_user, login_required, logout_user, current_user
from website import dbapp
views = Blueprint("views", __name__)

@views.route("/",methods=["GET","POST"])
@login_required
def home():
    listofperson=dbapp.listpersonforevent()
    nextweddinganniversary=dbapp.weddinganniversary()
    inmariage=dbapp.inmariage()
    alivepersonstat=dbapp.alivepersons()

    if request.method=="POST":
        if request.form.get("list_event"):
            alivepersonstat = dbapp.alivepersons()
            nextweddinganniversary=dbapp.weddinganniversary()
            persondraw = []
            personid=dbapp.getid(request.form.get("person"))
            outputevent = []
            outputevent.append(dbapp.eventofperso(personid))
            outputeventname=[]
            outputeventdate=[]
            outputrelpers = ""
            outputrelname = []
            for i in outputevent[0]:
                outputeventname.append(i[3])
                outputeventdate.append(i[2])
        elif request.form.get("family_tree"):
            nextweddinganniversary=dbapp.weddinganniversary()
            alivepersonstat = dbapp.alivepersons()
            outputeventname = ""
            outputeventdate = []
            outputrelpers = ""
            outputrelname = []
            print("fammtree")
            personid = dbapp.getid(request.form.get("person"))
            persondraw1=personid
            print(persondraw1)
            persondrawM2=dbapp.persondrawM2(personid)
            print(persondrawM2)
            persondrawF2=dbapp.persondrawF2(personid)
            print(persondrawF2)
            persondrawMM3=dbapp.persondrawMM3(personid)
            print(persondrawMM3)
            persondrawMF3=dbapp.persondrawMF3(personid)
            print(persondrawMF3)
            persondrawFM3=dbapp.persondrawFM3(personid)
            print(persondrawFM3)
            persondrawFF3=dbapp.persondrawFF3(personid)
            print(persondrawFF3)
            perosndrawMMM4=dbapp.perosndrawMMM4(personid)
            print(perosndrawMMM4)
            perosndrawMMF4=dbapp.perosndrawMMF4(personid)
            print(perosndrawMMF4)
            perosndrawMFM4=dbapp.perosndrawMFM4(personid)
            print(perosndrawMFM4)
            persondrawMFF4=dbapp.persondrawMFF4(personid)
            print(persondrawMFF4)
            persondrawFMM4=dbapp.persondrawFMM4(personid)
            print(persondrawFMM4)
            persondrawFMF4=dbapp.persondrawFMF4(personid)
            print(persondrawFMF4)
            persondrawFFM4=dbapp.persondrawFFM4(personid)
            print(persondrawFFM4)
            persondrawFFF4=dbapp.persondrawFFF4(personid)
            print(persondrawFFF4)
            persondraw=[dbapp.getname(persondraw1),
                        dbapp.getname(persondrawM2),dbapp.getname(persondrawF2),
                        dbapp.getname(persondrawMM3),dbapp.getname(persondrawMF3),dbapp.getname(persondrawFM3),dbapp.getname(persondrawFF3),
                        dbapp.getname(perosndrawMMM4),dbapp.getname(perosndrawMMF4),dbapp.getname(perosndrawMFM4),dbapp.getname(persondrawMFF4),dbapp.getname(persondrawFMM4),dbapp.getname(persondrawFMF4),dbapp.getname(persondrawFFM4),dbapp.getname(persondrawFFF4)]
        elif request.form.get("relationship_name"):
            alivepersonstat = dbapp.alivepersons()
            nextweddinganniversary=dbapp.weddinganniversary()
            persondraw = []
            outputeventname = ""
            outputeventdate = []
            outputrelpers = ""
            outputrelname = []
            firstperson=request.form.get("firstperson")
            secondperson = request.form.get("secondperson")
            relationship_name=request.form.get("relationship_name")
            if firstperson==secondperson:
                flash('Can’t make a relationship with the same people!', category='error')
            elif len(relationship_name)<=2:
                flash('Bad relationship name.', category='error')
            else:
                if dbapp.createrelationship(dbapp.getid(firstperson),dbapp.getid(secondperson),relationship_name):
                    flash('Created!', category='success')
                else:
                    flash('Fail!', category='error')
        elif request.form.get("delete_relationship"):
            alivepersonstat = dbapp.alivepersons()
            nextweddinganniversary=dbapp.weddinganniversary()
            persondraw = []
            outputeventname = ""
            outputeventdate = []
            outputrelpers = ""
            outputrelname = []
            relationshipid=request.form.get("relationship_id")

            if dbapp.deleterelationship(relationshipid):
                flash('Deleted!', category='success')
            else:
                flash('Fail!', category='error')
        elif request.form.get("modify_mariage"):
            alivepersonstat = dbapp.alivepersons()
            nextweddinganniversary=dbapp.weddinganniversary()
            persondraw = []
            outputeventname = ""
            outputeventdate = []
            outputrelpers = ""
            outputrelname = []
            marriegeid=request.form.get("mariage_id")
            status=request.form.get("status")

            if dbapp.modifymariage(marriegeid,status):
                flash('Modified!', category='success')
            else:
                flash('Fail!', category='error')
        elif request.form.get("create_event"):
            alivepersonstat = dbapp.alivepersons()
            nextweddinganniversary = dbapp.weddinganniversary()
            persondraw = []
            outputeventname = ""
            outputeventdate = []
            outputrelpers = ""
            outputrelname = []
            eventbyperson=request.form.get("eventbyperson")
            event_date=request.form.get("event_date")
            event_name=request.form.get("event_name")

            if dbapp.createevent(dbapp.getid(eventbyperson),event_date,event_name):
                flash('Created!', category='success')
            else:
                flash('Fail!', category='error')
        elif request.form.get("delete_oldevents"):
            alivepersonstat = dbapp.alivepersons()
            nextweddinganniversary = dbapp.weddinganniversary()
            persondraw = []
            outputeventname = ""
            outputeventdate = []
            outputrelpers = ""
            outputrelname = []
            if dbapp.deleteoldevents():
                flash('Deleted!', category='success')
            else:
                flash('Fail!', category='error')
        elif request.form.get("addmarriage"):
            alivepersonstat = dbapp.alivepersons()
            nextweddinganniversary = dbapp.weddinganniversary()
            persondraw = []
            outputeventname = ""
            outputeventdate = []
            outputrelpers = ""
            outputrelname = []
            firstperson=request.form.get("firstperson")
            secondperson=request.form.get("secondperson")
            marriage_date=request.form.get("marriage_date")
            # print(marriage_date,dbapp.getid(firstperson),dbapp.getid(secondperson))
            if dbapp.addmarriage(dbapp.getid(firstperson),dbapp.getid(secondperson),marriage_date):
                flash('Add!', category='success')
            else:
                flash('Fail!', category='error')
            inmariage = dbapp.inmariage()
        elif request.form.get("list_relationship"):
            alivepersonstat = dbapp.alivepersons()
            nextweddinganniversary = dbapp.weddinganniversary()
            persondraw = []
            outputeventname = ""
            outputeventdate = []
            relshippersonid=dbapp.getid(request.form.get("relshipperson"))
            outptrelationship=[]
            outptrelationship.append(dbapp.relationshipofperso(relshippersonid))
            outputrelname=[]
            outputrelpers=[]
            for i in outptrelationship[0]:
                outputrelname.append(i[3])
                outputrelpers.append(dbapp.getname(i[2]))
        elif request.form.get("addperson"):
            alivepersonstat = dbapp.alivepersons()
            nextweddinganniversary = dbapp.weddinganniversary()
            persondraw = []
            outputeventname = ""
            outputeventdate = []
            outputrelpers = ""
            outputrelname = []
            print(request.form.get("gender"))
            fatherid=dbapp.getid(request.form.get("fatherperson"))
            motherid=dbapp.getid(request.form.get("motherperson"))
            dateofbirth=request.form.get("dateofbirth")
            name=request.form.get("personname")
            personid = ""

            if request.form.get("gender")=="Male":
                print("da li udje ovde")
                gender=1
                personid+="10"
            else:
                gender=0
                personid+="11"
            personid+=motherid[0]
            personid += motherid[1]
            personid += fatherid[0]
            personid += fatherid[1]
            personid+=dateofbirth.split("-")[0]
            personid += dateofbirth.split("-")[1]
            personid += dateofbirth.split("-")[2]
            if dbapp.createuser(personid,name,fatherid,motherid,dateofbirth,gender):
                flash('Add!', category='success')
                alivepersonstat = dbapp.alivepersons()
            else:
                flash('Fail!', category='error')

        else:
            alivepersonstat = dbapp.alivepersons()
            nextweddinganniversary=dbapp.weddinganniversary()
            persondraw=[]
            outputeventname = ""
            outputeventdate = []
            outputrelpers = ""
            outputrelname = []


    if request.method == "GET":
        alivepersonstat = dbapp.alivepersons()
        nextweddinganniversary=dbapp.weddinganniversary()
        persondraw=[]
        outputeventname = ""
        outputeventdate = []
        outputrelpers=""
        outputrelname=[]


    return render_template("home.html",user=current_user, listofperson=listofperson,
                           outputeventlen=len(outputeventname),
                           outputeventname=outputeventname,
                           outputeventdate=outputeventdate,
                           persondraw=persondraw,
                           nextweddinganniversary=nextweddinganniversary,
                           inmariage=inmariage,
                           outputrellen=len(outputrelpers),outputrelpers=outputrelpers,
                           outputrelname=outputrelname,
                           alivepersonstat=alivepersonstat)