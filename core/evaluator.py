from rouge_score import rouge_scorer

class Evaluator:
    def __init__(self):
        self.scorer = rouge_scorer.RougeScorer(['rouge1', 'rougeL'], use_stemmer=True)

    def evaluate(self, reference, generated):
        scores = self.scorer.score(reference, generated)
        return {k: v.fmeasure for k, v in scores.items()}
