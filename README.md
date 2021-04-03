# hangmanAI
#### little hangman bot inspired by conditional probabilities

## Summary 
Inspired by conditional probabilities, the idea is to pick the optimal character by max(p(char | len(word) & known characters for positions)).
So, given a list of common english words, for each word that is of the same length as the word being searched for, and that has the characters guessed so far in the correct positioons, then we can guess the highest frequency character, which is the maximum probability character.

### Example Results
![image](https://user-images.githubusercontent.com/26100016/113494093-2c0f3280-949a-11eb-8045-48f0d5419af2.png)

