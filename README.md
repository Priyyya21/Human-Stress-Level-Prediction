 Live Web App
   https://human-stress-level-prediction-priyasharma.onrender.com

Project Overview
This project predicts the stress level of a human (Low, Medium, High) using behavioral, lifestyle, work, and health-related attributes — without requiring medical devices or sensitive physiological data.
Users provide inputs such as:
- Age
- Sleep Duration & Sleep Quality
- Wake Up Time & Bed Time
- Physical Activity
- Screen Time
- Caffeine Intake
- Alcohol Intake
- Smoking Habit
- Meditation Practice
- Exercise Type
- Work Hours
- Travel Time
- Social Interactions
- Blood Pressure
- Cholesterol Level
- Blood Sugar Level
- Gender, Occupation, Marital Status

The model then predicts overall human stress level as:
 Low | Medium | High

 Objective
- To develop a machine learning system capable of estimating a person’s stress level based on daily lifestyle factors — supporting mental wellness awareness and early stress risk detection.

 Machine Learning Models Used
- Multiple models were trained and compared:
 Model       	                  Accuracy	         Comments
 Random Forest Classifier	      80%	              Best performing model
 Gradient Boosting	             72%	              Stable but lower recall
 SVM                           	67%	              Underfitting issues
 Deep Learning (ANN)           	69%	              Good but not better than RF
➡️ Random Forest Classifier selected as final model

Feature Engineering & Data Processing:
Handling categorical data using Label Encoding
StandardScaler applied for numerical normalization
Class imbalance solved using SMOTE
Removed noise/outliers through EDA
Feature importance analysis to understand major stress contributors
Key Exploratory Data Insights
Higher Blood Pressure, Cholesterol & Blood Sugar → Strongly correlate with higher stress
Increased Screen Time & Work Hours raise stress risk
Meditation Practice & Physical Activity reduce stress levels
Late Bedtime + Early Wakeup → Poor stress scores
Less Social Interaction associated with high stress

Tech Stack:
Component	Technology
Machine Learning	Python, Scikit-learn
Web Framework	Flask
Data Handling	Pandas, NumPy
Visualization	Matplotlib, Seaborn
Deployment	Render Cloud Hosting
Folder Structure
 Human Stress Level Prediction
 ┣  templates
 ┃ ┗ index.html
 ┣ app.py
 ┣ model.pkl
 ┣ requirements.txt
 ┣ README.md

 How to Run Locally
# Clone the repository
git clone https://github.com/Priyyya21/Human-Stress-Level-Prediction
# Create virtual environment
python -m venv myenv
# Windows
myenv\Scripts\activate
# Mac/Linux
source myenv/bin/activate
# Install required dependencies
pip install -r requirements.txt
# Run the app
python app.py
Visit app locally at:
➡  http://127.0.0.1:5000

 Future Improvements:
Add SHAP Explainability inside the app UI
Mental health advice based on prediction result
Collect real-world user input to retrain model
Mobile-friendly redesigned interface
Add user history dashboard with stress tracking

👩‍💻 Author
Priya Sharma
B.Tech – Computer Science & Engineering
Machine Learning & Data Science Enthusiast
