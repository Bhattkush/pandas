# 📊 Pandas Data Analysis Project

This project demonstrates the core concepts of **Pandas** for data analysis and manipulation in Python.
It includes working with **Series, DataFrames, handling missing values, filtering, grouping, and merging datasets**.

---

## 🚀 Features

* Load data from CSV/Excel files
* Select and filter rows/columns
* Handle missing data (`isnull`, `dropna`, `fillna`)
* Perform aggregation (`mean`, `sum`, `count`)
* GroupBy operations
* Merge and concatenate multiple datasets
* Export results to CSV/Excel

---

## 🛠️ Installation

1. Clone this repository:

```bash
git clone https://github.com/yourusername/pandas-project.git
```

2. Navigate into the folder:

```bash
cd pandas-project
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 📌 Usage

Run the example notebook or Python script:

```bash
python analysis.py
```

Example:

```python
import pandas as pd  

data = {
    "Name": ["Kush", "Ravi", "Aman"],
    "Age": [20, 19, 22],
    "City": ["Ahmedabad", "Delhi", "Mumbai"]
}
df = pd.DataFrame(data)

print(df[df["Age"] > 20])
```

Output:

```
   Name  Age    City
2  Aman   22  Mumbai
```

---

## 📂 Dataset

The dataset used in this project is a sample CSV file with columns: `Name, Age, City`.
You can replace it with your own dataset.

---

## 📸 Sample Output

![screenshot](screenshot.png)

---

## 🤝 Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you’d like to change.

---

## 📜 License

This project is licensed under the MIT License.
