#Copywrite (C) Paul Ashby 2014
#Count vowels in a file.

count = 0
vowel = "aeiou"
vowel_cap = "AEIOU"
vowelcount = 0

file = open("input.txt", "r")
for eachline in file:
    count += 1 #Counts number of lines in file.
    for eachletter in eachline:
        if eachletter in vowel or eachletter in vowel_cap:
            vowelcount += 1 #Counts the number of vowels in file.
add = file.read()
file.close()

print("There are", count, "lines in this file.")
print("There are", vowelcount, "vowels in this file.")
