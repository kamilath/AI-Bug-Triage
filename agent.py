import json
from analyzer import analyze_bug
from duplicate import find_duplicate
from test_generator import generate_test_cases, generate_regression


def load_bugs():
    try:
        with open("data/bugs.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def process_bug(title, description):
    result = analyze_bug(title, description)

    bugs = load_bugs()

    duplicate, score = find_duplicate(
        title,
        description,
        bugs
    )

    result["title"] = title
    result["description"] = description
    result["duplicate"] = duplicate
    result["duplicate_score"] = round(float(score), 2)

    result["test_cases"] = generate_test_cases(
        title,
        description,
        result["component"]
    )

    result["regression_tests"] = generate_regression(
        result["component"]
    )

    return result