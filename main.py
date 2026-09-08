import json
import sys
from agent import process_bug


def read_bugs(path):
    with open(path, "r", encoding="utf-8") as file:
        text = file.read()

    return [x.strip() for x in text.split("===") if x.strip()]


def main():
    if len(sys.argv) < 3:
        print("Usage: python main.py --file <file>")
        return

    path = sys.argv[2]

    reports = read_bugs(path)

    bugs = []

    for report in reports:
        process_bug(report, bugs)

    order = {
        "Critical": 1,
        "High": 2,
        "Medium": 3,
        "Low": 4
    }

    bugs.sort(key=lambda x: order[x["severity"]])

    print(json.dumps(bugs, indent=4))


if __name__ == "__main__":
    main()