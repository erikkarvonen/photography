from flask import Flask, render_template, json

app = Flask(__name__)

# Load image data
with open("data.json") as f:
    albums = json.load(f)

@app.route("/")
def home():
    return render_template("index.html", albums=albums)

@app.route("/album/<name>")
def album(name):
    images = albums.get(name, [])
    return render_template("album.html", album_name=name, images=images)

if __name__ == "__main__":
    app.run(debug=True)
