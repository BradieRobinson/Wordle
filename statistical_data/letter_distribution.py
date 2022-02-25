import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
import string

def main():
    '''
    Prints graph of distribution of letters in 1 - 5th position + overall distribution
    '''
    folder_root = "../data/filtered/"

    allowed_guesses_input = folder_root + "wordle-allowed-guesses.csv"
    allowed_guesses_output = "letter_distribution/allowed_guesses/"

    answers_input = folder_root + "wordle-answers.csv"
    answers_output = "letter_distribution/answers/"

    read_data_frame(allowed_guesses_input, allowed_guesses_output)
    read_data_frame(answers_input, answers_output)

def read_data_frame(input_file, output_file):
    '''
    Read datafame and count occurance
    '''
    df = pd.read_csv(input_file)
    letter_freq = pd.DataFrame({'Letters': list(string.ascii_lowercase)}, columns=['Letters'])

    overall_lst = []
    for i in range(5): #loop all positions
        labels, counts = np.unique(df[str(i)].tolist(),return_counts=True)
        overall_lst.append(df[str(i)].tolist())
        create_data_img(labels, counts, i, output_file)

        if len(list(string.ascii_lowercase)) != len(labels): #ensure that all columns contain all lowercase ascii letters
            labels, counts = check_list_size(list(string.ascii_lowercase), labels, counts)
        letter_freq = append_to_dataframe(letter_freq, labels, counts, str(i))

    labels, counts = np.unique(overall_lst,return_counts=True)   
    letter_freq = append_to_dataframe(letter_freq, labels, counts, "overall")
    create_data_img(labels, counts, "overall", output_file)

    letter_freq.to_csv(output_file + "frequency", index=False) #create csv of all occurances

def append_to_dataframe(letter_freq, labels, counts, heading):
    '''
    Add each row into the old dataframe
    '''
    new_freq = pd.DataFrame({'Letters': labels, heading : counts}, columns=['Letters', heading])
    return pd.merge(letter_freq, new_freq, on='Letters')


def check_list_size(ascii, labels, counts):
    '''
    If letter was not used in a position add to list with count as 0
    '''
    counts = np.pad(array=counts, pad_width=(0,len(ascii)-len(labels)))
    labels= np.append(labels, list(set(ascii) - set(labels)))
    return labels, counts


def create_data_img(labels, counts, img_name, output_file):
    '''
    Create image of distribution
    '''
    ticks = range(len(counts))
    plt.bar(ticks,counts, align='center')
    plt.xticks(ticks, labels)
    plt.ylabel('Total Occurances') 
    plt.xlabel('Letter') 
    plt.title("Position: " + str(img_name))
    plt.savefig(output_file + str(img_name) + '.png')
    plt.clf()


if __name__ == "__main__":
    main()