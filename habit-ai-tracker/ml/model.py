# Import machine learning library
from sklearn.linear_model import LogisticRegression

# Training data
# [streak, completed_days]

X = [
    [1, 2],
    [2, 4],
    [3, 5],
    [5, 8],
    [7, 10],
    [10, 15]
]

# Output labels
# 1 = likely to complete tomorrow
# 0 = likely to fail

y = [0, 0, 0, 1, 1, 1]

# Create model
model = LogisticRegression()

# Train model
model.fit(X, y)


# Prediction function
def predict_habit(streak, completed_days):

    # Prepare input
    data = [[streak, completed_days]]

    # Predict result
    prediction = model.predict(data)

    # Predict probability
    probability = model.predict_proba(data)

    # Get confidence score
    confidence = probability[0][1] * 100

    # Return prediction and confidence
    return prediction[0], round(confidence, 2)