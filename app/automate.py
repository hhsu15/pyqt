"""Mini project 1

1. Get target files from a directory
2. Read in those files and concatenate them into one
3. Apply regex rules to extract certain information from text data
4. Create a new file with extracted data as additional columns

"""

import os
import re

import pandas as pd


# resource_dir = "/Users/hsin/git/learnwithshin/core-python-automation/resources/"


def get_target_files(prefix, resource_dir):
    """Get the target files."""
    target_files = [
        file for file in os.listdir(resource_dir) if file.startswith(prefix)
    ]
    return target_files


def concat_df(file_names, resource_dir):
    """Read in each csv file and concatenate into one dataframe."""
    all_dfs = [pd.read_csv(resource_dir + f) for f in file_names]
    return pd.concat(all_dfs)


def extract_interest(string):
    int_reg = r"interest rate:\s*(\d*\.\d*)"
    match = re.search(int_reg, string, re.I)
    try:
        return float(match.group(1))
    except AttributeError:
        print(f"Failed to edtract interest. No match for string: {string}")
        return None


def extract_payment(string):
    payment_reg = r"monthly payment:\s*\${0,1}(\d*)"
    match = re.search(payment_reg, string, re.I)
    try:
        return float(match.group(1))
    except AttributeError:
        print(f"Failed to edtract payment. No match for string: {string}")
        return None


def automate(directory, output_name):
    # get all target file names
    file_names = get_target_files("20", directory)

    # combine all files into one df
    all_df = concat_df(file_names, directory)

    # assign new column using regex for extraction
    all_df["interest"] = all_df["comments"].apply(extract_interest)
    all_df["payment"] = all_df["comments"].apply(extract_payment)

    # reset index

    all_df.reset_index(inplace=True)
    # save to csv
    all_df.to_csv("/Users/hsin/Desktop/" + output_name)
    return all_df
