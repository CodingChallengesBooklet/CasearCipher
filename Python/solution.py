
# define the data we need: alphabet, text, shift amount.
alphabet = "abcdefghijklmnopqrstuvwxyz"
# .lower() is used to convert the text into only lower text as our alphabet only has lowercase letters.
text = input("Please enter your text: ").lower()
# make sure to use int() so our shift is a number not a string.
shift_amount = int(input("Please enter the shift amount: "))

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

# Show the difference between the original and encoded text.
print(f"\"{text}\" has been encoded to \"{new_text}\"")