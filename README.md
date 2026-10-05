# Supermarket Sales Analysis

Data analytics project analyzing **500 supermarket transactions (Jan to Jul 2026)** across 4 branches to find what drives sales, how customers pay and spend, and where the business can act.

**Tools:** Python (pandas, matplotlib) | Google Sheets | Microsoft Word (report)

## Business Questions
- Which product generates the highest sales?
- Which branch and category perform best?
- What is the most popular payment method?
- Do Members spend more than Normal customers?
- What is the average customer rating, and how do sales change over time?

## Dataset
`data/supermarket_sales.csv` has 500 transactions with these columns: Invoice ID, Date, Branch, City, Customer Type, Gender, Product, Category, Quantity, Unit Price, Payment, Rating, Sales.

Source: [Google Sheet](https://docs.google.com/spreadsheets/d/1QIX__4VObHFMEXnRM2xJyXmB5JAB2peHrJcQ41_U9TE/edit?usp=sharing)

## Approach
1. Loaded the data and parsed dates
2. Checked for missing values and duplicate invoice IDs (none found)
3. Verified `Sales = Quantity x Unit Price` on all 500 rows (all matched)
4. Grouped and summarized by product, branch, category, payment, customer type and month
5. Visualized the results and wrote business recommendations

## Key Findings
| Metric | Result |
|---|---|
| Total sales | ₹2,44,411.08 |
| Average per transaction | ₹488.82 |
| Top product | Cheese (₹27,906), narrowly ahead of Coffee (₹27,695) and Shampoo (₹27,497) |
| Top branch | C - Mumbai (₹72,469, about 30% of sales, 143 transactions) |
| Top category | Beverages (₹56,108, about 23% of sales); lowest is Bakery (₹6,516) |
| Payments | Evenly split: UPI 127, Net Banking 126, Card 125, Cash 122 |
| Members vs Normal | Members avg ₹483 vs Normal ₹497 (about 3% lower); Members are 59% of transactions |
| Average rating | 3.99 / 5 |
| Monthly trend | Peak in April (₹52,570), lowest in February (₹30,068) |

### Charts
![Top products](charts/products.png)
![Sales by branch](charts/branch.png)
![Sales by category](charts/category.png)
![Monthly sales](charts/monthly.png)

## Business Recommendations
- Keep more stock of Beverages, Cheese, Coffee and Shampoo, which drive the most revenue.
- Study Mumbai's product mix and footfall and apply it in Bengaluru, which has the lowest average transaction (₹466).
- Support all payment methods equally, since UPI leads by only one transaction.
- Members do not spend more per visit, so use basket-size offers (bundles, minimum-spend rewards) instead of plain discounts.
- Review Bakery and Vegetables, which have low sales value, to decide whether to promote or reduce them.

## Limitations
The dataset has no currency or cost column, so values are assumed to be in rupees and profit could not be analyzed. July contains only 1 July, so it is left out of the monthly trend.

## Project Structure
```
supermarket-sales-analysis/
├── data/supermarket_sales.csv
├── src/supermarket_analysis.py
├── charts/                      # generated PNG charts
├── report/Supermarket_Sales_Analysis.docx
├── requirements.txt
└── README.md
```

## How to Run
```bash
git clone https://github.com/SHAIKABDULNAVEEDSHAREEF/supermarket-sales-analysis.git
cd supermarket-sales-analysis
pip install -r requirements.txt
python src/supermarket_analysis.py
```
The script prints all results and saves the charts to `charts/`.

## Author
**Shaik Abdul Naveed Shareff**
[LinkedIn](https://linkedin.com/in/shaik-naveed-514895268) | [GitHub](https://github.com/SHAIKABDULNAVEEDSHAREEF)
