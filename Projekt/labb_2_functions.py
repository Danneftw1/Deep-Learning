from pandas import DataFrame, Series
from statistics import mean, median
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

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


def length_words_and_characters_histplot(df,
    size_x=1, size_y=2, figsizes=(15, 5), bin=50, kde=True
) -> sns.histplot: 
    fig, axs = plt.subplots(size_x, size_y, figsize=figsizes)

    sns.histplot(df["character_amount"], bins=bin, kde=kde, ax=axs[0])
    axs[0].set_title("Sentence length in characters")
    axs[0].set_xlabel("Characters")
    axs[0].set_ylabel("Amount")

    sns.histplot(df["word_amount"], bins=bin, kde=kde, ax=axs[1])
    axs[1].set_title("Sentence length in words")
    axs[1].set_xlabel("Words")
    axs[1].set_xticks(np.arange(1, 21))
    axs[1].set_ylabel("Amount")

    plt.tight_layout()
    plt.show()