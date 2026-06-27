SKILL_ALIASES = {
    "python": ["python", "python3"],
    "machine learning": ["machine learning", "ml"],
    "tensorflow": ["tensorflow", "tensor flow"],
    "pytorch": ["pytorch", "torch"],
    "opencv": ["opencv", "open cv"],
    "sql": ["sql", "mysql", "postgresql"],
    "flask": ["flask"],
    "git": ["git", "github"],
    "numpy": ["numpy"],
    "pandas": ["pandas"],

    "html": ["html", "html5"],
    "css": ["css", "css3"],
    "javascript": ["javascript", "js"],
    "react": ["react", "reactjs"],
    "node": ["node", "nodejs", "node.js"],
    "express": ["express", "expressjs"],
    "mongodb": ["mongodb", "mongo"],

    "excel": ["excel", "ms excel"],
    "power bi": ["power bi", "powerbi"],
    "tableau": ["tableau"],
    "matplotlib": ["matplotlib"],

    "aws": ["aws", "amazon web services"],
    "azure": ["azure", "microsoft azure"],
    "docker": ["docker", "container"],
    "kubernetes": ["kubernetes", "k8s"],
    "linux": ["linux", "ubuntu"]
}


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

    matched = set()

    missing = []

    for skill in required_skills:

        aliases = SKILL_ALIASES.get(skill, [skill])

        found = False

        for alias in aliases:

            if alias.lower() in text:

                matched.add(skill)

                found = True

                break

        if not found:

            missing.append(skill)

    if len(required_skills) == 0:

        score = 0

    else:

        score = int((len(matched) / len(required_skills)) * 100)

    return score, sorted(list(matched)), missing