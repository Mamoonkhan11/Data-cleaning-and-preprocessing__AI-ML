import pandas as pd

def detected_removed_outliers(df: pd.DataFrame, columns: list) -> pd.DataFrame:
    dfout = df.copy()
    for col in columns:
        if col in dfout.columns:

        # Calculate Q1, Q3, and IQR
         Q1 = dfout[col].quantile(0.25)
         Q3 = dfout[col].quantile(0.75)
         IQR = Q3 - Q1
         lower_bound = Q1 - 1.5 * IQR
         upper_bound = Q3 + 1.5 * IQR

        # Remove outliers
        dfout = dfout[(dfout[col] >= lower_bound) & (dfout[col] <= upper_bound)]

    return dfout