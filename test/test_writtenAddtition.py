import sys
sys.path.append('../math2remember')
from math2remember.writtenAddition import writtenAddition

def testWrittenAddtition():
    assert writtenAddition('123', '22')=='145'
    assert writtenAddition('22', '123')=='145'
    assert writtenAddition('22', '19')=='41'
    assert writtenAddition('19', '22')=='41'
    assert writtenAddition('28791', '568891')=='597682'
    assert writtenAddition('17', '2')=='19'
    assert writtenAddition('111', '0')=='111'