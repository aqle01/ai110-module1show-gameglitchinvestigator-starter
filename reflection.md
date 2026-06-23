# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?

The settings were on the left, and the main game area had clearly separated sections for entering guesses, viewing hints, and starting a new game. 

It does give a certain Notion page vibe but otherwise I think it looked clean and simple, easy to navigate with white background and colors that are not overwhelming.

- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

1) When I tried guessing 1 or any negative number it said to go lower, which should not be allowed since we're just guessing a number between 1 and 100. The answer always turns out to be a number between 1-100.
2) It says "Press Enter to apply" but that didn't seem to work.
3) Once I tried guessing 54 and it said to go higher, then I tried guessing 13 and was told to go lower, which is technically not possible to satisfy.
4) The "New Game" button doesn't seem to work correctly. It does lead to the number of attempts left being reset to 8 but the game doesn't really work anymore when I click "Submit Guess".

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
|12 |          | 📉 Go LOWER!|none|
|10 |          | 📉 Go LOWER!|none|
| 1 |Go HIGHER!| 📉 Go LOWER!|none|
|-2 |Error     | 📉 Go LOWER!|none|
---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
I used Claude and ChatGPT on this project

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).

When I described the backwards hints, Claude pinpointed that in `check_guess` the two hint messages were swapped: a guess above the secret returned "📈 Go HIGHER!" when it should have said "📉 Go LOWER!", and vice versa. It suggested refactoring the logic out of `app.py` into `logic_utils.py` and correcting the messages. I verified the fix two ways: I called `check_guess(1, 50)` and `check_guess(90, 50)` directly and saw "Go HIGHER!" and "Go LOWER!" respectively, and I ran `pytest tests/ -v`, which reported 5 passed. The behavior also matched the game when I reran it, so I trusted the suggestion was correct.

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

The AI-generated starter tests were misleading. They asserted things like `check_guess(60, 50) == "Too High"`, but `check_guess` actually returns a tuple such as `("Too High", "📉 Go LOWER!")`, so the assertion didn't even match the real return type. More importantly, those tests only checked the outcome label and never the hint message, which meant they would have "passed" even while the reversed-hint bug was still present. I caught this by reading what the tests actually compared, and I verified it by writing new tests that check the message direction (`test_too_low_guess_hint_says_go_higher` / `test_too_high_guess_hint_says_go_lower`) — those are the ones that actually fail if the bug returns.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?

I decided a bug was fixed when the behavior matched the rules of the game for inputs where I already knew the right answer. For the high/low bug I used cases like guess 1 vs secret 50 (which should say "Go HIGHER!"), checked both the function's return value and the running app and only counted it as fixed when both agreed.

- Describe at least one test you ran (manual or using pytest) and what it showed you about your code.

I ran `pytest tests/ -v` and added two regression tests, `test_too_low_guess_hint_says_go_higher` and `test_too_high_guess_hint_says_go_lower`, which assert that the hint message contains "HIGHER" / "LOWER" in the right direction. They showed me that the outcome label ("Too High" / "Too Low") had always been correct and that only the message direction was broken so a test that checked just the label (like the original ones) would have hidden the bug entirely. All 5 tests passed after the fix.

- Did AI help you design or understand any tests? How?

Yes. Claude pointed out that the starter tests only checked the outcome label and compared against a plain string instead of the tuple the function actually returns, so they could never catch the reversed-hint bug. It helped me rewrite those tests to unpack the tuple (and write assertions) and understand why testing the user-facing message is what actually protects against this kind of bug.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
