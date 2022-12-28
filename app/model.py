from ext.db import init_db


db = init_db()


def count_all_documents(page):
    return db[page].count_documents({})


def insert_documents(page, data):
    return db[page].insert_one(data)


def get_course(page):
    return db[page].find_one()