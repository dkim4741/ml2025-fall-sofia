import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score


class Data:
    def __init__(self, n):
        self.n = n
        self.count = 0
        self.X = np.zeros(n, dtype=float)
        self.Y = np.zeros(n, dtype=int)

    def add(self, x, y):
        if self.count < self.n:
            self.X[self.count] = float(x)
            self.Y[self.count] = int(y)
            self.count += 1


def main():
    N = int(input("Enter N: "))
    train_data = Data(N)
    for i in range(N):
        x = float(input(f"Train #{i + 1} x: "))
        y = int(input(f"Train #{i + 1} y: "))
        train_data.add(x, y)

    M = int(input("Enter M: "))
    test_data = Data(M)
    for i in range(M):
        x = float(input(f"Test #{i + 1} x: "))
        y = int(input(f"Test #{i + 1} y: "))
        test_data.add(x, y)

    X_train = train_data.X.reshape(-1, 1)
    y_train = train_data.Y
    X_test = test_data.X.reshape(-1, 1)
    y_test = test_data.Y

    best_k = -1
    best_acc = -1.0

    limit_k = min(10, N)

    for k in range(1, limit_k + 1):
        knn = KNeighborsClassifier(n_neighbors=k)
        knn.fit(X_train, y_train)

        pred = knn.predict(X_test)
        acc = accuracy_score(y_test, pred)

        if acc > best_acc:
            best_k = k
            best_acc = acc

    print(f"Best k: {best_k}")
    print(f"Test Accuracy: {best_acc}")


if __name__ == "__main__":
    main()