import os
from sentiment import detect_sentiment

TEMPLATES = {
    "positive": [
        "Thank you so much for your kind words! The whole team at {name} is delighted you enjoyed your visit. We look forward to welcoming you again soon.",
        "We really appreciate your wonderful feedback. Comments like yours motivate the {name} team every day. See you again soon!",
        "Thank you for taking the time to share this! We are so glad you had a great experience at {name}.",
        "Your support means a lot to us. Thank you for choosing {name}, and we hope to serve you again very soon.",
        "What a lovely review, thank you! We will share it with our team. Hope to see you again at {name}.",
    ],
    "negative": [
        "We are sorry your experience at {name} did not meet your expectations. Your feedback matters to us. Please contact us directly so we can look into this and make it right.",
        "Thank you for telling us about this, and we sincerely apologize. We are reviewing what happened with our team. Please reach out to us so we can resolve it for you.",
        "We apologize for the disappointment. This is not the standard we want at {name}. We would like to hear more details so we can improve and make things right.",
        "We are truly sorry for the trouble you faced. Your comments help us improve. Please contact the {name} team directly so we can address your concern personally.",
        "Thank you for your honest feedback. We are sorry we let you down this time. We would value a chance to put things right, so please get in touch with us.",
    ],
    "neutral": [
        "Thank you for your feedback about {name}. If there is anything we can do to make your next visit better, please let us know.",
        "Thanks for visiting {name} and sharing your thoughts. We are always working to improve and hope to see you again.",
        "We appreciate you taking the time to review us. Your feedback helps {name} get better every day.",
    ],
}


def make_reply(business_name, review):
    sentiment = detect_sentiment(review)
    options = TEMPLATES[sentiment]
    reply = options[len(review) % len(options)].format(name=business_name)
    return sentiment, reply


def save_draft(business_name, review, sentiment, reply):
    folder = os.path.join(os.path.dirname(__file__), "output")
    os.makedirs(folder, exist_ok=True)
    path = os.path.join(folder, "reply_drafts.md")
    with open(path, "a", encoding="utf-8") as f:
        f.write(f"## Review ({sentiment})\n")
        f.write(f"- Business: {business_name}\n")
        f.write(f"- Review: {review}\n")
        f.write(f"- Draft reply: {reply}\n")
        f.write("- Status: DRAFT, approval pending\n\n")
    return path


if __name__ == "__main__":
    business = input("Business ka naam: ")
    print("Review paste karein. Khatam karne ke liye khali line dabayein.")
    while True:
        review = input("Review: ").strip()
        if not review:
            break
        sentiment, reply = make_reply(business, review)
        save_draft(business, review, sentiment, reply)
        print(f"[{sentiment}] {reply}\n")
    print("Drafts save ho gaye: agents/review_reply/output/reply_drafts.md")
