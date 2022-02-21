
import pandas as pd

def main():
    '''
    Converts wordle-allowed-guesses into a useable dataframe.
    Note for future work: frame.append will be deprecated in a later pandas verion.
    '''
    df = pd.DataFrame(columns=["word", "0", "1", "2", "3", "4", "value"])
    for word in [line.split()[0] for line in open("wordle-allowed-guesses.txt")]:
        df = df.append({'word' : word,
                        '0' : word[0],
                        '1' : word[1],
                        '2' : word[2],
                        '3' : word[3],
                        '4' : word[4],
                        'value' : 0},
                        ignore_index=True)
    df.to_csv("allowed-guesses-usable.csv", index=False)

if __name__ == "__main__":
    main()

