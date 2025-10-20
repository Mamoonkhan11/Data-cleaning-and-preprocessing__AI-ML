import os
import matplotlib.pyplot as plt
import seaborn as sns

def save_outlier_pltb_boxplot(data, column, outpath="outputs/visuals"):
    os.makedirs(outpath, exist_ok=True)
    plt.figure(figsize=(8, 4))
    sns.boxplot(x=data[column])
    plt.title(f"Outliers Boxplot for {column}")
    filename = f"{outpath}/outliers_boxplot_{column}.png"
    plt.tight_layout()
    plt.savefig(filename)
    plt.close()
    return filename


def saved_correlation_heatmap(data, outpath="outputs/visuals"):
    os.makedirs(outpath, exist_ok=True)

    # 🔹 Only use numeric columns for correlation
    numeric_data = data.select_dtypes(include=["number"])
    corr = numeric_data.corr()

    plt.figure(figsize=(10, 8))
    sns.heatmap(corr, annot=True, fmt=".2f", cmap="coolwarm", square=True)
    plt.title("Correlation Heatmap")

    filename = f"{outpath}/correlation_heatmap.png"
    plt.tight_layout()
    plt.savefig(filename)
    plt.close()

    return filename