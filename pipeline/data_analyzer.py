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
        count = 0
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
            count += 1

        if count == 0:
            return {}

        average_score = total_score / count

        # Print Result of Calculation
        results["highest"] = highest_score
        results["lowest"] = lowest_score
        results["average"] = average_score

        results["performance"] = performance

        return results

# Call analyse scores function and display result
if __name__ == "__main__":
    path = "../data/sample_scores.csv"

    analyzed_results = analyze_scores(path)

    print(analyzed_results)