def main():
    book_path = "books/frakenstein.txt"
    # Calls get_book_text function to return what was read from file as string
    text = get_book_text(book_path)
    # Calls get_num_words function to return the length of the string created from get_book_text
    num_words = get_num_words(text)
    # Calls get_num_letters to return the occurence of each letter in the string created from get_book_text
    num_letters = get_num_letters(text)
    print(f'--- Begin report of {book_path} ---')
    print(f"{num_words} words in document\n")
    for letter in num_letters:
        print(f"{letter} occurs {num_letters[letter]} times")
    print(f'--- End report ---')

def get_num_words(text):
    # Splits the string into a list to count words by showing the length of the list
    words = text.split()
    return len(words)

def get_book_text(path):
    # Opens the text file passed to the function
    with open (path) as f:
        return f.read()
def get_num_letters(text):
    # Splits the string into a list to count the number of letters
    words = text.split()
    num_letter = {}
    # Runs a loop for each string in the list
    for word in words:
        # Runs a loop for each character in each string
        for letter in word:
            # Checks that the character is alphabetic
            if letter.isalpha():
                # Makes the character lowercase to make the count case insenstive.
                letter = letter.lower()
                # If it already exists in the dictionary, increase the count by one.
                if letter in num_letter:
                    num_letter[letter] += 1
                # Otherwise create a new key in the dictionary
                else:
                    num_letter[letter] = 1
    # Return the dictionary sorted by number of occurences.
    return dict(sorted(num_letter.items(), key=lambda item: item[1], reverse=True))
main()