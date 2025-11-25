import numpy as np
from sklearn.neighbors import KNeighborsRegressor


class KNNRegressor:
    def __init__(self, k, n):
        self.k = k
        self.n = n
        self.count = 0

        # Pre-allocation
        self.X = np.zeros(n)
        self.Y = np.zeros(n)

    def add_point(self, x, y):
        if self.count < self.n:
            self.X[self.count] = float(x)
            self.Y[self.count] = float(y)
            self.count += 1
        else:
            print("Error: Dataset is full.")

    def finalize(self):
        pass

    def predict(self, query):
        if self.k > self.n:
            return "Error: integer k must be <= N."

        X_2d = self.X.reshape(-1, 1)

        knn = KNeighborsRegressor(n_neighbors=self.k)
        knn.fit(X_2d, self.Y)

        y_pred = knn.predict([[float(query)]])[0]
        return y_pred


def main():
    N = int(input("Enter positive integer N: "))
    k = int(input("Enter positive integer k: "))

    model = KNNRegressor(k, N)

    print(f"Enter {N} (x, y) points:")
    for i in range(N):
        x = float(input(f"Point #{i + 1} - x: "))
        y = float(input(f"Point #{i + 1} - y: "))
        model.add_point(x, y)

    model.finalize()

    label_variance = np.var(model.Y)
    print(f"Variance of labels in the training dataset: {label_variance}")

    query = float(input("Enter X to predict Y: "))

    result = model.predict(query)

    print(f"For X = {query}, Predicted Y = {result}")


if __name__ == "__main__":
    main()
    main()


