from analyzer.ats import calculate_ats_score
from flask import Flask, render_template, request
from analyzer.parser import extract_text
from analyzer.score import calculate_resume_score
import os

app = Flask(__name__)

# Upload Folder
UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# Create Upload Folder if it doesn't exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/analyze", methods=["POST"])
def analyze():

    if "resume" not in request.files:
        return "No Resume Uploaded."

    file = request.files["resume"]

    if file.filename == "":
        return "No File Selected."

    role = request.form.get("role")

    # Save uploaded file
    filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
    file.save(filepath)

    try:

        # Extract Resume Text
        resume_text = extract_text(filepath)

        # Calculate Resume Score
        score, feedback = calculate_resume_score(resume_text)

        ats_score, matched_skills, missing_skills = calculate_ats_score(
            resume_text,
            role
        )

    except Exception as e:

        print(e)

        resume_text = ""

        score = 0

        feedback = ["Unable to analyze resume."]

        ats_score = 0
        matched_skills = []
        missing_skills = []

    return render_template(
        "dashboard.html",
        filename=file.filename,
        role=role,
        resume_text=resume_text,
        score=score,
        feedback=feedback,
        ats_score=ats_score,
        matched_skills=matched_skills,
        missing_skills=missing_skills
    )


if __name__ == "__main__":
    app.run(debug=True)