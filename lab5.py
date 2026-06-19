import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel("ecommerce_sales_data.xlsx")

print(df.head(7))

print(df.tail(5))

print(df.info())

print(df.describe())