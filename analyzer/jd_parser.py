import re

STOP_WORDS = {
    "the", "and", "for", "with", "your", "you", "our",
    "will", "are", "this", "that", "from", "have",
    "has", "into", "their", "they", "must", "should",
    "required", "requirements", "experience", "years",
    "year", "candidate", "work", "job", "role", "team"
}


def extract_keywords(job_description):

    if not job_description:
        return []

    text = job_description.lower()

    words = re.findall(r"[a-zA-Z0-9.+#]+", text)

    keywords = []

    for word in words:

        if len(word) > 2 and word not in STOP_WORDS:

            keywords.append(word)

    return list(set(keywords))