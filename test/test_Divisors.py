import sys, os
sys.path.append('/Users/takumi/Desktop/pydev/bamboo_test/lib')
from Divisors import Divisors
import pytest

def test_Divisors():
    d = Divisors(3, 20, 6).length
    assert type(d) is int
    assert d == 1

