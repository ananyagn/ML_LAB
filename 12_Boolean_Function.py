# Boolean Functions
import numpy as np

def step_function(z):
    return 1 if z >= 0 else 0

def perceptron(inputs, weights, bias):
    summation = np.dot(inputs, weights) + bias
    return step_function(summation)

def train_perceptron(inputs, targets, weights, bias, learning_rate, epochs):
    for _ in range(epochs):
        for i in range(len(inputs)):
            prediction = perceptron(inputs[i], weights, bias)
            error = targets[i] - prediction
            weights += learning_rate * error * np.array(inputs[i])
            bias += learning_rate * error
    return weights, bias

def main():
    # AND Gate
    and_inputs = [[0, 0], [0, 1], [1, 0], [1, 1]]
    and_targets = [0, 0, 0, 1]
    and_weights = [0.0, 0.0]  # Initialize weights to zero
    and_bias = 0.0
    and_learning_rate = 0.1
    and_epochs = 10

    trained_and_weights, trained_and_bias = train_perceptron(and_inputs, and_targets, and_weights, and_bias, and_learning_rate, and_epochs)

    print("AND Gate:")
    for inp in and_inputs:
        output = perceptron(inp, trained_and_weights, trained_and_bias)
        print(f"Input: {inp}, Output: {output}")

    # OR Gate
    or_inputs = [[0, 0], [0, 1], [1, 0], [1, 1]]
    or_targets = [0, 1, 1, 1]
    or_weights = [0.0, 0.0]
    or_bias = 0.0
    or_learning_rate = 0.1
    or_epochs = 10

    trained_or_weights, trained_or_bias = train_perceptron(or_inputs, or_targets, or_weights, or_bias, or_learning_rate, or_epochs)

    print("\nOR Gate:")
    for inp in or_inputs:
        output = perceptron(inp, trained_or_weights, trained_or_bias)
        print(f"Input: {inp}, Output: {output}")

if __name__ == "__main__":
    main()
