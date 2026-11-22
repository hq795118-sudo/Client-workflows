import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from sentiment import detect_sentiment

CASES = [
    ("Very disappointing dining experience. We had a really bad experience. "
     "By the time we started eating the main course, nothing was hot. "
     "The accompanying salad had a spoiled lemon. The food was so pathetic "
     "in taste and quality that I couldn't even finish my roti and curry. "
     "Overly salty and completely inedible.", "negative"),
    ("Undercooked Chicken is being served here. Blood comes out of chicken.. "
     "service is pathetic, staff is rude. The chef does not even agrees that "
     "it's bad food. Don't go.", "negative"),
    ("Excellent experience. The staff is very well trained and ready to "
     "welcome you perfectly. There is huge car parking with the valet "
     "service. The food quality and taste is excellent.", "positive"),
    ("Haidri hotel is one of the simplest hotel in Qasimabad. Service is "
     "fast and the rates are lower as compared to others.", "positive"),
    ("A wonderful place for fast-food lovers, offering delicious food with "
     "excellent quality and appealing taste. Highly recommended for "
     "fast-food lovers.", "positive"),
]

wrong = 0
for i, (text, expected) in enumerate(CASES, 1):
    got = detect_sentiment(text)
    ok = got == expected
    wrong += 0 if ok else 1
    print(i, "OK   " if ok else "GHALAT", "sahi:", expected, "| tool:", got)
print("Natija:", len(CASES) - wrong, "/", len(CASES), "sahi")
