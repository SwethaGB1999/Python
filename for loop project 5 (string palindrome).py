#Check if a word is a palindrome using for loop
word=input("Enter a word: ")
rev=""
for i in word:
    rev=i+rev
if word==rev:
    print(word,"is a palindrome.")
else:
    print(word,"is not a palindrome.")


