# Caesar Cipher in Python
In this code challenge we are implementing the famous Caesar cipher used to send messages without a third-party being able to read them. 

## Problem
Implement a Caesar cipher, both encoding and decoding. The key is an integer from 1 to 25. This cipher rotates the letters of the alphabet (A to Z). The encoding replaces each letter with the 1st to 25th next letter in the alphabet (wrapping Z to A). So key 2 encrypts “HI” to “JK”, but key 20 encrypts “HI” to “BC”.

## Solution
The caesar cipher is a substitution cipher; a cipher where each letter in the alphabet is replaced with another.
This makes understanding the cipher quite easy.

### Caesar Cipher Explanation
We have 26 letters in the alphabet. 
When we "shift" the letters along the order of the letters change.
In our cipher, we replace any letters in the previous position with the letters in the shifted position.
We can use the sentence `THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG` to show this.
```python
Alphabet: A B C D E G F H I J K L M N O P Q R S T U V W X Y Z
Text: THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG
Shift all letters by 1
New alphabet: Z A B C D E G F H I J K L M N O P Q R S T U V W X Y
Text: UIF RVJDL CSPXO GPY KVNQT PWFS UIF MBAZ EPH
```
Look how unreadable the text has become after simply replacing the letters with the next letter in the alphabet!
Decoding the encoded text back into plaintext is simple: we apply the cipher in the opposite direction.
So for example, if we encode "APPLE" to "KZZVO" (shifting 10 places) we can turn "KZZVO" back to "APPLE" by shifting -10 places.

Read more:
- [Wikipedia page on the Caesar Cipher](https://en.wikipedia.org/wiki/Caesar_cipher)
- [Online Caesar Cipher converter](https://cryptii.com/pipes/caesar-cipher)

## Python Solution Explained

```python
# define the data we need: alphabet, text, shift amount.
alphabet = "abcdefghijklmnopqrstuvwxyz"
# .lower() is used to convert the text into only lower text as our alphabet only has lowercase letters.
text = input("Please enter your text: ").lower()
# make sure to use int() so our shift is a number not a string.
shift_amount = int(input("Please enter the shift amount: ")) 
```
```python
# This is very similar to the pseudocode example .
new_text = ""
for letter in text:
    if letter in alphabet:
        # We shift the letter only if it is in the alphabet.
        index = alphabet.index(letter)
        index += shift_amount
        index %= 26
        new_text += alphabet[index]
    else:
        # Just add any numbers/symbols/etc onto the encoded text .
        new_text += letter
```
```
# Show the difference between the original and encoded text.
print(f"\"{text}\" has been encoded to \"{new_text}\"")
```