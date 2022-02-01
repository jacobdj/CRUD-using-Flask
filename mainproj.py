from flask import *
from DBM import addEmp,selectAllEmp,deleteEmp,selectEmpById,updateEmp,name_pass
app=Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/addEmp",methods=["POST"])
def add_emp():
    id=request.form["id"]
    name=request.form["name"]
    contact=request.form["contact"]
    email=request.form["email"]
    pwd=request.form["pwd"]

    t=(id,name,contact,email,pwd)
    addEmp(t)
    return redirect("/emplist")

@app.route("/emplist")
def emp_list():
    d=selectAllEmp()
    return render_template("records.html",elist=d)

@app.route("/del")
def delete():
    return render_template("del.html")
@app.route("/deleteEmp",methods=["POST"])
def delete_emp():
    id=request.form["id"]
    deleteEmp(id)
    return redirect("/emplist")

@app.route("/update")
def update():
    return render_template("update.html")
@app.route("/updateEmp",methods=["POST"])
def update_emp():
    name=request.form["name"]
    contact=request.form["contact"]
    email=request.form["email"]
    pwd=request.form["pwd"]
    id=request.form["id"]

    t=(name,contact,email,pwd,id)
    updateEmp(t)

    return redirect("/emplist")
@app.route("/notreg")
def notreg():
    return render_template("notreg.html")

@app.route("/login")
def login():
    return render_template("login.html")
@app.route("/log",methods=["POST"])
def ulog():
    name=request.form["uname"]
    pwd=request.form["pwd"]
    d=name_pass()
    if((name,pwd)in d):
        return redirect("/emplist")
    else:
        return redirect("/notreg")
        

   



if(__name__=="__main__"):
    app.run(debug=True)
