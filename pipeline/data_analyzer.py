# This is the data_analyzer file that takes in formatted data from the file_cleaner and then makes statistical calculations
# on the data and returns the result

from file_cleaner import clean_file

def analyze_data(filename):
    file_cleaner_result = clean_file(filename)
    if file_cleaner_result["Status"] == "Failure":
        return file_cleaner_result

    df = file_cleaner_result["df"]

    result = {
        "Status": "Success",
        "metadata": {
            "rows_original": file_cleaner_result["rows_original"],
            "rows_removed_missing": file_cleaner_result["rows_removed_missing"],
            "rows_after_cleaning": file_cleaner_result["rows_after_cleaning"],
            "rows_removed_invalid_scores": file_cleaner_result["rows_removed_invalid_scores"],
        }
    }

    # Merge the result of the statistics with our result so far
    result.update(compute_statistics(df))

    # Merge the result of the performance with our result so far
    result.update(compute_performance(df))

    return result

# This function computes the highest, lowest and average score
def compute_statistics(df):
    return {
        "statistics": {
            "highest_score": float(df["score"].max()),
            "lowest_score": float(df["score"].min()),
            "average_score": float(df["score"].mean()),
        }
    }

def compute_performance(df):
    return {
        "performance": {
            "excellent": df.loc[df["score"] >= 85, "name"].tolist(),
            "good": df.loc[(df["score"] >= 70) & (df["score"] < 85), "name"].tolist(),
            "needs_improvement": df.loc[df["score"] < 70, "name"].tolist(),
        }
    }