import pandas as pd
import os
import shutil

"""a very simple question and answer application to use with the accompanied
word-list. It's just for personal use, so it's as simple as possible.
"""


def load_data(reset=False):
    """Reads tsv file and returns DataFrame.

    rteurns DataFrame
    """
    df = pd.read_csv('word-list.tsv', sep='\t', header=0)

    if (not 'score' in df.columns) or (reset == True):
        df['score'] = 1

    return df.sort_values(by=['score'])


def write_data(df):
    """Write DataFrame to tsv file.

    returns None
    """

    df.to_csv('word-list.tsv', sep='\t', index=False)

    return None


def clear_cli():
    """Clears CLI.

    returns none
    """
    os.system('cls' if os.name == 'nt' else 'clear')

    return None


def question(question, answer, score):
    """Asks question, shows the answer, checks if user memorized the question.

    question is string
    answer is string
    score is float
    returns none
    """
    memorized = False

    while not memorized:
        print('\n  word: ', question, '\n')
        input('  press enter to see the meaning ')
        clear_cli()
        print('\n  meaning: ', answer, '\n')
        if input('  do you recall it? (y: 1): ') == '1':
            memorized = True
            score *= 1.02
        else:
            score *= 0.98
        clear_cli()

    return score


def question_loop(df):
    """Calls question function over rows of a DataFrame.

    df is DataFrame
    returns None
    """
    for index, row in df.iterrows():
        score = question(row['word'], row['meaning'], row['score'])
        df.loc[df['word'] == row['word'], 'score'] = round(score, 2)
        write_data(df)
        df = load_data()
    return None


if __name__ == "__main__":
    df = load_data()
    clear_cli()
    question_loop(df)
