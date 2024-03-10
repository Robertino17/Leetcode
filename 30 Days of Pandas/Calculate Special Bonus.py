import pandas as pd

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    dict_bonus = {"bonus": []}
    employees = employees.sort_values(by=["employee_id"])
    for i in range(len(employees)):
        if employees.iloc[i]["employee_id"] % 2 == 0 or employees.iloc[i]["name"][0] == 'M':
            dict_bonus["bonus"].append(0)
        else:
            dict_bonus["bonus"].append(employees.iloc[i]["salary"])
    employees["bonus"] = dict_bonus["bonus"]
    return employees.loc[:, ["employee_id", "bonus"]]