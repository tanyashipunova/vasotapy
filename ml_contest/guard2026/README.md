# Banking Fraud Detection - March 2026 Competition

I had a productive March tackling a big data challenge!

This repository contains my solution overview for a banking transaction fraud detection competition. The project focused on handling large-scale datasets and optimizing model performance using the PR-AUC metric.

## 🚀 Key Features
- **High-Performance Data Loading:** Utilized `Polars` and `Parquet` to process 600MB+ datasets efficiently on local hardware.
- **Gradient Boosting:** Implemented `CatBoost` for robust classification.
- **Incremental Training:** Developed a pipeline to train models across multiple data batches to manage memory constraints.
- **Automated Encoding:** Leveraged native string handling in CatBoost for streamlined feature engineering.

## 🛠️ Tech Stack
- **Language:** Python
- **Data Manipulation:** Polars, Pandas
- **Machine Learning:** CatBoost
- **Environment:** Jupyter Notebook

## 📊 Results & Metrics
The primary metric for this competition was **Average Precision (PR-AUC)**. 
I experimented with ~15 different model configurations with PR-AUC equals to ~0.81. Detailed parameters and their corresponding scores can be found here later.

```python
model = CatBoostClassifier(
    iterations=1000,
    learning_rate=0.05,
    depth=6,
    eval_metric='PRAUC', 
    loss_function='Logloss',
    early_stopping_rounds=50,
    auto_class_weights='Balanced',
    verbose=100,
    random_seed=42
)
```

## 📈 Learning Reflections
This project was a deep dive into Big Data management on local machines. Key learnings included:
- The efficiency of `Polars` "scanning" vs. "reading" modes.
- Managing hardware thermal/power throttling during 100% CPU load sessions.
- Understanding native categorical handling in modern GBDT libraries.
