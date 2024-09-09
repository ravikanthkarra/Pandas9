import pandas as pd

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    if len(orders) == 0:
        return pd.DataFrame([], columns = ['customer_number'])
    ord = orders.groupby('customer_number')['order_number'].count().reset_index(name = 'cnt')
    ord = ord[ord['cnt'] == ord['cnt'].max()]
    print(ord)
    df = pd.DataFrame([ord.iloc[0][0]]).rename(columns = {0: 'customer_number'})
    return df