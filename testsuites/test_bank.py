import pytest
from bankoperations import withdraw, balance
from operations import *

'''
@pytest.fixture()
def check():
    print('test about to start')
    yield
    print('test completed')

def test_withdraw(check):
   assert withdraw(3000) == 0
'''


#Parametrize test cases

@pytest.mark.parametrize('x,y,ans',[(10,20,30),(40,50,90)])
def test_add(x,y,ans):
    assert add(x,y) == ans

@pytest.mark.parametrize('amount,ans',[(2000,1000),(500,500)])
def test_withdraw(amount,ans):
    assert withdraw(amount) == ans
