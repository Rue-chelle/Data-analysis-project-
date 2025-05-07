# 📊 Bank Marketing Analysis Project


This project analyzes the Bank Marketing dataset from the UCI Machine Learning Repository using **Python**, **Pandas**, and **Matplotlib**. The goal is to explore the dataset, derive insights, and visualize key trends related to customer responses to direct marketing campaigns.

## 📁 Dataset

- **Source**: [UCI Machine Learning Repository - Bank Marketing Data Set](https://archive.ics.uci.edu/ml/datasets/Bank+Marketing)
- **Format**: CSV
- **Records**: 41,188
- **Attributes**: 20 (categorical and numerical), including customer demographics and campaign outcomes

## 🎯 Objectives

- Load and explore the dataset using `pandas`
- Perform basic statistical analysis
- Visualize important features using `matplotlib` and `seaborn`
- Discover patterns in customer responses to marketing efforts

## 🔬Tasks Performed

### 📥Task 1: Load and Explore the Dataset
- Loaded CSV file with `pandas.read_csv()`
- Inspected data with `.head()`, `.info()`, and `.isnull()`
- Cleaned missing or unknown values

### Task 2: Basic Data Analysis
- Computed summary statistics using `.describe()`
- Grouped by categorical features (e.g., job, marital status) to find trends
- Observed how attributes like age, education, and call duration relate to marketing success

###  Task 3: Data Visualization
- **Bar Chart**: Subscription counts
- **Histogram**: Age distribution of clients
- **Box Plot**: Age of subscribed clients 
- **Scatter Plot**: Duration by age

### 📌 Bonus Features
- Saved all plots as `.png` files
- Automated error handling for missing files or data

## ✅ How to Run

1. Make sure you have Python 3 installed.
2. Install the required libraries:
   ```bash
   pip install pandas matplotlib seaborn

3. Run the script:

python bank_marketing_analysis.py



## Output

Cleaned dataset preview

Descriptive statistics printed to console

Visualizations saved in Plots folder


## 📚 Insights

Clients with jobs show higher subscription success.

Longer calls are more likely to lead to a subscription.

## License

This project is for educational purposes. The dataset is provided by UCI under their data use terms.

## Author

Michelle Rufaro Samuriwo (a.k.a. Alora)

---
