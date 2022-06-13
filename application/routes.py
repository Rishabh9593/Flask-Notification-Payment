from application import app, db, mongo, myclient
from flask import render_template, request, json, Response, redirect, flash, url_for, session
from application.models import User, Books, Issue
from application.forms import LoginForm, RegisterForm
import stripe
from datetime import datetime, timedelta
import requests

@app.route("/")
@app.route("/index")
@app.route("/home")
def index():
    return render_template("index.html", index=True )

'''
@app.route("/Adminlogin", methods=['GET','POST'])
def Adminlogin():
    session['type'] = "Admin"
    if session.get('username'):
        return redirect(url_for('welcome'))

    form = LoginForm()
    if form.validate_on_submit():
        email       = form.email.data
        password    = form.password.data
        # pylint: disable=no-member
        user = User.objects(email=email).first()
        if user and user.get_password(password):
            flash(f"{user.first_name}, you are successfully logged in!", "success")
            session['user_id'] = user.user_id
            session['username'] = user.first_name
            
            return redirect("/index")
        else:
            flash("Sorry, something went wrong.","danger")
    return render_template("login.html", title="Login", form=form, login=True )
'''

@app.route("/login", methods=['GET','POST'])
def login():
    if session.get('username'):
        return redirect(url_for('index'))

    form = LoginForm()
    if form.validate_on_submit():
        email       = form.email.data
        password    = form.password.data
        # pylint: disable=no-member
        user = User.objects(email=email).first()
        if user and user.get_password(password):
            flash(f"{user.first_name}, you are successfully logged in!", "success")
            session['user_id'] = user.user_id
            session['username'] = user.first_name
            session['Year'] = user.Year
            session['branch'] = user.branch
            
            return redirect("/index")
        else:
            flash("Sorry, something went wrong.","danger")
    return render_template("login.html", title="Login", form=form, login=True )

'''
@app.route("/Stafflogin", methods=['GET','POST'])
def Stafflogin():
    if session.get('username'):
        return redirect(url_for('index'))

    form = LoginForm()
    if form.validate_on_submit():
        email       = form.email.data
        password    = form.password.data
        # pylint: disable=no-member
        user = User.objects(email=email).first()
        if user and user.get_password(password):
            flash(f"{user.first_name}, you are successfully logged in!", "success")
            session['user_id'] = user.user_id
            session['username'] = user.first_name
            session['Year'] = user.Year
            session['branch'] = user.branch
            
            return redirect("/index")
        else:
            flash("Sorry, something went wrong.","danger")
    return render_template("login.html", title="Login", form=form, login=True )


@app.route("/Adminregister", methods=['POST','GET'])
def Adminregister():
    if session.get('username'):
        return redirect(url_for('index'))
    form = AdminRegisterForm()
    if form.validate_on_submit():
        # pylint: disable=no-member
        admin_id     = Admin.objects.count()
        admin_id     += 3

        email       = form.email.data
        password    = form.password.data
        first_name  = form.first_name.data
        last_name   = form.last_name.data

        admin = Admin(admin_id=admin_id, email=email, first_name=first_name, last_name=last_name)
        admin.set_password(password)
        admin.save()
        flash("You are successfully registered!","success")
        return redirect(url_for('index'))
    return render_template("Adminregister.html", title="Register", form=form, register=True)
'''

@app.route("/register", methods=['POST','GET'])
def register():
    '''
    if session.get['type'] == "Admin":
        return redirect(url_for('Adminregister'))
    if session.get['type'] == "Staff":
        return redirect(url_for('Staffregister'))
    '''    
    if session.get('username'):
        return redirect(url_for('index'))
    form = RegisterForm()
    if form.validate_on_submit():
        # pylint: disable=no-member
        #user_id     = User.objects.count()
        #user_id     += 3

        email       = form.email.data
        password    = form.password.data
        first_name  = form.first_name.data
        last_name   = form.last_name.data
        Year = form.Year.data
        branch = form.branch.data
        chat_id = form.TelegramUserID.data

        user = User(user_id= chat_id, email=email, first_name=first_name, last_name=last_name, Year=Year, branch=branch)
        user.set_password(password)
        #user.set_tgid(chat_id)
        user.save()
        flash("You are successfully registered!","success")

        URL = "https://api.telegram.org/bot1374267801:AAFBeI6TX4rpsHeYJa3rG1rHHJqIEW9j7I8/sendMessage"
        PARAMS = {'text':'Welcome to library Management System, you will be notified about your due fees of payment here','chat_id':chat_id} 
        r = requests.get(url = URL, params = PARAMS) 
        data = r.json() 
        print(data)

        return redirect(url_for('index'))
    return render_template("register.html", title="Register", form=form, register=True)

'''
@app.route("/Staffregister", methods=['POST','GET'])
def register():
    if session.get('username'):
        return redirect(url_for('index'))
    form = RegisterForm()
    if form.validate_on_submit():
        # pylint: disable=no-member
        user_id     = User.objects.count()
        user_id     += 3

        email       = form.email.data
        password    = form.password.data
        first_name  = form.first_name.data
        last_name   = form.last_name.data
        Year = form.Year.data
        branch = form.branch.data
        

        user = User(user_id=user_id, email=email, first_name=first_name, last_name=last_name, Year=Year, branch=branch)
        user.set_password(password)
        user.save()
        flash("You are successfully registered!","success")
        return redirect(url_for('index'))
    return render_template("register.html", title="Register", form=form, register=True)
'''

@app.route("/logout")
def logout():
    session['user_id']=False
    session['type']="None"
    session.pop('username',None)
    return redirect(url_for('index'))

@app.route("/books/")
@app.route("/books/<year>")
def books(year = None):
    if year is None:
        year = "Spring 2019"
        # pylint: disable=no-member
    #Books(BookId="5", title="Book4", publication="publi4", author="auth4", No_of_Copies="5",Year="2019").save()
      
    booksdata = Books.objects.order_by("-BookId")
    return render_template("books.html", booksData=booksdata, books = True, year=year )

'''
@app.route("/api/")
@app.route("/api/<idx>")
def api(idx=None):
    if(idx == None):
        jdata = courseData
    else:
        jdata = courseData[int(idx)]
    
    return Response(json.dumps(jdata), mimetype="application/json")
'''

@app.route("/user")
def user():
    # pylint: disable=no-member
     #User(user_id=1, first_name="Christian", last_name="Hur", email="christian@uta.com", password="abc1234").save()
     #User(user_id=2, first_name="Mary", last_name="Jane", email="mary.jane@uta.com", password="password123").save()
     users = User.objects.all()
     return render_template("user.html", users=users)

'''
@app.route("/payment", methods=['POST','GET'])
def payment():
    form = Payment()
    
    stripe.checkout.Session.create(
    success_url = url_for('thanks',_external=True) + '?session_id={CHECKOUT_SESSION_ID}',
    cancel_url = url_for('payment',_external=True),
    payment_method_types=["card"],
    line_items=[{
    "price": "price_1HGm7QFB0yRJy3BjQN5zByXs",
                "quantity": 1,
    },
    ],
    mode="payment",)
    checkout_session_id=session['id'], 
    print(checkout_session_id)
    return render_template('payment.html', 
        checkout_session_id=session['id'],
        checkout_public_key=app.config['STRIPE_PUBLIC_KEY'],
        form=form
        )  
'''

@app.route("/thanks")
def thanks():
    return render_template("thanks.html")      



@app.route('/1')
def index1():
    if not session.get('username'):
        return redirect(url_for('login'))  
    
    user_id = session.get('user_id')

    if session.get('paying_book'):
        BookId = session['paying_book']


        # pylint: disable=no-member
        
        p = Issue.objects(user_id=user_id, BookId=BookId)
        p.delete()
        
    
    # pylint: disable=no-member
    books = Issue.objects(user_id=user_id, fees__gt="0")
    return render_template("t.html", issue=True, title="Issued", books = books, key=app.config['STRIPE_PUBLIC_KEY'], pay=True)    


@app.route('/charge1', methods=['POST','GET'])
def charge1():
    BookId = request.form.get('BookId')
    session['paying_book'] = BookId

    Date_now = datetime.now() 
    mydb = myclient['project']
    mycol = mydb['issue']
    x = mycol.find_one({'BookId': BookId})
    Return_date = x['Return_date'] 
    if Date_now > Return_date:
        d0 = Date_now
        d1 = Return_date
        delta = d0 - d1
        amount = delta.days*500
        amount1 = delta.days*5
       
    stripe.Charge.create(
        amount=amount,
        currency='inr',
        card=request.form['stripeToken'],
        description='Stripe Flask')

    return render_template('thanks.html', amount=amount1)

@app.route("/issue", methods=["GET","POST"])
def issue():

    if not session.get('username'):
        return redirect(url_for('login'))

    BookId = request.form.get('BookId')
    title = request.form.get('title')
    publication = request.form.get('publication')
    author = request.form.get('author')
    Issue_date = datetime.now()
    Return_date = Issue_date + timedelta(days=15)

    Year = session.get('Year')
    branch = session.get('branch')
    
    
    user_id = session.get('user_id')

    if BookId:
        # pylint: disable=no-member
        if Issue.objects(user_id=user_id,BookId=BookId):
            flash(f"Oops! You have already issued this book: {title}!", "danger")
            return redirect(url_for("books"))
        else:
            mydb = myclient['project']
            mycol = mydb["books"]
            x = mycol.find_one({'BookId': BookId})
            copies = x["No_of_Copies"]

            if copies > 0:
                Issue(user_id=user_id,BookId=BookId,title=title, publication=publication, author=author, Issue_date=Issue_date, Return_date=Return_date, Year=Year, branch=branch, fees=0).save()
                flash(f"You have issued these book: {title}!", "success")
                copies -= 1
                myquery = { 'BookId': BookId }
                newvalues = { "$set": { "No_of_Copies": copies } }
                mycol.update_one(myquery, newvalues)
            else:
                flash(f"Oops! This book is out of stock, try later {title}!", "danger")
                return redirect(url_for("books"))    
    # pylint: disable=no-member
    books = Issue.objects(user_id=user_id)
    return render_template("issue.html", issue=True, title="Issued", books = books)    



if __name__ == '__main__':
  app.run(debug=True)    