import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from sentiment import detect_sentiment

CASES = [
    ("Khana bohat acha tha, service bhi zabardast", "positive"),
    ("Khana bilkul acha nahi tha, bohat mehnga", "negative"),
    ("Biryani lazeez thi lekin service bohat slow thi", "neutral"),
    ("Khana theek tha", "neutral"),
    ("Staff bohat rude tha, dobara kabhi nahi aunga", "negative"),
    ("Mazedar khana, shukriya", "positive"),
    ("Place main road par hai", "neutral"),
    ("Food great tha lekin wait bohat zyada", "neutral"),
]

wrong = 0
for i, (text, expected) in enumerate(CASES, 1):
    got = detect_sentiment(text)
    ok = got == expected
    wrong += 0 if ok else 1
    print(i, "OK   " if ok else "GHALAT", "sahi:", expected, "| tool:", got, "|", text)
print("Natija:", len(CASES) - wrong, "/", len(CASES), "sahi")
