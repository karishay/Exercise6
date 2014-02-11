from sys import argv
#import, open, read by line: the twain content
script, filename = argv

#split all the words in the line by " " into a dictionary of words
#if that word is already in the dictionary,
#increment the value by one
#print a list of key and value pairs



# strip all characters before 97 and after 123
# if i in ted is not in ascii range 97, 123 -- strip it. 
# print stripped results of red
#newList = []

#while i in ted:
#    if ord('a') < i < ord('z'):
#        newList = i

def dictionary_repeated_words(filename):
    ted = open(filename, "r").read()
    ted = ted.lower()
    OnlyLetter = ""
    for i in range(len(ted)):
        if not ord(ted[i]) >= ord('a') and ord(ted[i]) < ord('z'):
            OnlyLetter +=  " "
            #OnlyLetter += ted[i]
        else:
            OnlyLetter += ted[i]
    ted_dict = {}
    words = OnlyLetter.split()
    for word in words:
        ted_dict[word] = ted_dict.get(word, 0) + 1

    for key, value in ted_dict.iteritems():
        print key, value

print dictionary_repeated_words('test.txt')



