__author__ = 'jc451073'
vowels = ['a', 'e', 'i', 'o', 'u']
vowel_count = 0
name = input('Enter your name:')
for c in name:
    if c.lower() in vowels:
         vowel_count += 1
#print(vowel_count)
print("Out of {} letters, {} has {} vowels'.format(len(name))", name, vowel_count)

