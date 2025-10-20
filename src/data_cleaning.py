import pandas as pd

def cleaned_data(df: pd.DataFrame) -> pd.DataFrame:
        
        # Fill missing Age values with the mean age
        if 'Age' in df.columns:
            df['Age'].fillna(df['Age'].mean())

        # Fill missing Embarked values with the mode
        if 'Embarked' in df.columns:   
            df['Embarked'].fillna(df['Embarked'].mode()[0])

        # Drop unnecessary columns
        if 'Cabin' in df.columns:
            df.drop(columns=['Cabin'], inplace=True, errors='ignore')

        return df