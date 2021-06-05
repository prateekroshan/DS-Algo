def pallindrome_check(str):
    original_str = str
    reversed_str = str[::-1]
    if original_str == reversed_str:
        print (f"{str} is pallindrome")
    else:
        print (f"{str} is not pallindrome")


if __name__ == "__main__":
    string = 'pip'
    pallindrome_check(string)
# inputWord = input("Type any word to check");
# result = pallindrome_check(inputWord)
# print(result)

