def calculate_resume_score(text):

    score = 0

    feedback = []

    text = text.lower()

    # Email
    if "@" in text:
        score += 10
    else:
        feedback.append("Add an Email Address.")

    # Phone
    if any(ch.isdigit() for ch in text):
        score += 10
    else:
        feedback.append("Add a Phone Number.")

    # Education
    education = [
        "b.tech",
        "bachelor",
        "college",
        "university",
        "bba",
        "mca"
    ]

    if any(word in text for word in education):
        score += 15
    else:
        feedback.append("Education Section Missing.")

    # Skills
    skills = [
        "python",
        "java",
        "c++",
        "sql",
        "html",
        "css",
        "javascript",
        "flask",
        "machine learning"
    ]

    found = 0

    for skill in skills:
        if skill in text:
            found += 1

    score += min(found * 3, 20)

    if found < 3:
        feedback.append("Add More Technical Skills.")

    # Projects
    if "project" in text:
        score += 20
    else:
        feedback.append("Projects Section Missing.")

    # Experience
    if "experience" in text or "internship" in text:
        score += 15
    else:
        feedback.append("Add Internship Experience.")

    # Certification
    if "certificate" in text or "certification" in text:
        score += 10
    else:
        feedback.append("Add Certifications.")

    return score, feedback