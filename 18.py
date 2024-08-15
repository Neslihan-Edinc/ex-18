def frequency_of_words(words_list):
    word_count = {}
    for word in words_list:
       
        word = word.lower().strip(",?!.;:")
        if word not in word_count:
            word_count[word] = 1
        else:
            word_count[word] += 1
    return word_count


user_input = input("Enter a list of words (separated by spaces): ")
words_list = user_input.split()


result = frequency_of_words(words_list)
print(f"Word frequencies in the list: {result}")
