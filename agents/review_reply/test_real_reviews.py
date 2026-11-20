"""Asli Google reviews par detect_sentiment ka test.
Sirf review ka matn, reviewers ke naam nahi.
Sahi labels insani nazar se likhe gaye hain."""

import os
import sys

# Is file ke folder ko path mein daalo taake sentiment.py import ho sake
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from sentiment import detect_sentiment

# (review ka matn, sahi label)
TEST_CASES = [
    (
        "I have no words, just because its in Hyderabad they dont even try to "
        "provide an adequate experience of taste let alone the customer service . "
        "not recommended at all sadly. The manchurian tasted as if they were "
        "giving it for free . Shame on you. Lamoosh team and chef.",
        "negative",
    ),
    (
        "I recently visited the Hyderabad branch of Ridan House of Mandi with my "
        "family, and it was a truly wonderful dining experience. The variety of "
        "dishes and the exceptional taste stood out, and the generous portion "
        "sizes make it excellent value for money. The dining area is clean and "
        "well maintained, which added to the comfort of our meal. However, the "
        "atmosphere could benefit from some improvement. While the setup suits "
        "the location, the space felt a bit congested at times. Enhancing the "
        "ambiance would elevate the overall experience even further. Overall, "
        "Ridan House of Mandi delivers on flavor, quality, and value - a great "
        "choice for family dining in Hyderabad.",
        "positive",
    ),
    (
        "Nothing Special here, It very expensive compared to other Restaurants "
        "here in Hyderabad, Atmosphere wasnt that good, Cleanness was about 5/10, "
        "In short it is Expensive for no reason. Food Quality Not Worth the Price.",
        "negative",
    ),
    (
        "we 3 friends came here for the 1st time and our experience went great! "
        "We heard good reviews of this place that's why visited to celebrate "
        "birthday and honestly found it a good place.",
        "positive",
    ),
    (
        "Disappointed by the service. Food served was cold and didn't reflect "
        "that it was prepared after the order. The restaurant manager lacks "
        "public dealing and didn't behave the way he was supposed to do . "
        "Food taste and ambience was good.",
        "negative",
    ),
]


def main():
    wrong = []
    for number, (review, expected) in enumerate(TEST_CASES, start=1):
        got = detect_sentiment(review)
        ok = got == expected
        mark = "OK  " if ok else "GHALAT"
        print(f"{number}. {mark} | sahi: {expected} | tool ne diya: {got}")
        if not ok:
            wrong.append((number, review, expected, got))

    total = len(TEST_CASES)
    correct = total - len(wrong)
    print()
    print(f"Natija: {correct}/{total} sahi")

    if wrong:
        print()
        print("Ghalat pehchane gaye reviews:")
        for number, review, expected, got in wrong:
            print(f"  #{number}: sahi={expected}, tool={got}")
            print(f"     {review[:90]}...")


if __name__ == "__main__":
    main()
