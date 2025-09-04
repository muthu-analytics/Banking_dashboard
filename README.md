# 🏦 Banking Dashboard & Python EDA – Risk Analytics in Lending

## 📌 Problem Statement
Banks face a high risk of losing money if loans are granted to customers who cannot repay.  
The goal of this project is to build a **Power BI dashboard** and perform **Python-based exploratory data analysis (EDA)** to help minimize risk by analyzing client profiles and making data-driven lending decisions.

---

## ✅ Solution
- Built **interactive dashboards in Power BI** with KPIs for loans, deposits, client engagement, and accounts.  
- Performed **Python-based statistical analysis & visualization** to explore the dataset.  
- Provided **actionable insights** for banking operations to identify risk-prone clients and optimize decision-making.
---

## 📂 Dataset
The dataset contains information about banking clients and relationships.  
It consists of multiple interlinked tables:  

- **Banking Relationship**  
- **Client-Banking**  
- **Gender**  
- **Investment Advisor**  
- **Period**  

📌 Sample dataset is provided here → `Banking.csv`

---

## 🧹 Data Cleaning & Transformation
- Created **Engagement Timeframe** to track client duration.  
- Added **Engagement Days** using `DATEDIFF`.  
- Created **Income Band** bins:  
  - `< 100,000` → Low  
  - `< 300,000` → Mid  
- Calculated **Processing Fees** (0.05 × Loan for high fee structures).  

---

## 🧮 Key DAX Calculations
```DAX
-- Total Clients
Total Clients = DISTINCTCOUNT('Clients - Banking'[Client ID])

-- Total Loan
Total Loan = [Bank Loan] + [Business Lending] + [Credit Cards Balance]

-- Engagement Days
Engagement Days = DATEDIFF('Clients - Banking'[Joined Bank], TODAY(), DAY)

-- Total Fees
Total Fees = SUMX('Clients - Banking', [Total Loan] * 'Clients - Banking'[Processing Fees])

📊 Dashboards (Power BI)
1️⃣ Home Dashboard

Overview of total clients, loans, deposits, and accounts.
<img width="1308" height="723" alt="Screenshot 2025-09-03 061034" src="https://github.com/user-attachments/assets/87b6ab2e-44d4-4a93-9e43-2687ac6bd184" />


2️⃣ Loan Analysis

Breakdown of loans by nationality, occupation, and income band.
<img width="1290" height="725" alt="Screenshot 2025-09-03 061142" src="https://github.com/user-attachments/assets/6066e563-c0a7-4a36-8a89-859c41a8ad96" />

3️⃣ Deposit Analysis

Deposits segmented by accounts and client demographics.
<img width="1277" height="691" alt="Screenshot 2025-09-03 061211" src="https://github.com/user-attachments/assets/0c9338c8-99a3-4059-ac3f-c8b8788ea6a2" />

4️⃣ Summary Dashboard

Overall insights with KPIs and comparative analysis.
<img width="1277" height="712" alt="Screenshot 2025-09-03 061245" src="https://github.com/user-attachments/assets/09660b8b-c096-47f5-b892-912f6224a891" />


🐍 Python Analysis (EDA)

Along with Power BI dashboards, I also performed Python-based Exploratory Data Analysis (EDA) using Pandas, Matplotlib, and Seaborn.

🔹 Key Steps

Imported dataset (Banking.csv) using Pandas

Created new feature: Income Band (Low, Medium, High)

Analyzed categorical columns (Gender, Occupation, Nationality, etc.)

Plotted distributions of numerical columns

Generated correlation heatmap for numerical relationships

📊 Sample Outputs
Income Band Distribution

bins = [0,100000,300000,float('inf')]
labels = ['low','med','high']
df['Income Band'] = pd.cut(df['Estimated Income'], bins=bins, labels=labels, right=False)
df['Income Band'].value_counts().plot(kind='bar', color=['skyblue','orange','green'], edgecolor='black')

Correlation Heatmap
correlation_matrix = df[numerical_cols].corr()
sns.heatmap(correlation_matrix, annot=True, cmap='crest', fmt='.2f')

📌 Insights

Total 714 clients analyzed.

Loans worth 518M+ and deposits worth 147M+ tracked.

Private banks attracted the highest number of clients.

Loan-to-deposit ratio = 3.58, showing heavy reliance on lending.

Deposits vary strongly by income band and nationality.

🚀 Future Work

Add predictive modeling for loan defaults.

Create real-time dashboards.

Expand with geographical analysis.

🛠️ Tools Used

Power BI – Dashboard development

DAX – KPI calculations

Python 3.11+ – Data analysis

Pandas, NumPy, Matplotlib, Seaborn

CSV / Excel – Data source




