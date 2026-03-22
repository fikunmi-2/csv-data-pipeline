# This is the dataset_formatter file that coverts the analysis in human_readable output.

def format_output(analyzed_result, mode="human"):
    if analyzed_result["Status"] == "Failure":
        return analyzed_result
    if mode == "human":
        return {
            "Status": "Success",
            "result": "\n".join([
            format_statistics_human(analyzed_result['statistics']),
            format_performance_human(analyzed_result['performance']),
            format_metadata_human(analyzed_result['metadata']),
        ])
        }

    elif mode == "machine":
        return {
            "Status": "Success",
            "result": {
                "Statistics": format_statistics_machine(analyzed_result["statistics"]),
                "Performance": format_performance_machine(analyzed_result["performance"]),
                "Metadata": format_metadata_machine(analyzed_result["metadata"]),
            }
        }
    else:
        return {
            "Status": "Failure",
            "Error": f"Invalid mode '{mode}'. Use 'human' or 'machine'."
        }

def format_statistics_human(statistics):
    return (f"Statistics:\n"
            f"- Highest Score: {(statistics['highest_score']):.2f}\n"
            f"- Lowest Score: {(statistics['lowest_score']):.2f}\n"
            f"- Average Score: {(statistics['average_score']):.2f}\n")

def format_performance_human(performance):
    return (f"Performance:\n"
            f"- Excellent: {', '.join(performance['excellent'])}\n"
            f"- Good: {', '.join(performance['good'])}\n"
            f"- Needs Improvement: {', '.join(performance['needs_improvement'])}\n")

def format_metadata_human(metadata):
    return (f"Metadata:\n"
            f"- Number of Rows (original): {metadata['rows_original']}\n"
            f"- Number of Rows Missing values: {metadata['rows_removed_missing']}\n"
            f"- Number of Rows with invalid scores: {metadata['rows_removed_invalid_scores']}\n"
            f"- Number of Rows (after cleaning): {metadata['rows_after_cleaning']}\n")

def format_statistics_machine(statistics):
    return {
        "Highest Score": round(statistics['highest_score'], 2),
        "Lowest Score": round(statistics['lowest_score'], 2),
        "Average Score": round(statistics['average_score'], 2),
    }

def format_performance_machine(performance):
    return {
        "Excellent": performance['excellent'],
        "Good": performance['good'],
        "Needs Improvement": performance['needs_improvement'],
    }

def format_metadata_machine(metadata):
    return {
        "Number of Rows (original)": metadata['rows_original'],
        "Number of Rows Missing values": metadata['rows_removed_missing'],
        "Number of Rows with invalid scores": metadata['rows_removed_invalid_scores'],
        "Number of Rows (after cleaning)": metadata['rows_after_cleaning'],
    }