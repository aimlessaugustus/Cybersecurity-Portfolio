"""A script to generate potential passwords according to Marco's rules."""

# The company keywords.
KEYWORDS = ["innovation", "excellence", "security",
            "digital", "cloud", "future", "talent"]
YEARS = range(1990, 2030)
OUTPUT_FILE = "phrases.txt"


def generate_phrases():
    """Return phrases in the form: CapitalizedKeyword + number + !"""
    return [
        f"{keyword.capitalize()}{number}!"
        for keyword in KEYWORDS
        for number in YEARS
    ]


if __name__ == "__main__":
    with open(OUTPUT_FILE, "w", encoding="utf-8") as output:
        output.write("\n".join(generate_phrases()))
        if KEYWORDS:
            output.write("\n")
