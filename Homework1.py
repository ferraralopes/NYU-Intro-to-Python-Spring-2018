
'''Part 1'''

sentence = 'After every storm, if you look hard enough, a rainbow appears'
print(len(sentence))
if len(sentence) < 240:
    print('The sentence fits into a tweet')
elif len(sentence) > 240:
    print('Sorry, the sentence is too long for a tweet')

'''Part 2'''
print('That tweet is {} characters and you have {} remaining characters' .format(len(sentence), 240- len(sentence)))
