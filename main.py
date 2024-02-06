def palindrome(word):
    count = 1

    if word.isspace():
        return False
    
    word = word.upper()
    
    word = word.replace(' ', '')

    for letter in word:
        if letter == ' ':
            continue
        elif letter == word[len(word) - count]:
            count += 1
            continue
        else:
            return False
    return True

if __name__ == '__main__': 
    print(palindrome(word))
