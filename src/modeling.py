import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, roc_auc_score
import matplotlib.pyplot as plt
import seaborn as sns
import os

def train_random_forest(df: pd.DataFrame, feature_cols: list[str], target_col: str = "churn", save_plot_path: str = "outputs/feature_importance.png"):
    # Prepare data
    X = df[feature_cols]
    y = df[target_col]

    # Split data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train model
    model = RandomForestClassifier(random_state=42)
    model.fit(X_train, y_train)

    # Evaluate model
    y_pred = model.predict(X_test)
    y_prob = model.predict_proba(X_test)[:, 1]

    print("Classification Report:")
    print(classification_report(y_test, y_pred))

    auc_score = roc_auc_score(y_test, y_prob)
    print(f"AUC Score: {auc_score:.4f}")

    # Feature importances
    importances = pd.Series(model.feature_importances_, index=feature_cols).sort_values(ascending=False)

    # Plot and save
    plt.figure(figsize=(10, 6))
    sns.barplot(x=importances.values, y=importances.index)
    plt.title("Feature Importances")
    plt.tight_layout()
    os.makedirs(os.path.dirname(save_plot_path), exist_ok=True)
    plt.savefig(save_plot_path)
    plt.close()

    print(f"\n📊 Feature importance chart saved to: {save_plot_path}")
