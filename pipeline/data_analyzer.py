# This is the data_analyzer file that takes in formatted data from the file_cleaner and then makes statistical calculations
# on the data and returns the result

from file_cleaner import clean_file

def analyze_data(filename):
    file_cleaner_result = clean_file(filename)
    if file_cleaner_result["Status"] == "Failure":
        return file_cleaner_result

    df = file_cleaner_result["df"]

    result = {}
    result.update(file_cleaner_result)

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