#!/usr/bin/env python3
# ==============================================================
# FizzBuzz Challenge Solution
# ==============================================================
# Author: Dr. Saad Laouadi
# Repository: Code Challenges 🧠
# Language: Python
# ==============================================================
# Description:
# This script solves the classic FizzBuzz problem. It prints the
# numbers from 1 to 50, but for multiples of 3, it prints "Fizz",
# for multiples of 5, it prints "Buzz", and for multiples of both
# 3 and 5, it prints "FizzBuzz".
#
# Goal:
# Practice and master the use of conditionals and loops in Python.
# ==============================================================


# ==============================================================
# FizzBuzz Challenge Solution (Simple Conditionals)
# ==============================================================

for num in range(1, 51):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)


# ==============================================================
# FizzBuzz Challenge Solution (String Concatenation)
# ==============================================================

for num in range(1, 51):
    output = ""
    if num % 3 == 0:
        output += "Fizz"
    if num % 5 == 0:
        output += "Buzz"
    print(output or num)


# ==============================================================
# FizzBuzz Challenge Solution (Dictionary Mapping)
# ==============================================================

fizzbuzz_dict = {3: "Fizz", 5: "Buzz"}

for num in range(1, 51):
    output = "".join([value for key, value in fizzbuzz_dict.items() if num % key == 0])
    print(output or num)
