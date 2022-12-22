import pandas as pd
import os

"""a very simple question and answer application to use with the accompanied
word-list. It's just for personal use, so it's as simple as possible.
"""


def load_data(shuffle=False):
    """Reads tsv file and returns DataFrame.

    shuffle is bool
    rteurns DataFrame
    """
    df = pd.read_csv('word-list.tsv', sep='\t', header=0)

    if shuffle == True:
        return df.sample(frac=1)

    return df


def clear_cli():
    """Clears CLI.

    returns none
    """
    os.system('cls' if os.name == 'nt' else 'clear')

    return None


def question(question, answer):
    """Asks question, shows the answer, checks if user memorized the question.

    question is string
    answer is string
    returns none
    """
    memorized = False

    while not memorized:
        print('\nword: ', question, '\n')
        input('press enter to see the meaning ')
        print('\nmeaning: ', answer, '\n')
        if input('memorized? (yes: 1): ') == '1':
            memorized = True
        clear_cli()

    return None


def question_loop(df):
    """Calls question function over rows of a DataFrame.

    df is DataFrame
    returns None
    """
    for index, row in df.iterrows():
        question(row['word'], row['meaning'])

    return None


if __name__ == "__main__":
    shuffle = input('shuffle? (y:1)') == '1'
    df = load_data(shuffle)
    clear_cli()
    question_loop(df)
