#KNN
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.preprocessing import StandardScaler

def knn_experiment(data_path, target_column, splits=[0.1, 0.3], ks=[3,5,7], numeric_features=None):
    data = pd.read_csv(data_path)
    
    if numeric_features:
        X = data[numeric_features]
    else:
        X = data.drop(columns=[target_column])
    y = data[target_column]

    # Scale features for better KNN performance
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    for test_size in splits:
        print(f"\n\n---- Split: {100 - test_size*100:.0f}-{test_size*100:.0f} ----")
        X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=test_size, random_state=42)

        for k in ks:
            # Try Euclidean (p=2) and Manhattan (p=1) using minkowski metric
            for p_val, metric_name in [(2, 'euclidean'), (1, 'manhattan')]:
                model = KNeighborsClassifier(n_neighbors=k, metric='minkowski', p=p_val)
                model.fit(X_train, y_train)
                y_pred = model.predict(X_test)

                print(f"\nK={k}, Metric={metric_name}")
                print("Accuracy:", accuracy_score(y_test, y_pred))
                print("Report:\n", classification_report(y_test, y_pred, zero_division=0))

# Run for glass dataset (all features except 'Type' are numeric)
knn_experiment("glassagn.csv", "Type")

# Run for fruit dataset, specify only numeric features to avoid string columns
numeric_cols_fruits = ['mass', 'width', 'height', 'color_score']
knn_experiment("fruitsagn.csv", "fruit_label", numeric_features=numeric_cols_fruits)
