from flask import Flask, render_template, request
import os
from privacy_engine import process_image

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        file = request.files["image"]

        if file:
            input_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            output_path = os.path.join("static", "output.png")

            file.save(input_path)

            process_image(input_path, output_path)

            return render_template("index.html", image="output.png")

    return render_template("index.html", image=None)


if __name__ == "__main__":
    app.run(debug=True)