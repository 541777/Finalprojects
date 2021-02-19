import pytest

from . import views


def test_DiscretionarybonusA():
    total =views.Discretionarybonus(policystartdate='01/08/1983',policynum='A100013',policymember='yes')
    assert total == 1000


def test_DiscretionarybonusA1():
    total =views.Discretionarybonus(policystartdate='01/08/1996',policynum='A100014',policymember='no')
    assert total == 0

def test_DiscretionarybonusB():
    total =views.Discretionarybonus(policystartdate='10/04/1995',policynum='B100001',policymember='no')
    assert total == 0

def test_DiscretionarybonusB1():
    total =views.Discretionarybonus(policystartdate='10/04/1995',policynum='B100000',policymember='yes')
    assert total == 1000

def test_DiscretionarybonusC1():
    total =views.Discretionarybonus(policystartdate='10/04/1995',policynum='C100000',policymember='yes')
    assert total == 1000

def test_DiscretionarybonusC2():
    total =views.Discretionarybonus(policystartdate='10/04/1982',policynum='C100000',policymember='no')
    assert total == 0



