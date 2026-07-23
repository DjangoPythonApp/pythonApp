class Perceptron:
    def __init__(self, learning_rate=0.1, epochs=1000):
        self.learning_rate = learning_rate
        self.epochs = epochs
        self.weights = []
        self.bias = 0.0

    def activation_function(self, value):
        """Return 1 for positive class and 0 for negative class."""
        return 1 if value >= 0 else 0

    def predict(self, features):
        """
        Perceptron formula:

        z = (x1 × w1) + (x2 × w2) + bias
        """

        weighted_sum = self.bias

        for feature, weight in zip(features, self.weights):
            weighted_sum += feature * weight

        return self.activation_function(weighted_sum)

    def train(self, x_train, y_train):
        """Train the perceptron using labelled data."""

        number_of_features = len(x_train[0])

        self.weights = [0.0] * number_of_features
        self.bias = 0.0

        for _ in range(self.epochs):
            total_errors = 0

            for features, actual_output in zip(x_train, y_train):
                predicted_output = self.predict(features)

                error = actual_output - predicted_output

                if error != 0:
                    total_errors += 1

                for index in range(number_of_features):
                    self.weights[index] += (
                        self.learning_rate
                        * error
                        * features[index]
                    )

                self.bias += self.learning_rate * error

            if total_errors == 0:
                break


def normalize_features(cgpa, aptitude):
    """
    Scale both features approximately between 0 and 1.

    CGPA is divided by 10.
    Aptitude score is divided by 100.
    """

    return [
        cgpa / 10,
        aptitude / 100,
    ]


# Original training data
training_data = [
    [8.5, 82],
    [7.8, 75],
    [8.0, 70],
    [6.2, 52],
    [5.8, 45],
    [6.5, 55],
]

# Convert original data into normalized data
x_train = [
    normalize_features(cgpa, aptitude)
    for cgpa, aptitude in training_data
]

# 1 = Placed
# 0 = Not Placed
y_train = [1, 1, 1, 0, 0, 0]


# Create and train the model once
placement_model = Perceptron(
    learning_rate=0.1,
    epochs=1000,
)

placement_model.train(x_train, y_train)


def predict_placement(cgpa, aptitude):
    """Predict placement for a new student."""

    normalized_data = normalize_features(cgpa, aptitude)

    return placement_model.predict(normalized_data)