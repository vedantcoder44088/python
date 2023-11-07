def count_words(text):
    words = text.split()
    return len(words)


def count_lines(text):
    lines = text.split('\n')
    return len(lines)


def count_word_occurrence(text, target_word):
    words = text.split()
    count = words.count(target_word)
    return count


def count_character_occurrence(text, target_char):
    count = text.count(target_char)
    return count


def count_blank_spaces(text):
    count = text.count(' ')
    return count


def main():


    with open("text01.txt", 'r') as file:
        content = file.read()

        word_count = count_words(content)
        line_count = count_lines(content)

        target_word = 'Patel'
        word_occurrence = count_word_occurrence(content, target_word)

        target_char = 'V'
        char_occurrence = count_character_occurrence(content, target_char)

        blank_space_count = count_blank_spaces(content)

        print("Word count: ", word_count)
        print("Line count: ",line_count)
        print("Occurrence of ", target_word, " : ", word_occurrence)
        print("Occurrence of ", target_char, " : ", char_occurrence)
        print("Number of blank spaces: ", blank_space_count)


if __name__ == "__main__":
    main()
