import os

FOLDER = os.path.join(os.path.dirname(__file__), "output")
DRAFTS = os.path.join(FOLDER, "reply_drafts.md")
APPROVED = os.path.join(FOLDER, "approved_replies.md")


def load_drafts():
    with open(DRAFTS, "r", encoding="utf-8") as f:
        text = f.read()
    blocks = [b.strip() for b in text.split("## Review") if b.strip()]
    return ["## Review" + b for b in blocks]


def load_approved():
    if not os.path.exists(APPROVED):
        return ""
    with open(APPROVED, "r", encoding="utf-8") as f:
        return f.read()


if __name__ == "__main__":
    if not os.path.exists(DRAFTS):
        print("Pehle reply_maker.py chalayein, abhi koi draft nahi hai.")
        raise SystemExit

    drafts = load_drafts()
    already = load_approved()
    approved_count = 0

    for number, draft in enumerate(drafts, start=1):
        if draft.replace('Status: DRAFT, approval pending', 'Status: APPROVED') in already:
            continue
        print("=" * 50)
        print(f"Draft {number} of {len(drafts)}")
        print(draft)
        choice = input("Manzoor? y = haan, n = nahi, s = baad mein, q = band: ").strip().lower()
        if choice == "q":
            break
        if choice == "y":
            with open(APPROVED, "a", encoding="utf-8") as f:
                f.write(draft.replace('Status: DRAFT, approval pending', 'Status: APPROVED') + "\n\n")
            approved_count += 1
            print("Manzoor ho gaya.")
        elif choice == "n":
            print("Radd kar diya.")
        else:
            print("Baad ke liye chhor diya.")

    print(f"\nIs baar {approved_count} draft manzoor hue.")
    print("Note: koi message bheja nahi gaya. Bhejna aap khud karenge.")
