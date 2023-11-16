from server.database.mongo import data_collection

async def get_data():
    res = await data_collection.find_one({}, {'_id': 0})
    return res