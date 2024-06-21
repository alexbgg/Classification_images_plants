import os

from flask import Flask, render_template, request
from werkzeug.utils import secure_filename

# from src.models.predict_model import predict_image

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def upload_file():
    if request.method == "POST":
        # Check if the post request has the file part
        if "file" not in request.files:
            return render_template("web_app.html", message="No file part")
        file = request.files["file"]
        if file.filename == "":
            return render_template("web_app.html", message="No selected file")
        if file:
            filename = secure_filename(file.filename)
            file_path = os.path.join("/path/to/the/uploads", filename)
            file.save(file_path)
            # Prediction function from your ML model
            # prediction = predict_image(file_path)
            return render_template(
                # "web_app.html", message="Successfully processed", prediction=prediction
                "web_app.html", message="Successfully processed"
            )
    return render_template("web_app.html")


if __name__ == "__main__":
    app.run(debug=True)
