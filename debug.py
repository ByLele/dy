# import pdb;
# pdb.set_trace()
print("debug py!")

breakpoint()

def hello():
    for i in range(10):
        i = i+2
        print(i)

hello()

import sys
print(sys.path)
sys.path.append("./utils/Setting.py")
print(sys.path)