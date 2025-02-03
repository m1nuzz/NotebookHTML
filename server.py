from flask import Flask, render_template, request

app = Flask(__name__)

# Global variable to store the text
shared_text = ""

@app.route("/", methods=["GET", "POST"])
def index():
    global shared_text
    if request.method == "POST":
        shared_text = request.form["text"]
    return render_template("index.html", text=shared_text)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
