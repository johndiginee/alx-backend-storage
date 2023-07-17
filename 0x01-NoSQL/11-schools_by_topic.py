#!/usr/bin/env python3
"""MongoDB Operations with Python using pymongo."""


def schools_by_topic(mongo_collection, topic):
    """Returns the list of school having a specific topic."""
    documents = mongo_collection.find({"topics": topic})
    list_docs = [doc for doc in documents]
    return list_docs
