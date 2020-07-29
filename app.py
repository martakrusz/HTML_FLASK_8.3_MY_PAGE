from flask import Flask
from flask import render_template
from flask import request, redirect, url_for

app = Flask(__name__)


@app.route('/mypage/me', methods=['GET'])
def mypage():
    if request.method == 'GET':
        owner = {"Imię": "Marta", "Nazwisko": "Krusz"}
        print("We received GET")
        return render_template("me.html", items=owner)
    elif request.method == 'POST':
        return redirect(url_for("mp_contact"))


@app.route('/mypage/contact', methods=['GET', 'POST'])
def mp_contact():
   if request.method == 'GET':
       print("We received GET")
       return render_template("contact.html")
   elif request.method == 'POST':
       print("We received POST")
       print(request.form)
       return redirect(url_for('mp_contact'))

if __name__ == "__main__":
    app.run(debug=True)
    