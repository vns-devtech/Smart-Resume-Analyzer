from flask import Flask, render_template, request
from analyzer.parser import extract_text
import os

app = Flask(__name__)

# Upload folder
UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# Create uploads folder if it doesn't exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/analyze", methods=["POST"])
def analyze():

    file = request.files["resume"]
    role = request.form["role"]

    # Save uploaded file
    filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
    file.save(filepath)

    resume_text = extract_text(filepath)

    return f"""
    <h1>Resume Uploaded Successfully 🎉</h1>

    <hr>

    <h2>File Name:</h2>
    <p>{file.filename}</p>

    <h2>Selected Role:</h2>
    <p>{role}</p>

    <hr>

    <h2>Extracted Resume Text</h2>

    <pre style="white-space:pre-wrap;
    font-size:16px;
    background:#f5f5f5;
    padding:20px;
    border-radius:10px;">
    {resume_text}
    </pre>

    <br>

    <a href="/">⬅ Upload Another Resume</a>
    """
    


if __name__ == "__main__":
    app.run(debug=True)