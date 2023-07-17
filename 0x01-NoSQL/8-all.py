def list_all(mongo_collection):
    """first use of pymongo."""
    if mongo_collection.find().count() == 0:
        return []

    return mongo_collection.find()
