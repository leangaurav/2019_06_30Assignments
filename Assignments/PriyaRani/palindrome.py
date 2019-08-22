import sys
with open('alphabet.txt','r') as r:
    #word=0
    palindromes = []
    for line in r:
        words =line.split(' ')
        # print(type(words))
        # print('The available words are ', words)
        for word in words:
            print(type(word))
            word = word.lower()
            reverse_word = word[::-1]
            if word == reverse_word:
                palindromes.append(word)

    print('Palindrome word(s): ', palindromes)
    
