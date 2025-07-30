 🩺 Indian Liver Disease Predictor




📘 Project Overview
This project aims to predict liver disease in Indian patients using various biochemical and demographic features.
I trained multiple machine learning models including:

XGBoost
LightGBM
CatBoost
Random Forest



✅ LightGBM emerged as the best performer with an accuracy of 85%.




📊 Dataset
I used the Indian Liver Patient Dataset (ILPD) from the UCI Machine Learning Repository.



🧬 Features:
Age
Gender
Total Bilirubin
Direct Bilirubin
Alkaline Phosphotase
Alamine Aminotransferase
Aspartate Aminotransferase
Total Proteins
Albumin
Albumin and Globulin Ratio



🎯 Target:
1 → Liver Disease present
0 → No Liver Disease




⚙️ Data Preprocessing & Exploration

Handled missing/null values (Albumin & A/G Ratio)
Encoded categorical data (Gender)
Normalized continuous variables
Performed correlation analysis, distribution plots, and feature importance
Removed the outliers





🤖 Model Training & Evaluation
We trained and evaluated the following models:

Model	Accuracy
Random Forest	82%
XGBoost	84%
CatBoost	83%
LightGBM	85%




✅ Why LightGBM?
Highest test accuracy
Fast training time
Lower memory usage
Less overfitting → Better generalization




📏 Evaluation Metrics Used:

Accuracy
Precision, Recall, F1-score
Confusion Matrix





💾 Model Saving
The best-performing model (LightGBM) was saved using joblib:

bash
Copy
Edit
model/liver_disease_lgbm.pkl



🚀 Deployment

Built with Streamlit
Hosted on Hugging Face Spaces
Users can enter patient data via web form and get instant predictions




🔗 Live Demo:
👉 https://huggingface.co/spaces/BaburauKrishna/Indian-Liver-Patient




🛠️ Tech Stack

Language: Python 🐍
Framework: Streamlit
Deployment: Hugging Face Spaces

ML Libraries:
LightGBM, XGBoost, CatBoost, scikit-learn, pandas, matplotlib, seaborn





🧪 How to Run Locally
bash
Copy
Edit


# Clone the repository
git clone https://github.com/KrishnaPodu/indian-liver-predictor.git
cd indian-liver-predictor


# Install required packages
pip install -r requirements.txt



# Launch the Streamlit app
streamlit run app.py
🙌 Acknowledgements
Dataset: UCI ML Repository

Libraries: scikit-learn, LightGBM, XGBoost, CatBoost, pandas, matplotlib, seaborn

UI Framework: Streamlit




