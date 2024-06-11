from DataBusiness import BaseConnection


def test_returning_by_name():
    connection = BaseConnection()
    eldenring = connection.collection.find_one({'title': 'Elden Ring'})

    assert eldenring['title'] == 'Elden Ring'

def test_deleting():
    connection = BaseConnection()
    connection.embeddings.delete_many({})

    print("All deleted.")
