def generate_feedback(score, ats_score, missing_skills):

    feedback = []

    # Resume Score
    if score >= 85:
        feedback.append("Excellent resume structure.")
    elif score >= 70:
        feedback.append("Good resume, but there is room for improvement.")
    else:
        feedback.append("Improve the resume structure and add more details.")

    # ATS Score
    if ats_score >= 80:
        feedback.append("Your resume is highly ATS-friendly.")
    elif ats_score >= 60:
        feedback.append("Your resume has a decent ATS score.")
    else:
        feedback.append("Your ATS score is low. Add more job-specific skills.")

    # Missing Skills
    if missing_skills:
        feedback.append(
            "Consider learning: " + ", ".join(missing_skills)
        )

    # Resume Tips
    feedback.append("Keep your resume to one page.")
    feedback.append("Use action verbs such as Developed, Built, Designed.")
    feedback.append("Quantify achievements whenever possible.")
    feedback.append("Keep your GitHub and LinkedIn profiles updated.")

    return feedback