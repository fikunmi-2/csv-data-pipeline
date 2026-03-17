# This is the dataset_formatter file that coverts the analysis in human_readable output.

from data_analyzer import analyze_data

def format_human_readable(data):
    data_analyzer_result = analyze_data(data)

    if data_analyzer_result["Status"] == "Failure":
        return data_analyzer_result

    print(f"\n{data_analyzer_result}")

    return (f"{format_statistics_human(data_analyzer_result["statistics"])}"
            f"\n"
            f"{format_performance_human(data_analyzer_result["performance"])}")

def format_statistics_human(statistics):
    return (f"Statistics:\n"
            f"- Highest Score: {(statistics['highest_score']):.2f}\n"
            f"- Lowest Score: {(statistics['lowest_score']):.2f}\n"
            f"- Average Score: {(statistics['average_score']):.2f}\n")

def format_performance_human(performance):
    return (f"Performance:\n"
            f"- Excellent: {", ".join(performance['excellent'])}\n"
            f"- Good: {", ".join(performance['good'])}\n"
            f"- Needs Improvement: {", ".join(performance['needs_improvement'])}\n")

# format_machine_readable = format_human_readable

# Testing the data
print(format_human_readable("../data/sample_data.csv"))