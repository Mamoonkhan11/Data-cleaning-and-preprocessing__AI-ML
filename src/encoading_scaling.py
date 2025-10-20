import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler

def encoaded_scaled_data(df: pd.DataFrame) -> pd.DataFrame:
    
    # label encoding for categorical features
    if 'Sex' in df.columns:
        le = LabelEncoder()
        df['Sex'] = le.fit_transform(df['Sex'].astype(str))

    # One-hot encoding for 'Embarked' feature
    if 'Embarked' in df.columns:
        df = pd.get_dummies(df, columns=['Embarked'], drop_first=True)

    # Scaling numerical features
    numeric_cols = [col for col in ['Age', 'Fare'] if col in df.columns]
    if numeric_cols:
        scaler = StandardScaler()
        df[numeric_cols] = scaler.fit_transform(df[numeric_cols])

    return df


    