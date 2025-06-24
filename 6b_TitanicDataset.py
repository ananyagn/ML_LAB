import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.preprocessing import LabelEncoder

# Load the Titanic dataset
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)

# Preview the dataset
print(df.head())

# Preprocess the data
# Fill missing values
df['Age'] = df['Age'].fillna(df['Age'].median())
df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])

# Label encode the 'Sex' and 'Embarked' columns
label_encoder = LabelEncoder()
df['Sex'] = label_encoder.fit_transform(df['Sex'])
df['Embarked'] = label_encoder.fit_transform(df['Embarked'])

# Select features and target variable
X = df[['Pclass', 'Sex', 'Age', 'Fare', 'Embarked']]  # Features
y = df['Survived']  # Target variable

# Split the data into training and testing sets for different ratios
for split_ratio in [0.1, 0.3]:
    print(f"\n--- Train-Test Split: {int((1 - split_ratio) * 100)}-{int(split_ratio * 100)} ---")
    
    # Split the data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=split_ratio, random_state=42)
    
    # Initialize the Naive Bayes model
    model = GaussianNB()
    
    # Train the model
    model.fit(X_train, y_train)
    
    # Make predictions on the test set
    y_pred = model.predict(X_test)
    
    # Evaluate the model
    cm = confusion_matrix(y_test, y_pred)
    acc = accuracy_score(y_test, y_pred)
    
    # Output results
    print("Confusion Matrix:\n", cm)
    print("Accuracy: {:.2f}%".format(acc * 100))
