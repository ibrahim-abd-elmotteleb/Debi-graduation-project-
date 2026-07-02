from flask import Flask, request, jsonify
import joblib
from wrangle_utils import clean_text  # Preprocessing function
import traceback
from embedding import embeddings
from subjectivity import predict_subjectivity
# Load model and vectorizer
model = joblib.load("models/trained_model.sav")
threshold = joblib.load("models/threeshold.pkl")
app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        review = data.get('review')

        if not review:
            return jsonify({'error': 'No review provided'}), 400

        cleaned = clean_text(review)
        subjectivity , score = predict_subjectivity(cleaned)
        if ((subjectivity == "Objective") & (score >= 0.80)):
            prediction = "هذا معلومة وليست رأي, فضلا ادخل رأي"
        else:
            vector = embeddings([cleaned])
            prob = model.predict_proba(vector)[0][1]
            prediction = int(prob >= threshold)
            prediction = "ايجابي" if prediction else "سلبي"

        return jsonify({'prediction': prediction})

    except Exception as e:
        return jsonify({'error': str(e), 'trace': traceback.format_exc()}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False, threaded=False)


