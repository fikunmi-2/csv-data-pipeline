import csv

def analyze_scores(file_path):
    """
    Reads a CSV of names and scores and returns analysis results.
    """
    results = {}
    with open(file_path, mode='r', newline='', encoding='utf-8') as csvfile:
        records = csv.DictReader(csvfile)
        first_record = True

        total_score = 0
        len_record = 0
        performance = {"Excellent": [], "Good": [], "Needs Improvement": []}

        for record in records:
            if first_record:
                highest_score = float(record['score'])
                lowest_score = float(record['score'])
                first_record = False
            score = float(record['score'])
            if score > highest_score:
                highest_score = score
            if score < lowest_score:
                lowest_score = score

            if score >= 85:
                performance['Excellent'].append(record['name'])
            elif 70 <= score < 85:
                performance['Good'].append(record['name'])
            else:
                performance['Needs Improvement'].append(record['name'])
            total_score += score
            len_record += 1

        if len_record == 0:
            return {}

        average_score = total_score / len_record

        # Print Result of Calculation
        results["Highest score"] = highest_score
        results["Lowest score"] = lowest_score
        results["Average score"] = average_score

        results["Performance"] = performance

        return results

# Call analyse scores function and display result
path = "../data/sample_scores.csv"

analyzed_results = analyze_scores(path)

print(analyzed_results)