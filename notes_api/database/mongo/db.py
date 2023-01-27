import pymongo


async def connect(connection_string: str) -> None:
    client = pymongo.MongoClient(connection_string)
