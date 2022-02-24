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

    #read_data_frame(allowed_guesses_input, allowed_guesses_output)
    read_data_frame(answers_input, answers_output)

    

def read_data_frame(input_file, output_file):
    '''
    Read datafame and count occurance
    '''
    df = pd.read_csv(input_file)
    #letter_freq = pd.DataFrame(columns=list(string.ascii_lowercase))
    letter_freq = pd.DataFrame({'Letters': list(string.ascii_lowercase)}, columns=['Letters'])
    #print(letter_freq)


    overall_lst = []
    for i in range(5):
        labels, counts = np.unique(df[str(i)].tolist(),return_counts=True)
        overall_lst.append(df[str(i)].tolist())
        create_data_img(labels, counts, i, output_file)
        #print(i)
        if len(list(string.ascii_lowercase)) != len(labels):
            labels, counts = check_list_size(list(string.ascii_lowercase), labels, counts)

            #print(len(list(string.ascii_lowercase)) - len(labels))

        #freq = pd.DataFrame({'Letters': labels, str(i) : counts}, columns=['Letters', str(i)])
        #letter_freq = pd.merge(letter_freq, freq, on='Letters')
        #print(letter_freq)

        

    labels, counts = np.unique(overall_lst,return_counts=True)    
    create_data_img(labels, counts, "overall", output_file)

def check_list_size(ascii, labels, counts):
    # print("--")

    #counts = np.pad(array=counts, pad_width=len(ascii)-len(labels))
    # print(counts)
    #labels.append(list(set(ascii) - set(labels)))
    #labels= np.append(labels, list(set(ascii) - set(labels)))
    #print(labels)

    print(counts)
    print(labels)
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