def get_range_for_difficulty(difficulty: str):
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 100
    if difficulty == "Hard":
        return 1, 50
    return 1, 100


def parse_guess(raw: str):
    if raw is None:
        return False, None, "Enter a guess."

    if raw == "":
        return False, None, "Enter a guess."

    try:
        if "," in raw:
            raw = raw.replace(",", "")
            value = int(raw)
        if "." in raw:
            value = int(float(raw))
        else:
            value = int(raw)
    except Exception:
        return False, None, "That is not a number."

    return True, value, None



def check_guess(guess, secret):
    try:
        guess = int(guess)
        secret = int(secret)
    except (ValueError, TypeError):
        return "Invalid"

    if guess == secret:
        return "Win"
    elif guess > secret:
        return "Too High"
    else:
        return "Too Low"




