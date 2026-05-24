from ml.model import predict_habit

# Wrapper function
def get_prediction(streak):

    prediction, confidence = predict_habit(
        streak,
        streak + 2
    )

    return prediction, confidence