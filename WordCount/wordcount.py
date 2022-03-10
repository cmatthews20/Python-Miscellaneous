
wordCount = int(input("How many Words?: "))

wordList = []
firstLetters = ""
for i in range(wordCount):
    name=str(input("Word?: "))
    wordList.append(name)
    
    firstLetters += name[0]
    
longestWord= max(wordList, key=len)
print("the longest word is", longestWord)

shortestWord= min(wordList, key=len)
print("the shortest word is", shortestWord)


print("firstletters:", firstLetters)

