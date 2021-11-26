import pytest
from bankoperations import withdraw, balance

@pytest.fixture()
def check():
    print('test about to start')
    yield
    print('test completed')

def test_withdraw(check):
   assert withdraw(3000) == 0

