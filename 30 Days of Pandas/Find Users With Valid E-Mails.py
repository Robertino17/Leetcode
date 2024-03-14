import pandas as pd

def valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    users['is_invalid'] = 0
    for i in range(len(users)):
        email = users.loc[i]["mail"]
        if email[-13:] == '@leetcode.com' and email[0].isalpha() and set(email[:-13]).intersection(set('![]#($)^%=*@+&')) == set():
            users.loc[i, 'is_invalid'] = 1
    return users[users['is_invalid'] == 1].drop('is_invalid', axis=1)