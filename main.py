# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

#from cgitb import text
#from distutils import text_file

  
from cgitb import text

with open("story.txt", "r") as file:
    text = file.read()

      
word_count = {}
               
for word in text.strip().lower().split():
    if word in word_count:
        word_count[word] += 1
    else: 
        word_count[word] = 1

print(word_count)

    