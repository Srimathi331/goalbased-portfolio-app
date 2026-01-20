import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

class RiskProfiler:
    def __init__(self):
        self.model = None
        self._train_model()

    def _train_model(self):
        data = pd.DataFrame({
            'age': [25, 35, 45, 55, 65, 30, 40, 50, 60, 70],
            'income': [30000, 60000, 80000, 50000, 40000, 35000, 65000, 75000, 52000, 45000],
            'investment_experience': [1, 5, 10, 3, 2, 4, 6, 11, 5, 3],
            'risk_kind': [0, 1, 2, 1, 0, 0, 1, 2, 1, 0]
        })
        X = data[['age', 'income', 'investment_experience']]
        y = data['risk_kind']
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        model = LogisticRegression(max_iter=1000)
        model.fit(X_train, y_train)
        self.model = model

    def predict(self, age, income, investment_experience):
        features = [[age, income, investment_experience]]
        pred = self.model.predict(features)[0]
        risk_map = {0: "Low", 1: "Medium", 2: "High"}
        return risk_map.get(pred, "Medium")
