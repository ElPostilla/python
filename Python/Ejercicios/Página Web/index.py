from http.client import LENGTH_REQUIRED
from flask import Flask, render_template

app=Flask(__name__)
""""
@app.route("/")
def principal():
    return "Esto es python en html"

@app.route("/contacto")
def contacto():
    return "Esta es la pagina de contacto"
"""

@app.route("/")
def principal():
    return render_template("index.html")

@app.route("/lenguajes")
def mostrar_lenguajes():
    lenguajes=("PHP", "Python", "Java", "C#", 
                "JavaScript", "Perl", "Ruby", "Rust")
    return render_template("lenguajes.html", lenguajes=lenguajes)

@app.route("/contacto")
def contacto():
    return render_template("contacto.html")

if __name__=='__main__':
    app.run(debug=True, port=5017)
