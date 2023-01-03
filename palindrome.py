
#створення функції palindrome з позиційною переменною word
def palindrome (word):
# створення змінної rev_word, яка є зворотньою для word 
    rev_word = word [::-1]
 #operator if compares word and rev_word and print message True"   
    if rev_word==word:
        print (word, "- palindrome")
#if False, print another message
    else: 
        print (word, "- not palindrome")
#call function
palindrome("mom")
palindrome ("mother")