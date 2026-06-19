import pandas as pd
import matplotlib.pyplot as plt

#Phần 1: Khởi tạo và đọc dữ liệu
df = pd.read_excel("ecommerce_sales_data.xlsx")
print(df.head(7))
print(df.tail(5))
print(df.info())
print(df.describe())

#Phần 2: Khám phá làm sạch dữ liệu
print(df.isnull().sum())
df["Discount"] = df["Discount"].fillna(0)
df["CustomerID"] = df["CustomerID"].fillna("GUEST")
print(df.isnull().sum())
df["Date"] = pd.to_datetime(df["Date"])
print(df.duplicated().sum())

#Phần 3: Trích xuất và biến đổi dữ liệu
df["Revenue"] = df["Quantity"] * df["UnitPrice"] * (1 - df["Discount"])
df["Year"] = df["Date"].dt.year
df["Month"] = df["Date"].dt.month
df["DayOfWeek"] = df["Date"].dt.day_name()
def segment(price):
    if price >= 150:
        return "High"
    elif price >= 50:
        return "Medium"
    else:
        return "Low"

df["Price_Segment"] = df["UnitPrice"].apply(segment)

#Phần 4: Lọc và truy vấn dữ liệu
north_orders = df[(df["Region"]=="North") &
                  (df["Revenue"]>300)]

print(north_orders)
count_electronics = len(
    df[(df["Product_Category"]=="Electronics") &
       (df["Discount"]==0)]
)

print(count_electronics)
orders_mar_jun = df[df["Month"].between(3,6)]
print(orders_mar_jun)
top10 = df.nlargest(10,"Revenue")[
    ["OrderID","Product_Name","Revenue"]
]

print(top10)
max_quantity_order = df.loc[df["Quantity"].idxmax()]
print(max_quantity_order)

#Phần 5: Phân tích, gom nhóm và tổng hợp
revenue_region = df.groupby("Region")["Revenue"].sum()
print(revenue_region)
category_stats = df.groupby("Product_Category")[["Quantity","UnitPrice"]].mean()
print(category_stats)
monthly_orders = df.groupby("Month").size()
print(monthly_orders)
top3_customers = (
    df[df["CustomerID"]!="GUEST"]
    .groupby("CustomerID")["Revenue"]
    .sum()
    .sort_values(ascending=False)
    .head(3)
)

print(top3_customers)

#Phần 6: Trực quan hóa dữ liệu
revenue_by_category = (
    df.groupby("Product_Category")["Revenue"]
    .sum()
)

plt.figure(figsize=(8,5))
revenue_by_category.plot(kind="bar")

plt.title("Tong doanh thu theo danh muc san pham")
plt.xlabel("Danh muc san pham")
plt.ylabel("Doanh thu")
plt.xticks(rotation=45)

plt.show()
monthly_revenue = (
    df.groupby("Month")["Revenue"]
    .sum()
)

plt.figure(figsize=(8,5))
monthly_revenue.plot(kind="line", marker="o")

plt.title("Tong doanh thu theo thang")
plt.xlabel("Thang")
plt.ylabel("Doanh thu")

plt.grid(True)
plt.show()