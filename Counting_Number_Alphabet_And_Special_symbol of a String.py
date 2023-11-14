Email = 'purnasaud3123@gmail.com'
alphabet = []
digit = []
special_character = [ ]
for character in Email:
    if character.isalpha():
        alphabet.append(character)
    elif character.isdigit():
        digit.append(character)
    else:
        special_character.append(character)

print("Digit: ", len(digit), "Alphabet: ", len(alphabet), "Special_Character: ", len(special_character))


s1 = 'purna'
s2 = 'saud'

first_s1 = s1[0]
last_s2 = s2[-1]

second_last_s1 = s1[-2]
second_last_s1 = s2 [-2]

lengtth_s1 = len(s1)

