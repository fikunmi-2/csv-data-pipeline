# This is the data_analyzer file that takes in formatted data from the file_cleaner and then makes statistical calculations
# on the data and returns the result

from file_cleaner import clean_file
import pandas as pd
import numpy as np

def analyze_data(filename):
    file_cleaner_result = clean_file(filename)
    if file_cleaner_result["Status"] == "Failure":
        return {
            "Status": "Failure",
            "Error": file_cleaner_result["Error"]
        }

    df = file_cleaner_result["df"]

    result = {
        "Status": "Success",
        "file_cleaner_result": file_cleaner_result,
        "data_analyzer_result": {}
    }


    # If the data is empty, then it should return an empty data and not process any other information
    if df.empty:
        result["Status"] = "Failure"
        result["Error"] = "Dataframe is empty. So no analysis could be performed."
        return result

    # Merge the result of the statistics with our result so far
    result["data_analyzer_result"].update(compute_statistics(df))

    # Merge the result of the performance with our result so far
    result["data_analyzer_result"].update(compute_performance(df))

    return result

# This function computes the highest, lowest and average score
def compute_statistics(df):
    return {
        "Highest Score": float(df["score"].max()),
        "Lowest Score": float(df["score"].min()),
        "Average Score": float(df["score"].mean()),
    }

def compute_performance(df):
    # Put all the result categories to their corresponding records in the dataframe
    df["performance"] = np.where((df["score"] >= 70) & (df["score"] < 85), "Good",
                                 np.where(df["score"] >= 85, "Excellent", "Needs Improvement"))

    return {
        "Performance": {
            "Excellent": df.loc[df["performance"] == "Excellent", "name"].tolist(),
            "Good": df.loc[df["performance"] == "Good", "name"].tolist(),
            "Needs Improvement": df.loc[df["performance"] == "Needs Improvement", "name"].tolist(),
        }
    }

# Testing our data_analyzer
result_test = analyze_data("../data/sample_data.csv")
# result_test = analyze_data(1)
print(result_test)