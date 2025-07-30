🩺 Indian Liver Disease Predictor
📘 Project Overview
This project aims to predict liver disease in Indian patients using various biochemical and demographic features. Using machine learning algorithms such as XGBoost, LightGBM, CatBoost, and Random Forest, we evaluate which model performs best in classifying liver disease presence.

The final model, LightGBM, achieved an accuracy of 85%, making it the best performer on our dataset.

📊 Dataset
We used the publicly available Indian Liver Patient Dataset (ILPD) from the UCI Machine Learning Repository.

🔗 Download Dataset
Features include:

Age

Gender

Total Bilirubin

Direct Bilirubin

Alkaline Phosphotase

Alamine Aminotransferase

Aspartate Aminotransferase

Total Proteins

Albumin

A/G Ratio
... and the target: Liver Disease (1 = positive, 0 = negative)

⚙️ Data Preprocessing and Exploration
Loaded and cleaned missing/null values (particularly in the Albumin and A/G Ratio columns).

Encoded categorical features (Gender) using binary encoding.

Normalized numerical features where appropriate.

Performed correlation analysis and basic EDA using matplotlib and seaborn.

🤖 Model Training and Evaluation
We trained and tested four popular classification models:

Model	Accuracy
Random Forest	82%
XGBoost	84%
CatBoost	83%
LightGBM	85%

✅ Why LightGBM?
LightGBM was chosen due to:

The highest test accuracy (85%)

Fast training time and lower memory usage

Better generalization (less overfitting)

Each model was trained on an 80-20 train-test split and evaluated using:

Accuracy

Confusion matrix

Precision, Recall, and F1-score

🧠 Model Saving
The best-performing model (LightGBM) was serialized and saved as:

bash
Copy
Edit
model/liver_disease_lgbm.pkl
We used joblib for efficient model serialization.

🚀 Deployment
The application is deployed using Streamlit and hosted on Hugging Face Spaces.

Users can enter patient data through a simple web form and receive predictions in real-time.

🖥️ Tech Stack
Language: Python

Framework: Streamlit

Deployment: Hugging Face Spaces

ML Libraries: LightGBM, XGBoost, CatBoost, scikit-learn, pandas

🧪 How to Run Locally
bash
Copy
Edit
# Clone the repo
git clone https://github.com/KrishnaPodu/indian-liver-predictor.git
cd indian-liver-predictor

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
🌐 Live Demo
https://huggingface.co/spaces/BaburauKrishna/Indian-Liver-Patient
