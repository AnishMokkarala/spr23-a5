#!/usr/bin/env python3
from calculator_adapter import run


### ADD AT LEAST TWO TESTS HERE!
assert run("1 * 2").output == "2"
assert run("3 + 2").output == "5"
###

print("All tests passed!")
