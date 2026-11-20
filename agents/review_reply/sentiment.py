import re

POSITIVE_WORDS = {
    "good", "great", "amazing", "excellent", "delicious", "tasty",
    "friendly", "clean", "best", "love", "loved", "perfect", "nice",
    "fast", "helpful", "awesome", "wonderful", "fresh",
    "lazeez", "zabardast", "behtareen", "shukriya", "acha", "achha",
    "umda", "mazedar",
}

NEGATIVE_WORDS = {
    "bad", "worst", "slow", "cold", "rude", "dirty", "terrible",
    "awful", "poor", "late", "expensive", "stale", "horrible",
    "disappointed", "disappointing", "waste",
    "bekar", "ganda", "mehnga", "dair", "bura", "kharab",
}

NEGATIVE_PHRASES = [
    "not good", "not happy", "not fresh", "not clean", "not tasty",
    "never again", "bilkul acha nahi", "acha nahi", "achha nahi",
]


# EXTRA words
POSITIVE_WORDS |= {"superb", "fantastic", "outstanding", "enjoyed", "yummy", "recommended", "shandar", "lajawab", "kamal", "mast", "pasandida"}
NEGATIVE_WORDS |= {"disgusting", "horrible", "terrible", "filthy", "overpriced", "unhygienic", "tasteless", "overrated", "bakwas", "kharab"}
NEGATIVE_PHRASES += ["not recommended", "dont recommend", "do not recommend", "not worth", "shame on you", "nothing special", "not satisfied", "not impressed", "never going back", "wasnt good", "wasnt that good", "bilkul bekar", "theek nahi", "thik nahi", "pasand nahi", "maza nahi"]


def detect_sentiment(review):
    text = review.lower()

    neg_score = 0
    for phrase in NEGATIVE_PHRASES:
        if phrase in text:
            neg_score += 1
            text = text.replace(phrase, " ")

    words = re.findall(r"[a-z]+", text)
    pos_score = sum(1 for w in words if w in POSITIVE_WORDS)
    neg_score += sum(1 for w in words if w in NEGATIVE_WORDS)

    if neg_score > pos_score:
        return "negative"
    if pos_score > neg_score:
        return "positive"
    return "neutral"


if __name__ == "__main__":
    test_reviews = [
        "Food was amazing, staff very friendly",
        "Service was very slow and the food was cold",
        "Not good, waiter was rude",
        "Khana bohat lazeez tha, shukriya",
        "Place is on the main road",
    ]
    for r in test_reviews:
        print(detect_sentiment(r), "<-", r)
