from src.flask_app.main import home, dummy_data, check_secrets

def test_home():
    assert home() == 'initiated successfully!'
    
def test_checkSecret():
    assert check_secrets() == 'OK'

'''    
def  test_dummyData():
    assert dummy_data() == "{
        'title': 'struggle',
        'body': 'you can never dared imagine how it will hit you.'
    }"
'''