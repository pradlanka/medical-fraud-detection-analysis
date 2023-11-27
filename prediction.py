import joblib
def predict(data):
    clf = joblib.load("cb_modeltop5.joblib”")
    return clf.predict(data)