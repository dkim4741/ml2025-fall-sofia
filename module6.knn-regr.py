import numpy as np

class KNNRegressor:
    def __init__(self, k):
        self.k = k
        self.X = np.array([])
        self.Y = np.array([])

    def add_point(self, x, y):
        self.X = np.append(self.X, float(x))
        self.Y = np.append(self.Y, float(y))

    def predict(self, query):
        if self.k > len(self.X):
            return "Error: integer k must be <= N."

        distances = np.abs(self.X - float(query))

        k_idx = np.argsort(distances)[:self.k]

        return np.mean(self.Y[k_idx])


def main():
    N = int(input("Enter positive integer N: "))
    k = int(input("Enter positive integer k: "))

    model = KNNRegressor(k)

    print(f"Enter {N} (x, y) points:")
    for i in range(N):
        x = float(input(f"Point #{i+1} - x: "))
        y = float(input(f"Point #{i+1} - y: "))
        model.add_point(x, y)

    query = float(input("Enter X to predict Y: "))

    result = model.predict(query)

    print(f"For X = {query}, Predicted Y = {result}")

if __name__ == "__main__":
    main()
