word = input()

palindrome = True

for n in range(0, len(word)):
    if word[n] != word[n * -1 - 1]:
        palindrome = False
if palindrome:
    palindrome = "This is a palindrome!"
else:
    palindrome = "Not a palindrome :("

print(palindrome)
