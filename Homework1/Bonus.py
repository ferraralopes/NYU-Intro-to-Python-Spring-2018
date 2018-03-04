"""Homnework 1 - Bonus"""

sentence = 'After every storm, if you look hard enough, a rainbow appears'
print(len(sentence))
Twitter_Len = 280
if len(sentence) < Twitter_Len:
    print('The sentence fits into a tweet')
elif len(sentence) > Twitter_Len:
    print('Sorry, the sentence is too long for a tweet')
    print('That tweet is {} characters and you have {} remaining characters' .format(len(sentence), Twitter_Len- len(sentence)))
