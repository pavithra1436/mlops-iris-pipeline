import joblib
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

print("1. Loading dataset...")
iris = load_iris()
X, y = iris.data, iris.target

print("2. Training the Random Forest model...")
model = RandomForestClassifier(n_estimators=10, random_state=42)
model.fit(X, y)

print("3. Saving the model to disk...")
joblib.dump(model, "model.joblib")

print("Success! Model trained and saved as 'model.joblib'.")