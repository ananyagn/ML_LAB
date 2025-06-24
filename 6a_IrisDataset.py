#iris dataset
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import confusion_matrix, accuracy_score

# Load the dataset
df = pd.read_csv('Iris.csv')

# Preview the dataset
print(df.head())

# Separate features (X) and target (y)
X = df.drop('species', axis=1)  # Drop the target column (Species)
y = df['species']  # The target column

# Split the data into training and testing sets
for split_ratio in [0.1, 0.3]:
    print(f"\n---Train_Test split: {int((1-split_ratio)*100)}-{int(split_ratio*100)}---")
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=split_ratio, random_state=42)
    
    # Initialize and train the Naive Bayes model
    model = GaussianNB()
    model.fit(X_train, y_train)
    
    # Make predictions on the test set
    y_pred = model.predict(X_test)
    
    # Evaluate the model
    cm = confusion_matrix(y_test, y_pred)
    acc = accuracy_score(y_test, y_pred)
    
    # Output results
    print("Confusion Matrix:\n", cm)
    print("Accuracy:", acc * 100)
