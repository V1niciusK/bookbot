def main():
    path_to_book="books/frankenstein.txt"
    book = txt_file_to_string(path_to_book)
    
    word_count=count_words(book)
    char_distribution=char_tally(book)
    # print (char_distribution)
    prettify_results(path_to_book, word_count, char_distribution)

def count_words(text):
    return len(text.split())

def char_tally( text ):

    lowercase_text = text.lower()

    tally = {}

    """ for word in lowercase_text.split():

        for letter in list( word ):

    """
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

def sort_dict(dict):
    print(f"sort_dict input: {dict}")
    #cumbersome implementation, to be improved
    temp_array = []

    for key in dict:
        #print(f"key: {key}")
        #print(f"value: {dict[key]}")
        temp_array.append({"key":key, "value": dict[key]})

    def sort_on(dict):
        return dict["value"]
    
    temp_array.sort(reverse=True, key=sort_on)
    print(f"temp_array: {temp_array}")

    sorted_dictionary = {}
    for item in temp_array:
        print(f"item: {item}")
        sorted_dictionary[item["key"]] = item["value"]

    return sorted_dictionary


def prettify_results(book ,word_count, char_dict):

    # formated strings limitation
    lines_of_text=char_dict['\n'] + 1

    # character logic

    print(f"--- Begin report of {book} ---")
    print("")
    print("Text statistics")
    print(f"{lines_of_text} lines compose the document")
    print("")
    print("Word statistics")
    print(f"{word_count} words found in the document")
    print("")
    print("Character statistics")
    
    print(f"The TBD character was found TBD times ")

    print(sort_dict(char_dict))


main()
