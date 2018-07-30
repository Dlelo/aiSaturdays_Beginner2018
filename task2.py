import random

words = [word.rstrip('\n') for word in open('words.txt')]
randomPhrase = " ".join([words[random.randrange(0, len(words))] for i in range(4)])

print "The 4 words: " 
print randomPhrase
splitingPhrase=randomPhrase.split(" ")

reversingPhrase=splitingPhrase[-1::-1]
joinReversePhrase = ' '.join(reversingPhrase)
#print joinReversePhrase
#reverse order of the words


reverseWords = joinReversePhrase.split(" ")
thereversedWords = [words[::-1] for words in reverseWords]
reversePhrase = " ". join(thereversedWords)

print "Reverse the order of the 4 words and the letters in each word. Answer: "
print reversePhrase
