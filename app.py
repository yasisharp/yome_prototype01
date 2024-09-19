
from flask import Flask, render_template, request
import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing.sequence import pad_sequences
import pickle

# Load the trained LSTM model and tokenizer
model = tf.keras.models.load_model('antibody_prediction_lstm.h5')
with open('tokenizer.pkl', 'rb') as handle:
    tokenizer = pickle.load(handle)

# Load the label encoder for target predictions
with open('label_encoder.pkl', 'rb') as handle:
    label_encoder = pickle.load(handle)

# Initialize Flask app
app = Flask(__name__)

# Home route to display the input form
@app.route('/')
def home():
    return render_template('index.html')

# Route to handle predictions
@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # Get the antibody sequence from the form
        antibody_seq = request.form['antibody_sequence']

        # Tokenize and pad the input sequence
        seq = tokenizer.texts_to_sequences([antibody_seq])
        padded_seq = pad_sequences(seq, maxlen=100, padding='post')

        # Predict the target sequence
        prediction = model.predict(padded_seq)
        predicted_class = np.argmax(prediction, axis=1)
        predicted_target = label_encoder.inverse_transform(predicted_class)[0]

        # Display the prediction result
        return render_template('result.html', prediction=predicted_target)

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)
