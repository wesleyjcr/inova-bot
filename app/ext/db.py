from pymongo import MongoClient


def init_db():
    client = MongoClient(
        "mongodb+srv://telegram_bot:BOToperacaoFIFA2020@cluster0.3pee7.mongodb.net/inova_bot?retryWrites=true&w=majority"
    )
    db = client["inova_bot"]

    return db
