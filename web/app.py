from flask import Flask, render_template, request, abort

app = Flask(__name__)

@app.route("/")
def hello():
    return "UOCI docker demo!"

@app.route("/<path:file>")
def get_file(file):
    if "~" in file or "//" in file or ".." in file:
        abort(403)

    elif(file.endswith(".html") or file.endswith(".css")):
        if "./templates" in file:
            local_path = file
        else:
            local_path = "./templates/" + file
        try:
            with open(local_path, "r") as f:
                content = f.read()
                content_type = "text/css" if file.endswith(".css") else "text/html"
            return content, 200, {'Content-Type': content_type}
        except FileNotFoundError:
            abort(404)
    else:
        abort(404)

@app.errorhandler(404)
def p_n_f(a):
    return render_template("404.html"), 404

@app.errorhandler(403)
def forbidden(a):
    return render_template("403.html"), 403


if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')
