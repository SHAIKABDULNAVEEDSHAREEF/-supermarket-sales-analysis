"""Supermarket Sales Analysis - Python (pandas + matplotlib)
Input : supermarket_sales.csv  (export of the Google Sheet, 500 rows)
Output: printed results + 4 chart images (PNG)
"""
import pandas as pd
import matplotlib.pyplot as plt

# ---------- 1. Load data ----------
df = pd.read_csv("supermarket_sales.csv", parse_dates=["Date"])
print("Rows, columns:", df.shape)

# ---------- 2. Data quality checks ----------
print("Missing values:", df.isna().sum().sum())
print("Duplicate invoice IDs:", df["Invoice ID"].duplicated().sum())

# ---------- 3. Verify Sales = Quantity x Unit Price ----------
df["Calc Sales"] = df["Quantity"] * df["Unit Price"]
mismatch = ((df["Calc Sales"] - df["Sales"]).abs() > 0.02).sum()
print("Rows where Sales != Quantity x Unit Price:", mismatch)

# ---------- 4. Key metrics ----------
print("Total sales:", round(df["Sales"].sum(), 2))
print("Average sales per transaction:", round(df["Sales"].mean(), 2))
print("Average rating:", round(df["Rating"].mean(), 2))

# ---------- 5. Group and summarize ----------
top_products = df.groupby("Product")["Sales"].sum().sort_values(ascending=False)
by_branch = df.groupby(["Branch", "City"])["Sales"].agg(["sum", "count", "mean"]).round(2)
by_category = df.groupby("Category")["Sales"].sum().sort_values(ascending=False)
payments = df["Payment"].value_counts()
by_customer = df.groupby("Customer Type")["Sales"].agg(["mean", "count"]).round(2)
monthly = df[df["Date"] < "2026-07-01"].groupby(df["Date"].dt.strftime("%b"))["Sales"].sum()
monthly = monthly.reindex(["Jan", "Feb", "Mar", "Apr", "May", "Jun"])

print("\nTop 5 products:\n", top_products.head(5).round(2))
print("\nBy branch:\n", by_branch)
print("\nBy category:\n", by_category.round(2))
print("\nPayment methods:\n", payments)
print("\nMember vs Normal:\n", by_customer)
print("\nMonthly sales:\n", monthly.round(2))

# ---------- 6. Charts ----------
def clean(ax):
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

top8 = top_products.head(8).sort_values()
fig, ax = plt.subplots(figsize=(6.5, 3.4))
ax.barh(top8.index, top8.values, color="#1F4E79")
ax.set_title("Top 8 Products by Sales")
clean(ax); fig.tight_layout(); fig.savefig("chart_products.png", dpi=160); plt.close(fig)

branch_sales = df.groupby("City")["Sales"].sum().sort_values(ascending=False)
fig, ax = plt.subplots(figsize=(6.5, 3.2))
ax.bar(branch_sales.index, branch_sales.values, color="#1F4E79")
ax.set_title("Sales by Branch / City")
clean(ax); fig.tight_layout(); fig.savefig("chart_branch.png", dpi=160); plt.close(fig)

fig, ax = plt.subplots(figsize=(6.5, 3.2))
ax.bar(by_category.index, by_category.values, color="#1F4E79")
ax.set_title("Sales by Category")
plt.setp(ax.get_xticklabels(), rotation=25, ha="right")
clean(ax); fig.tight_layout(); fig.savefig("chart_category.png", dpi=160); plt.close(fig)

fig, ax = plt.subplots(figsize=(6.5, 3.2))
ax.plot(monthly.index, monthly.values, marker="o", color="#1F4E79")
ax.set_title("Monthly Sales (Jan-Jun 2026)")
clean(ax); fig.tight_layout(); fig.savefig("chart_monthly.png", dpi=160); plt.close(fig)
print("\nCharts saved.")
