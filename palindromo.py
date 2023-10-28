def palindromo(word):
    new_word = word.replace(' ', '')
    new_word = new_word.lower()

    new_word_reverse = new_word[ : :-1]
    print(new_word_reverse)
    if new_word_reverse == new_word:
        return True
    else:
        return False



def main():
    word = input("Ingresa una palabra: ")
    is_palindromo = palindromo(word)
    if is_palindromo == True:
        print("Es palindromo")
    else:
        print("No es palindromo")



if __name__ == '__main__':
    main()