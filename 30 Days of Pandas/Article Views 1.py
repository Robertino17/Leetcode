import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    dict_for_out = {"id": []}
    for i in range(len(views)):
        if views.iloc[i]["author_id"] == views.iloc[i]["viewer_id"] and views.iloc[i]["author_id"] not in dict_for_out["id"]:
            dict_for_out["id"].append(views.iloc[i]["author_id"])
    dict_for_out["id"].sort()
    return pd.DataFrame(dict_for_out)