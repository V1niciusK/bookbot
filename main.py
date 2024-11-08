def main():
    path_to_book="books/frankenstein.txt"
    book = txt_file_to_string(path_to_book)
    
    word_count=count_words(book)
    char_distribution=char_tally(book)
    
    pretty_results(path_to_book, word_count, char_distribution)

def count_words(text):
    return len(text.split())

def char_tally( text ):

    lowercase_text = text.lower()

    tally = {}

    for letter in lowercase_text:
        if not ( letter in tally ):

            tally[ letter ] = 1

        else:
            tally[ letter ] += 1

    return tally

def txt_file_to_string(path):
    with open(path) as file:
        try:
            returnable_string = file.read()
            return returnable_string
        except Exception as e:
            print(f"Could not read file in {path}: {e}")
            exit()

def sort_dict(dict, index="value"):
    
    #cumbersome implementation, to be improved
    temp_array = []

    for key in dict:
        temp_array.append({"key":key, "value": dict[key]})

    def sort_on(d):
        return d[index]
    
    temp_array.sort(reverse=True, key=sort_on)

    sorted_dictionary = {}
    for item in temp_array:
        sorted_dictionary[item["key"]] = item["value"]

    return sorted_dictionary


def pretty_results(book ,word_count, char_dict):

    # formated strings limitation
    lines_of_text=char_dict['\n'] + 1

    print(f"--- Begin report of {book} ---")
    print("")
    print("Text statistics")
    print(f"{lines_of_text} lines compose the document")
    print("")
    print("Word statistics")
    print(f"{word_count} words found in the document")
    print("")
    print("Character statistics")
    sorted_char_dict = sort_dict(char_dict)
    for character in sorted_char_dict:
        if character.isalpha():
            print(f"The {character} character was found {sorted_char_dict[character]} times ")

    print()


main()
