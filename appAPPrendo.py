from flask import Flask, request, render_template

app = Flask(__name__, template_folder="view")

@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html")

@app.route("/crianca")
def Perfilcriana():
    return render_template("index2.html")

@app.route("/professor")
def Pagprofissional():
    return render_template("indexProfessor.html")

@app.route("/logincrianca")
def LoginCrianca():
    return render_template("login.html")

@app.route("/cadastrocrianca")
def cadastrocrianca():
    return render_template('cadastroCrianca.html')

@app.route("/estudoconteuro")
def estudoConteudo():
    return render_template("estudoConteudo.html")

@app.route("/buscaProfessor")
def buscaProfessor():
    return render_template("indexProfessor.html")

@app.route("/autentica",methods=['POST'])
def autentica():
    cepusr = request.form['cep']
    pswrd = request.form['senha']
    #Consultar se usuário existe, passando usr e pswrd!
    return render_template("usuario.html", cep=cepusr, senha=pswrd)

@app.route("/menuConteudo")
def menuConteudo():
    return render_template("menuConteudo.html")

@app.route("/estudo")
def estudo():
    return render_template("estudoConteudo.html")

@app.route("/questoes")
def questoes():
    pass

if __name__ == "__main__":
  app.run()