import pandas as pd

def fix_names(users: pd.DataFrame) -> pd.DataFrame:
    users = users.sort_values(by=["user_id"])
    for i in range(len(users)):
        users.loc[i, "name"] = users.loc[i, "name"][0].upper() + users.loc[i, "name"][1:].lower()
    return users