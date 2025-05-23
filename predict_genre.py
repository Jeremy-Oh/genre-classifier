import joblib

# Load model components
model = joblib.load('genre_classifier_model.pkl')
vectorizer = joblib.load('tfidf_vectorizer.pkl')
label_encoder = joblib.load('label_encoder.pkl')

def predict_genre(plot):
    X = vectorizer.transform([plot])
    y_pred = model.predict(X)
    genre = label_encoder.inverse_transform(y_pred)
    return genre[0]

if __name__ == "__main__":
    print("?? Movie Genre Predictor")
    print("Type a plot description below. Type 'exit' to quit.\n")

    while True:
        user_input = input("Enter movie plot: ")
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break
        genre = predict_genre(user_input)
        print(f"??? Predicted Genre: {genre}\n")