import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 
import os


# setting style for better visuals
sns.set_theme(style="whitegrid")

#datafile path
data_file="bank-additional-full.csv"

#checking existance of file
if not os.path.exists(data_file): 
    print(f"Error: {data_file} not found in this current director.")
    exit()

#load dataset
df = pd.read_csv(data_file, sep= ';')

#log file to store analysis results
with open("bank_marketing_.txt", "w") as log:

# Display first 5 rows
    log.write("First 5 rows of the dataset:\n")
    log.write(df.head().to_string())

#Display dataset information
    log.write("Dataset Information:\n")
    df.info(buf=log)
    log.write("\n")

#check for missing values
    log.write("Missing values:\n")
    log.write(str(df.isnull().sum())+ "\n\n")

#Display descriptive stats
    log.write("Descriptive statistics:\n")
    log.write(str(df.describe(include='all')) + "\n\n")

#Analyse the distribution of the target variable
    log.write("Target Varable Distribution(y):\n")
    log.write(str(df['y'].value_counts()) + "\n\n")


#Directory to save plots:
plots_dir ="plots"
os.makedirs(plots_dir, exist_ok=True)

#1, Bar plot: Subscription counts
plt.figure(figsize=(6,4))
sns.countplot(data=df, x='y',palette='Set2')
plt.title("Subscription Counts")
plt.xlabel("Subscribed")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig(os.path.join(plots_dir,"Subscription_counts.png"))
plt.close()

#2, Histogram: Age distribution 
plt.figure(figsize=(8,5))
sns.histplot(data=df, x='age',bins=30, kde=True,color='skyblue')
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig(os.path.join(plots_dir,"Age_distribution.png"))
plt.close()

#3,Box plot: Age vs Subscription
plt.figure(figsize=(8,5))
sns.boxplot (data=df,x='y',y='age', palette='Pastel1')
plt.title("Age vs Subscription")
plt.xlabel("Subscribed")
plt.ylabel("Age")
plt.tight_layout()
plt.savefig(os.path.join(plots_dir,"Age vs Subscription.png"))
plt.close()

#4,Scatter plot Call duration vs age
plt.figure(figsize=(10,6))
sns.scatterplot (data=df,x='age',y='duration', hue='y',alpha=0.6)
plt.title("Call Duration vs Age (by Subscription outcome)")
plt.xlabel("Age")
plt.ylabel("Call Duration (seconds)")
plt.tight_layout()
plt.savefig(os.path.join(plots_dir,"Age vs Call Duration.png"))
plt.close()

print("Analysis Complete. Results saved in 'bank_marketing_.txt' and plots saved in 'plots' directory")



