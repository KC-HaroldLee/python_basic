import sampleModule, sys

def test(a, b) :
    print('sys.argv : ', sys.argv)
    sampleModule.testClass.sum(a, b)

test(5, 6)
