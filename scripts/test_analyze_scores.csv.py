from scripts.data_analyzer import analyze_scores

# Testing normal scores
result = analyze_scores("../data/normal_scores.csv")
print(result)

# Testing empty_scores
result = analyze_scores("../data/empty_scores.csv")
print(result)

# Testing single_score
result = analyze_scores("../data/single_score.csv")
print(result)