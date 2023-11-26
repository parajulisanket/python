# write a function that takes a string and count the number of the vowles present in the string.

def is_vowel(v):
    count = 0
    for i in v.lower():
        if i in 'aeiou':
            count = count + 1
    return count

# name = input("enter the string:")
# answer = is_vowel(name)
# print("The answer is",answer)






# write a function that takes string and count the number hof consonants present in that string.

def is_consanent(v):
    count = 0
    for i in v.lower():
        if i not in 'aeiou':
            count = count + 1
    return count

# name = input("enter the string:")
# answer = is_vowel(name)
# print("The answer is",answer)


# write a function that takes a string and count the number of consonants and vowles present in the string.
