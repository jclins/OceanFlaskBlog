from flask import Flask, render_template

app = Flask("hello")
nomeAula = "Aula python para Web"

@app.route("/")
def heelo():
    return "Hello"

@app.route("/usuario")
def usuario():
    usuario = [1,"JOCA","Professor"]
    alunos = ["Alice","Arthur","Bernardo","Davi","Gabriel","Heitor","Helena","Heloísa","João","Laura","Maria Alice","Maria Cecília","Maria Clara","Maria Julia","Miguel","Miguel","Samuel","Sophia","Theo","Valentina"]
    return render_template("index.html", usuario=usuario, nome=nomeAula, alunos=alunos  )

@app.route("/contato")
def contato():
    # nomeAula = "Aula python para Web"
    return render_template("index.html", nome=nomeAula )
    # return     """
    # <html>
    #     <head>
    #         <title>SOU EU!!!</title>
    #     </head>
    #     <body>
    #         <h1>JOCA LINS</h1>
    #     </body>
    # </html>
    # """