def is_palindrome(word):
    word = word.replace(" ", "").lower()
    
    length = len(word)
    for i in range(length // 2):
        if word[i] != word[length - i - 1]:
            return False
    return True