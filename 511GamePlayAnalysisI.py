import pandas as pd

def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    activity = activity.groupby(['player_id'])['event_date'].min().reset_index()
    print(activity)
    return activity.rename(columns = {'event_date':'first_login'})