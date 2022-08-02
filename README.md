# CaesarCipher
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

Read more:
- [Wikipedia page on the Caesar Cipher](https://en.wikipedia.org/wiki/Caesar_cipher)
- [Online Caesar Cipher converter](https://cryptii.com/pipes/caesar-cipher)

### Pseudo code solution

```python
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
text = INPUT
shift_amount = INPUT
```

```python
new_text = EMPTY STRING
FOR EACH letter IN text:
    index = INDEX OF letter IN alphabet
    index = index + SHIFT_AMOUNT
    index = index MOD 26
    new_text = new_text + alphabet[index]
END

OUTPUT new_text
```
