# hangmanAI
#### little hangman bot inspired by conditional probabilities

## Summary 
Inspired by conditional probabilities, idea is to pick the optimal character by max(p(char | len(word) & known characters)).
So, given a list of common english words, for each word that is of the same length as the word being searched for, and that has the characters we've correctly guessed so far, count the number occurences of each character. Then we can return the maximally occuring character as the highest probability character. 

Unfortunately the results are not good! Which is kind of interesting... I initially thought this was because my word dictionary had too many obscure words, including names, and words that just don't show up in a normal dictionary. I replaced my list with a list of popular english words, but performance didn't improve much. 

### Example Results
![sample result image](https://user-images.githubusercontent.com/26100016/102803121-9decc180-436c-11eb-9aa7-765fc80e8181.png)
