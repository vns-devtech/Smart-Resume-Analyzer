JOB_SKILLS = {

    "AI Engineer": [
        "python",
        "machine learning",
        "tensorflow",
        "pytorch",
        "opencv",
        "sql",
        "flask",
        "git",
        "numpy",
        "pandas"
    ],

    "Web Developer": [
        "html",
        "css",
        "javascript",
        "react",
        "node",
        "express",
        "mongodb",
        "sql",
        "git"
    ],

    "Data Analyst": [
        "python",
        "sql",
        "excel",
        "power bi",
        "tableau",
        "numpy",
        "pandas",
        "matplotlib"
    ],

    "Cloud Engineer": [
        "aws",
        "azure",
        "docker",
        "kubernetes",
        "linux",
        "git",
        "python"
    ]
}


def calculate_ats_score(text, role):

    text = text.lower()

    required_skills = JOB_SKILLS.get(role, [])

    matched = []

    missing = []

    for skill in required_skills:

        if skill.lower() in text:

            matched.append(skill)

        else:

            missing.append(skill)

    if len(required_skills) == 0:

        score = 0

    else:

        score = int((len(matched) / len(required_skills)) * 100)

    return score, matched, missing