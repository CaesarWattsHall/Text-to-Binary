def text_to_binary():
    while True:
        text = input("Enter a sentence or word: ")
        binary = ' '.join(format(ord(i), 'b') for i in text)
        print(binary)
        choice = input("Enter 1 to continue or 2 to exit: ")
        if choice == '2':
            break

text_to_binary()
