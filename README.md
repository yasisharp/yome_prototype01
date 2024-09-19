
# Yome Bio Prototype

## Goal
The goal of this project is to develop an in silico prototype for Yome Bio's AI-driven antibody discovery engine. This web-based tool allows users to input an antibody sequence and receive predictions of the target sequence using an LSTM-based machine learning model.

## Scientific Method
We employ a computational approach using machine learning to predict antibody-target interactions. Antibody sequences are tokenized, and an LSTM neural network is trained on preprocessed antibody-target interaction data to learn patterns and predict target specificity.

## Model Details
### LSTM Model
- **Embedding Layer**: Converts the tokenized antibody sequence into dense vectors for input.
- **LSTM Layer**: The core of the model that captures sequential dependencies in the antibody sequences.
- **Dense Layers**: A fully connected layer for classification, which predicts the target sequence.
- The model was trained on antibody-target interaction data, achieving an accuracy of over 80%.

### Data Sources
We sourced antibody-target data from publicly available datasets, specifically from the **IEDB (Immune Epitope Database)**.

## How to Run

### 1. Automated Setup (Linux)
To automatically set up the environment, you can use the provided `setup.sh` script. It will install the necessary dependencies, create a virtual environment, and install required Python packages.

1. Navigate to the project directory and run the following command:
   ```bash
   ./setup.sh
   ```

2. Activate the virtual environment:
   ```bash
   source venv/bin/activate
   ```

3. Run the Flask App:
   ```bash
   python app.py
   ```

4. Open your browser and go to `http://127.0.0.1:5000/` to use the interface.

### 2. Manual Setup (For Other Environments)
Alternatively, you can manually install dependencies and run the app.

1. Install Dependencies
   To install the required Python packages, run:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the Flask App:
   ```bash
   python app.py
   ```

3. Open your browser and go to `http://127.0.0.1:5000/` to use the interface.

### 3. Input Format
Input an antibody sequence using the standard 1-letter amino acid code (e.g., "KPLKPVKPKS"), and the system will predict the target sequence.
