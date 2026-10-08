from flask import Flask, render_template, request, send_from_directory

app = Flask(__name__, template_folder="Templates")


@app.route("/")
def inicio():
    return render_template("login.html")


@app.route("/logo")
def logo():
    return send_from_directory("Uploads", "logo.png")


@app.route("/fundo")
def fundo():
    return send_from_directory("Uploads", "fundo.png")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        senha = request.form.get("senha")

        print("E-mail:", email)
        print("Senha:", senha)

    return render_template("login.html")


@app.route("/cadastro", methods=["GET", "POST"])
def cadastro():
    if request.method == "POST":
        nome = request.form.get("nome")
        email = request.form.get("email")
        senha = request.form.get("senha")

        print("Nome:", nome)
        print("E-mail:", email)
        print("Senha:", senha)

        return render_template("login.html")

    return render_template("cadastro_usuario.html")


if __name__ == "__main__":
    app.run(debug=True)