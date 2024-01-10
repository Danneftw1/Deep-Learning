from pandas import DataFrame, Series
from statistics import mean, median

def character_counter_for_sentences(column: Series) -> None:
    sentence_length_characters = []
    for row, text in enumerate(column.iloc):
        sentence_length_characters.append(len(text))
    return sentence_length_characters


def word_counter_for_sentences(column: Series) -> None:
    sentence_length_words = []
    for row, text in enumerate(column.iloc):
        sentence_length_words.append(len(text.split()))
    return sentence_length_words


def word_or_character_length(word_or_character_amount: int, word_or_character_list: list) -> print:
    above_100_length = [length >= word_or_character_amount for length in word_or_character_list]
    is_above_100 = above_100_length.count(True)
    is_not_above_100 = above_100_length.count(False)

    above_or_equal_print = print(f"\nRows that are ABOVE or EQUAL to {word_or_character_amount} characters long: {is_above_100}")
    below_print = print(f"Rows that are BELOW {word_or_character_amount} characters long: {is_not_above_100}")
    return above_or_equal_print, below_print


def print_metrics_for_characters_or_words(word_or_character: str, word_or_character_list: list) -> print:
    print_median = print(f"Median Length {word_or_character}:", median(word_or_character_list))
    print_mean = print(f"Average Length {word_or_character}:", mean(word_or_character_list))
    print_min = print(f"Smallest Length {word_or_character}:", min(word_or_character_list))
    print_max = print(f"Longest Length {word_or_character}:", max(word_or_character_list),"\n")
    return print_median, print_mean, print_min, print_max