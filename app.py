#import libraries
from flask import Flask, render_template, request
import joblib

#instance of an app
app = Flask(__name__)

model = joblib.load('dib_79.pkl')

@app.route("/")
def welcome():
    return render_template("welcome.html")

@app.route("/home")
def home_page():
    return render_template("home.html")

@app.route("/blog", methods= ['POST'])
def blog():
    preg = request.form.get('preg')
    plas = request.form.get('plas')
    pres = request.form.get('pres')
    skin = request.form.get('skin')
    test = request.form.get('test')
    mass = request.form.get('mass')
    pedi = request.form.get('pedi')
    age = request.form.get('age')
 

    print(preg,plas,pres,skin,test,mass,pedi,age)

    pred = model.predict([[preg,plas,pres,skin,test,mass,pedi,age]])
    if pred[0] == 1:
        output = "Diabetic"
    else:
        output = "Not Diabetic"


    return render_template("blog.html", predicted_text = f'The Person Is {output}')

#run the app
if __name__=="__main__":
        app.run(debug=True)