from server.database.mongo import data_collection

async def get_data():
    res = data_collection.find_one()
    return res