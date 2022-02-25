
import pandas as pd

def main():
    '''
    File location for raw and filtered input and export locations. Sends files through to "create_csv" for export.
    '''
    raw_folder_loc = "../data/raw/"
    filtered_folder_loc = "../data/filtered/"
    raw_file_allowed_guesses = "wordle-allowed-guesses.txt"
    raw_wordle_answers = "wordle-answers.txt"
    create_csv(raw_folder_loc + raw_file_allowed_guesses, filtered_folder_loc + raw_file_allowed_guesses.split(".")[0])
    create_csv(raw_folder_loc + raw_wordle_answers, filtered_folder_loc + raw_wordle_answers.split(".")[0])


def create_csv(input_file, output_file):
    '''
    Converts wordle-allowed-guesses into a useable dataframe.
    Note for future work: frame.append will be deprecated in a later pandas version.
    '''
    df = pd.DataFrame(columns=["word", "0", "1", "2", "3", "4", "value"])
    for word in [line.split()[0] for line in open(input_file)]:
        df = df.append({'word' : word,
                        '0' : word[0],
                        '1' : word[1],
                        '2' : word[2],
                        '3' : word[3],
                        '4' : word[4],
                        'value' : 0},
                        ignore_index=True)
    df.to_csv(output_file + ".csv", index=False)

if __name__ == "__main__":
    main()

