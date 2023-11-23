from server.database.mongo import data_collection
import pandas as pd
import math

async def get_data(per_page: int=20, page: int=1, from_date="2021-01-01", to_date="2024-12-31", device_id: str='C10_301'):
    data = data_collection.find(
        {"TheTime": {
        '$gte': from_date,
        '$lte': to_date,
        },
        "device_id": device_id}
    )
    data_response = []
    for i in data:
        i['_id'] = str(i['_id'])
        data_response.append(i)
    data = pd.DataFrame(data_response)
    if data.empty:
        return []
    # data = pd.read_csv('./server/data/210109.csv')
    # data['TheTime'] = pd.to_datetime(data['TheTime'])
    # data = data[(data['TheTime'] >= from_date) & (data['TheTime'] <= to_date)]
    meta = {
        "total": len(data),
        "total_page": math.ceil(len(data)/per_page),
        "current_page": page,
        "per_page": per_page
    }
    start_index = per_page * (page - 1)
    data = data.iloc[start_index:start_index + per_page]
    return {"data": data.to_dict('records'), "meta": meta}