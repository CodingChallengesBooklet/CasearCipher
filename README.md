# Caesar Cipher
In this code challenge we are implementing the famous Caesar cipher used to send messages without a third-party being able to read them. 

![GitHub followers](https://img.shields.io/github/followers/hrszpuk?style=social)
![Twitter Follow](https://img.shields.io/twitter/follow/hrszpuk?style=social)
<br>
![GitHub language count](https://img.shields.io/github/languages/count/CodingChallengesBooklet/CasearCipher?style=for-the-badge)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/CodingChallengesBooklet/CasearCipher?style=for-the-badge)
![GitHub issues](https://img.shields.io/github/issues/CodingChallengesBooklet/CasearCipher?style=for-the-badge)
![GitHub last commit](https://img.shields.io/github/last-commit/CodingChallengesBooklet/CasearCipher?style=for-the-badge)
![GitHub branch checks state](https://img.shields.io/github/checks-status/CodingChallengesBooklet/CasearCipher/main?style=for-the-badge)

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

### Pseudo code solution
To get started, the code here is written in pseudocode which isn't a programming language, but a language that is simple 
and easy to read, so anyone can read it and understand the logic behind the code. 
After understanding the logic implementing your own version of the code in your preferred programming language becomes easier.

First off, we declare a few variables: alphabet, which is a list containing all the letters in the alphabet.
We also get the text the user wants encoding, and the shift amount which is the amount of letters we will shift each letter.
```python
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
text = INPUT
shift_amount = INPUT
```

Next it's time to actually encode the text.
We define `new_text` which will store the encoded text.
For each letter in text we do the following:
1. Get the index of that letter in the alphabet (e.g. a is 1, b is 2, c is 3, ...etc)
2. We add the `shift_amount` to the index (if our letter was "a" so an index of 1 it would now be 1 + `shift_amount`)
3. Then we use `mod` (short for [modulo](https://www.mathsisfun.com/definitions/modulo-operation.html)) to ensure the `index` is within 26 (which is the range of our alphabet).
4. And finally, we add the new letter to `new_text` but getting the letter at that index of the alphabet (e.g. alphabet[1] = a)

After we have looped over every letter in the `text` we output `new_text` which is our encoded text.
```python
new_text = EMPTY STRING
FOR EACH letter IN text
    index = INDEX OF letter IN alphabet
    index = index + shift_amount
    index = index MOD 26
    new_text = new_text + alphabet[index]
END

OUTPUT new_text
```

It's important to read the problem carefully, in this code challenge we must encode **and decode** a message from the user.
However, our code already facilitates this functionality.
As mentioned in "Caesar Cipher Explanation", to decode an encoded message we can apply the opposite shift amount.
In this sense, our code can both encode and decode ciphered text.

This solution will not accept anything that is not in the alphabet. So numbers, or symbols will break this code.
In order for the solution to accept numbers and symbols we must check if the letter is in the alphabet and if not 
then add it to `new_text` without any processing done to it. Example below.
```python
new_text = EMPTY STRING
FOR EACH letter IN text
    IF letter IN alphabet THEN
        index = INDEX OF letter IN alphabet
        index = index + shift_amount
        index = index MOD 26
        new_text = new_text + alphabet[index]
    ELSE THEN
        new_text = new_text + letter
END

OUTPUT new_text
```
