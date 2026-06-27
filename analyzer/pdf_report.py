from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from datetime import datetime


def generate_pdf_report(filename, role, score, ats_score,
                        matched_skills, missing_skills,
                        ai_feedback):

    pdf_path = "reports/resume_report.pdf"

    doc = SimpleDocTemplate(pdf_path)

    styles = getSampleStyleSheet()

    story = []

    story.append(Paragraph("<b>SMART RESUME ANALYZER REPORT</b>", styles["Title"]))

    story.append(Paragraph(f"<b>Date:</b> {datetime.now()}", styles["Normal"]))
    story.append(Paragraph("<br/>", styles["Normal"]))

    story.append(Paragraph(f"<b>Uploaded File:</b> {filename}", styles["Normal"]))
    story.append(Paragraph(f"<b>Selected Role:</b> {role}", styles["Normal"]))
    story.append(Paragraph(f"<b>Resume Score:</b> {score}/100", styles["Normal"]))
    story.append(Paragraph(f"<b>ATS Score:</b> {ats_score}%", styles["Normal"]))

    story.append(Paragraph("<br/>", styles["Normal"]))

    story.append(Paragraph("<b>Matched Skills</b>", styles["Heading2"]))

    for skill in matched_skills:
        story.append(Paragraph(f"✔ {skill}", styles["Normal"]))

    story.append(Paragraph("<br/>", styles["Normal"]))

    story.append(Paragraph("<b>Missing Skills</b>", styles["Heading2"]))

    for skill in missing_skills:
        story.append(Paragraph(f"✘ {skill}", styles["Normal"]))

    story.append(Paragraph("<br/>", styles["Normal"]))

    story.append(Paragraph("<b>AI Feedback</b>", styles["Heading2"]))

    for item in ai_feedback:
        story.append(Paragraph(f"• {item}", styles["Normal"]))

    doc.build(story)

    return pdf_path