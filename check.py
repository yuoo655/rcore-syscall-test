

import os
import codecs
import re
import signal
import argparse

# 运行shell命令
def exec_cmd(cmd):
    text = os.popen(cmd)
    return text

# 超时计时
class TimeOutException(Exception):
    def __init__(self, *args, **kwargs):
        pass

def timeout_handler(signum, frame):
    print("timeout signal received")
    # raise TimeOutException()


def main():
    
    
    
    
    return 1

    
if __name__ == '__main__':
    main()