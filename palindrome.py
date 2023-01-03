
#створення функції palindrome з позиційною переменною word
def palindrome (word):
# створення змінної rev_word, яка є зворотньою для word 
    rev_word = word [::-1]
 #operator if compares word and rev_word"   
    if rev_word==word:
    print (word, "- palindrome")
    