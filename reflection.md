# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
# aesthetically spreaking it looks funtional, nothing flashy.
# from the initial look it seemed to be runing fine untill you start to put in the values.
# then you can notice that the hints are missleading and can sometimes head you in the right direction, but most of the time it couldn't be trusted.

- List at least two concrete bugs you noticed at the start  
  # the first problem is that the new game button dose not reset the banner for the hint if you let the counter go to zero.
  # as a result, after the new game has started the player woul't have no clue in what direction to go in.
  # the second problem if you put a negative number the hint will always tell you to go lower.
  # this dose not make sense because with a negative the value is out of bounds

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
|1,000  |Go lower           | Not a Number    | none                   |
|-2     |Go Higher          | Go lower        | none                   |
| New Game |give a hint     |no hint given    |none                    |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
# ChatGBT,Cloude
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
# for the most part claude helped me fix the new game button i had gotten resting the history list and playing status. what i didnt know is that i needed put random.randint(low, high) instead of (1,100). thats where claued came in handy
- Give one example of an AI suggestion you did not accept as written (including what the AI suggested, why you rejected or changed it, and how you verified your version). It does not have to be a suggestion that was wrong: over-engineered, out of scope, harder to read, or a poor fit for this codebase all count.
# i asked claude to help me fix the check_guess funtion and all it did was cast the perameters to integers. then i asked chatGBT and it explaind where the logic was still alittle flawed



---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
# i ran alot of senarios manualy and ran the pytest
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
  # i was able to demonstate that it work by running negative numbers , numbers with commas, number close and far fron the secret number
- Did AI help you design or understand any tests? How?
# yes, eventhough it was passing the manual test it was still failing the pytest. and chatgbt helped clear up the output.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

# Every time a user clicks a button, moves a slider, or types into a text box, Streamlit reruns the entire Python script from the very first line to the last line. as a result,reruns make the app forgetful, you need a way to store information. That’s where Session State comes in, it gives the app shorterm memory.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
# testing wich Ai could give a more clear answer, as well as mentaly having a solution before hand.
  - This could be a testing habit, a prompting strategy, or a way you used Git.
# yes, this provides a whone new way to think of testing.
- What is one thing you would do differently next time you work with AI on a coding task?
# i wound think more carefully about my prompts
- In one or two sentences, describe how this project changed the way you think about AI generated code.
# i learned to code before ai got big and this was my introduction to it.
