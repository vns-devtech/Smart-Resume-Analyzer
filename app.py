from analyzer.jd_parser import extract_keywords
from flask import Flask, render_template, request, send_file
from analyzer.parser import extract_text
from analyzer.score import calculate_resume_score
from analyzer.ats import calculate_ats_score
from analyzer.feedback import generate_feedback
from analyzer.pdf_report import generate_pdf_report
import os

app = Flask(__name__)

# Upload Folder
UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# Reports Folder
REPORT_FOLDER = "reports"

# Create folders if they don't exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(REPORT_FOLDER, exist_ok=True)


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

    job_description = request.form.get("job_description")

    # Save uploaded file
    filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
    file.save(filepath)

    try:

        # Extract Resume Text
        resume_text = extract_text(filepath)

        jd_keywords = extract_keywords(job_description)

        # Resume Score
        score, feedback = calculate_resume_score(resume_text)

        # ATS Score
        if job_description.strip():

            matched_skills = []
            missing_skills = []

            resume_lower = resume_text.lower()

            for keyword in jd_keywords:

                if keyword in resume_lower:

                    matched_skills.append(keyword)

                else:

                    missing_skills.append(keyword)

            if len(jd_keywords) > 0:

                ats_score = int((len(matched_skills) / len(jd_keywords)) * 100)

            else:

                ats_score = 0

        else:

            ats_score, matched_skills, missing_skills = calculate_ats_score(
            resume_text,
            role
            )



        # AI Feedback
        ai_feedback = generate_feedback(
            score,
            ats_score,
            missing_skills
        )

        # Generate PDF Report
        pdf_path = generate_pdf_report(
            file.filename,
            role,
            score,
            ats_score,
            matched_skills,
            missing_skills,
            ai_feedback
        )

    except Exception as e:

        print("ERROR:", e)

        resume_text = ""

        score = 0

        feedback = ["Unable to analyze the resume."]

        ats_score = 0

        matched_skills = []

        missing_skills = []

        ai_feedback = []

        pdf_path = None

    return render_template(
        "dashboard.html",
        filename=file.filename,
        role=role,
        resume_text=resume_text,
        score=score,
        feedback=feedback,
        ats_score=ats_score,
        matched_skills=matched_skills,
        missing_skills=missing_skills,
        ai_feedback=ai_feedback,
        pdf_path=pdf_path,
        job_description=job_description
    )


@app.route("/download-report")
def download_report():

    report_path = os.path.join("reports", "resume_report.pdf")

    if os.path.exists(report_path):
        return send_file(
            report_path,
            as_attachment=True
        )

    return "PDF Report not found."


if __name__ == "__main__":
    app.run(debug=True)