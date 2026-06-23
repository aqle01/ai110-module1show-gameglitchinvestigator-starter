from logic_utils import check_guess

# check_guess returns a tuple: (outcome, message)
# e.g. ("Too Low", "📈 Go HIGHER!")


def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"


def test_guess_too_high():
    # If secret is 50 and guess is 60, outcome should be "Too High"
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"


def test_guess_too_low():
    # If secret is 50 and guess is 40, outcome should be "Too Low"
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"


# --- Regression tests for the high/low hint bug that was just fixed ---
# The bug: the hint messages were reversed. A guess that was too LOW told the
# player to "Go LOWER!", and a guess that was too HIGH told them to "Go HIGHER!"
# These tests target the message, not just the outcome label, because the
# outcome was already correct — only the direction of the hint was wrong.


def test_too_low_guess_hint_says_go_higher():
    # Guess (40) is below the secret (50) -> player must aim HIGHER.
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message.upper()
    assert "LOWER" not in message.upper()


def test_too_high_guess_hint_says_go_lower():
    # Guess (60) is above the secret (50) -> player must aim LOWER.
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert "LOWER" in message.upper()
    assert "HIGHER" not in message.upper()
