from nose.tools import *
from src.main import *

def test_1():
    filename = 'http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3.txt'
    buffer =read_url(filename)
    eq_(len(buffer), 9506, "buffer sizes do not match")
    
def test_a2d():
    result = [[False] * 4 for _ in range(4)]
    a = a2d(4)
    eq_(a, result, "Error with a2d function")