import sys
import re


def test():
    output = sys.stdin.read(1000000)
    
    result = bool(re.search(r'passed!', output))
    assert result == True

if __name__ == '__main__':
    test()

