#!/usr/bin/python3
def islower(c):
    return ord('a') <= ord(c) <= ord('z')

print(f"a is {'lower' if islower('a') else 'upper'}")
print(f"H is {'lower' if islower('H') else 'upper'}")
print(f"A is {'lower' if islower('A') else 'upper'}")
print(f"3 is {'lower' if islower('3') else 'upper'}")
print(f"g is {'lower' if islower('g') else 'upper'}")
