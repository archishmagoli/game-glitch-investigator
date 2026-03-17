# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

- **There are three difficulty modes (Easy, Medium, Hard) that have different guessing ranges, but the game always prints out "Guess a number between 1 and 100."**
- **The "Normal" and "Hard" ranges in `get_range_for_difficulty` are swapped - the harder the level, the bigger the range should be, but "Normal" mode has a larger guessing range than "Hard" mode.**
- **Similarly, the "Easy" and "Normal" attempts in `attempt_limit_map` are swapped: the easier the level, the more attempts the user should  have.**
- **The hints are swapped: if we guess a higher number, we should output "LOWER," and if we guess a lower number, we should output "HIGHER." Currently we are outputting the opposite.**
- **If our guess is too high, BUT it's an even number, we actually ADD 5 to the score instead of subtracting 5 in `update_score`. We should always subtract from the total score if our guess is wrong.**

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)? **I used Copilot for this project - more specifically, I used Agent Mode to make the fixes and move the relevant logic into `logic_utils.py`.**
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result). **The first bug I mentioned (regarding the ranges per difficulty mode) was an AI suggestion that was correctly identified as a bug.**
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result). **The AI suggested that the `history` list having different types was "misleading," but I thought the logic there was sound. After manual inspection, I see that we are appending any guess we get to the `history` list, which makes sense.**

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed? **I first ensured that Agent Mode actually fixed the bug properly by manually inspecting the code. Sometimes, the fix did not propagate, so I re-factored the prompts I used to be more specific.**
- Describe at least one test you ran (manual or using pytest) 
  and what it showed you about your code. **I refactored the existing `test_guess_too_high` and `test_guess_too_low` test cases in `test_game_logic.py` by adding two new `assert` messages to verify the "HIGHER"/"LOWER" suggestions. Initially, we were only testing the `result` ("Too High" or "Too Low"), so I made the test cases more robust. These tests helped me ensure that the user was getting the correct direction to make their next guess when the first guess was wrong.**
- Did AI help you design or understand any tests? How? **I saw that `update_score` had a bug in it such that the guessing the number correctly on the first attempt resulted in a deduction in the score. Once Agent Mode made the fix I instructed, I used AI to generate test cases with different accumulated attempt numbers to ensure the score was being deducted properly. Fortunately, the generated test cases looked great on the first try!**

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
**A "rerun" in Streamlit happens every time you interact with the application (e.g. clicking "Submit Guess", entering a number in the text box). In a rerun, the entire application script restarts and runs from top to bottom. You must make sure to save variables you want persisted in `st.session_state`, which is a special dictionary that keeps track of scores, guesses, and use progress even as the script restarts.**

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git. **I realized I need to be really specific in my prompts to AI. I can't just say "fix this bug," I need to specify what the bug is, how to fix it, along with which file I'm looking at.**
- What is one thing you would do differently next time you work with AI on a coding task?  **I would update my prompts to be more detailed AND ask AI to generate tests at the SAME time Agent Mode fixes a bug.**
- In one or two sentences, describe how this project changed the way you think about AI generated code. **I think AI-generated code is really model-dependent. I'm currently using Copilot's `Auto` mode, in which the model is being picked for me; I think directly using Claude would have been a better approach - I'll make sure to do this next time.**
