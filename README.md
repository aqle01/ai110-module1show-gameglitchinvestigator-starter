# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [x] **Describe the game's purpose.** It's a Streamlit number-guessing game. The app picks a secret number within a range that depends on the chosen difficulty (Easy 1–20, Normal 1–100, Hard 1–50), and the player guesses numbers within a limited number of attempts. After each guess the game gives a "higher / lower" hint and updates a score, ending when the player guesses correctly or runs out of attempts.

- [x] **Detail which bugs you found.**
  - The high/low hints were reversed — a guess that was too low told you to "Go LOWER" and vice versa, so the game was unwinnable by following the hints.
  - The hints could be self-contradictory (e.g. one guess says "go higher", a lower guess says "go lower") because the secret was being compared as a string on every other attempt.
  - The "New Game" button reset the attempt counter but the game stopped responding to "Submit Guess".
  - The text box shows "Press Enter to apply" but pressing Enter doesn't actually submit a guess.

- [x] **Explain what fixes you applied.**
  - Fixed the reversed hint logic in `check_guess` so "Too High" → Go LOWER and "Too Low" → Go HIGHER.
  - Refactored the core logic (`get_range_for_difficulty`, `parse_guess`, `check_guess`, `update_score`) out of `app.py` into `logic_utils.py`, separating game logic from the Streamlit UI.
  - Added pytest regression tests that check the hint message direction (not just the outcome label).
  - **Still open** (marked with `# FIXME` in the code): the "New Game" reset bug and the every-other-attempt string-comparison bug, which still causes wrong hints for edge cases like single-digit or negative guesses.

## Demo Walkthrough

A text-based run-through of a sample game on **Normal** difficulty (range 1–100). For this example the secret number is **50** (you can confirm it via the "Developer Debug Info" expander in the app).

1. The app loads with the title, the difficulty selector set to **Normal**, an empty guess box, and **"Attempts left: 7"**.
2. The user enters a guess of **40** and clicks **Submit Guess** → the game returns **Too Low** with the hint **"📈 Go HIGHER!"** (the corrected direction — 40 is below 50).
3. The user enters a guess of **70** and clicks **Submit Guess** → the game returns **Too High** with the hint **"📉 Go LOWER!"** (70 is above 50).
4. The score updates after each guess (each wrong guess applies a small penalty) and **"Attempts left"** counts down by one each time.
5. The user enters a guess of **50** and clicks **Submit Guess** → the game shows **"🎉 Correct!"**, plays the balloon animation, awards a win bonus based on how few attempts were used, and ends the round with **"You won! The secret was 50."**

This gives a clear, end-to-end record of how the fixed game behaves that anyone can follow without running it.

## 🧪 Test Results

```
$ python -m pytest tests/ -v
============================= test session starts =============================
platform win32 -- Python 3.13.1, pytest-9.1.1, pluggy-1.6.0
collected 5 items

tests/test_game_logic.py::test_winning_guess PASSED                      [ 20%]
tests/test_game_logic.py::test_guess_too_high PASSED                     [ 40%]
tests/test_game_logic.py::test_guess_too_low PASSED                      [ 60%]
tests/test_game_logic.py::test_too_low_guess_hint_says_go_higher PASSED  [ 80%]
tests/test_game_logic.py::test_too_high_guess_hint_says_go_lower PASSED  [100%]

============================== 5 passed in 0.02s ==============================
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
