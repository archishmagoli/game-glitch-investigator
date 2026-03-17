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

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
