import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    customers["is_order"] = customers["id"].apply(lambda x: 1 if x in orders["customerId"].unique() else 0)
    mask = customers["is_order"] == 0
    customers["Customers"] = customers["name"]
    return customers.loc[mask, ["Customers"]]