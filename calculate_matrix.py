def count_errors(reference, hypothesis):
    # Tokenize the reference and hypothesis into words
    ref_words = set(reference.lower().split())
    hyp_words = set(hypothesis.lower().split())

    # Count true positives, false positives, and false negatives
    true_positives = len(ref_words.intersection(hyp_words))
    false_positives = len(hyp_words - ref_words)
    false_negatives = len(ref_words - hyp_words)

    return true_positives, false_positives, false_negatives

# Example usage
reference = "But even that you see even the rock and roll dying and all that is touching someone and you know and all that was human contact if you like and now it’s not even hehehe hehe hehe"
hypothesis = "even roll"
#hypothesis = "Or even that you see even the rock and roll I know I hear what it was I love you"

#reference = "Hahaha on Khaosarn road we ate the khaosarn road khaosarn road khaosarn road what I mean no, only have cockroach hahaha and errr what"
#hypothesis = "hahaha"

tp, fp, fn = count_errors(reference, hypothesis)

print(f"True Positives: {tp}")
print(f"False Positives: {fp}")
print(f"False Negatives: {fn}")

def calculate_metrics(true_positives, false_positives, false_negatives):
    precision = true_positives / (true_positives + false_positives)
    recall = true_positives / (true_positives + false_negatives)
    f1_score = 2 * (precision * recall) / (precision + recall)
    return precision, recall, f1_score

# Example usage
true_positives = tp
false_positives = fp
false_negatives = fn

precision, recall, f1_score = calculate_metrics(true_positives, false_positives, false_negatives)

print(f"Precision: {precision:.2f}")
print(f"Recall: {recall:.2f}")
print(f"F1 Score: {f1_score:.2f}")

