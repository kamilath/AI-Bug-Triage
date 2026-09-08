from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def find_duplicate(title, description, bugs):
    text = title + " " + description

    if not bugs:
        return None, 0

    old = [
        bug["title"] + " " + bug["description"]
        for bug in bugs
    ]

    data = old + [text]

    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform(data)

    scores = cosine_similarity(vectors[-1], vectors[:-1])[0]

    index = scores.argmax()
    score = scores[index]

    if score >= 0.7:
        return bugs[index], score

    return None, score