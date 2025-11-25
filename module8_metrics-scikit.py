import numpy as np
from sklearn.metrics import precision_score, recall_score


class BinaryEvaluator:
    def __init__(self, n):
        self.n = n
        self.count = 0

        self.y_true = np.zeros(n, dtype=int)
        self.y_pred = np.zeros(n, dtype=int)

    def add_point(self, x, y):
        if self.count < self.n:
            self.y_true[self.count] = int(x)
            self.y_pred[self.count] = int(y)
            self.count += 1
        else:
            print("Error: dataset is already full.")

    def precision(self):
        return precision_score(self.y_true, self.y_pred, zero_division=0)

    def recall(self):
        return recall_score(self.y_true, self.y_pred, zero_division=0)


def main():
    N = int(input("Enter positive integer N: "))

    evaluator = BinaryEvaluator(N)

    print(f"Enter {N} (x, y) points (X = true label, Y = predicted label, both 0 or 1):")
    for i in range(N):
        x = int(input(f"Point #{i + 1} - X (true label): "))
        y = int(input(f"Point #{i + 1} - Y (predicted label): "))
        evaluator.add_point(x, y)

    precision = evaluator.precision()
    recall = evaluator.recall()

    print(f"Precision: {precision}")
    print(f"Recall: {recall}")


if __name__ == "__main__":
    main()
