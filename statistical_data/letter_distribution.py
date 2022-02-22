import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 

def main():
    '''
    Prints graph of distribution of letters in 1 - 5th position + overall distribution
    '''
    df = pd.read_csv ('../reading_data/allowed-guesses-usable.csv')
    overall_lst = []
    for i in range(5):
        labels, counts = np.unique(df[str(i)].tolist(),return_counts=True)
        overall_lst.append(df[str(i)].tolist())
        create_data_img(labels, counts, i)

    labels, counts = np.unique(overall_lst,return_counts=True)    
    create_data_img(labels, counts, "overall")



def create_data_img(labels, counts, img_name):
    ticks = range(len(counts))
    plt.bar(ticks,counts, align='center')
    plt.xticks(ticks, labels)
    plt.savefig("letter_distribution/allowed_gusses/" + str(img_name) + '.png')
    plt.clf()


if __name__ == "__main__":
    main()