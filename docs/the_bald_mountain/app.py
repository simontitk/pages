from flask import Flask, render_template, send_from_directory
import map


app = Flask(__name__)

app.config["UPLOAD_FOLDER"] = "static"


@app.route("/")
def index():
    
    return render_template("map.html")


@app.route("/image/<name>")
def image(name):
    path = f"{name}.jpg"
    print(path)
    return send_from_directory(directory=app.config["UPLOAD_FOLDER"], path=path)


if __name__ == "__main__":
    map.create_map(lang="eng")
    app.run(debug=True) 