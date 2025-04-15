import numpy as np
from sklearn.tree import DecisionTreeClassifier

# Toy training data
X_train = np.array([[100, 0], [120, 0], [130, 1], [150, 1]])
y_train = np.array([0, 0, 1, 1])

model = DecisionTreeClassifier()

model.fit(X_train, y_train)

# Toy test data
X_test = np.array([[140, 1], [110, 0]])
y_pred = model.predict(X_test)

# Print the predictions
for i, prediction in enumerate(y_pred):
    if prediction == 0:
        print(f"Sample {i + 1}")
    else:
        print(f"Sample {i + 1}")
