try:
    from datasets import load_dataset # type: ignore
except Exception:
    import sys
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", "datasets"])
    from datasets import load_dataset # type: ignore

import pandas as pd # type: ignore


# set sample limit
sample_limit = 100

# load the amozon_reviews dataset(small subset)
reviews_dataset = load_dataset("amazon_polarity",
                                split ="train",
                                keep_in_memory=True,
                                streaming=False
                                )


# collect the first 100 items using for loop
data_list = []
for i, item in enumerate(reviews_dataset):
    data_list.append(item)
    if i + 1 >= sample_limit    :
        break


# convert to pandas dataframe
reviews_df = pd.DataFrame(data_list)

# show the first rows

reviews_df.head()

Items_to_print = 10

reviews_df.head(Items_to_print)


# export to text file

with open("amazon_reviews_sample.txt", "w") as file:

    file.write(reviews_df.head(Items_to_print).to_string()) 


