# pricing-engine-challenge

# THRD Coding Challenge – Pricing Engine

## 💼 Overview

This project is a solution to the THRD coding challenge. It implements a simple **pricing engine** that analyzes product inventory and sales data to recommend new product prices based on real-time business logic.

## 🧾 Business Rules

The script processes product and sales data and applies the following rules:

1. **Low Stock + High Demand** → Increase price by **15%**
2. **Dead Stock** (no sales in last 30 days) → Decrease price by **30%**
3. **Overstocked Items** (quantity > 100 units) → Decrease price by **10%**
4. **Minimum Profit Rule** → Ensure at least **20% profit** over cost price

Final prices are rounded to **2 decimal places** and suffixed with "INR".

---

## 📂 Files Included

| File Name            | Description                                 |
|----------------------|---------------------------------------------|
| `pricing_engine.py`  | Main Python script implementing the logic   |
| `products.csv`       | Input CSV file with product data            |
| `sales.csv`          | Input CSV file with sales history           |
| `updated_prices.csv` | Output CSV file with updated prices         |
| `README.md`          | This documentation file                     |

---

## ⚙️ How to Run

1. Make sure you have Python 3 installed.
2. Place all files in the same directory.
3. Run the script:

```bash
python pricing_engine.py
