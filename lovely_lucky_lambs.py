# Lovely Lucky LAMBs
# ==================
#
# Being a henchman isn't all drudgery. Occasionally, when Commander Lambda is feeling generous, she'll hand out Lucky
# LAMBs (Lambda's All-purpose Money Bucks). Henchmen can use Lucky LAMBs to buy things like a second pair of socks,
# a pillow for their bunks, or even a third daily meal!
#
# However, actually passing out LAMBs isn't easy. Each henchman squad has a strict seniority ranking which must be
# respected - or else the henchmen will revolt and you'll all get demoted back to minions again!
#
# There are 4 key rules which you must follow in order to avoid a revolt: 1. The most junior henchman (with the least
# seniority) gets exactly 1 LAMB.  (There will always be at least 1 henchman on a team.) 2. A henchman will revolt
# if the person who ranks immediately above them gets more than double the number of LAMBs they do. 3. A henchman
# will revolt if the amount of LAMBs given to their next two subordinates combined is more than the number of LAMBs
# they get.  (Note that the two most junior henchmen won't have two subordinates, so this rule doesn't apply to them.
# The 2nd most junior henchman would require at least as many LAMBs as the most junior henchman.) 4. You can always
# find more henchmen to pay - the Commander has plenty of employees.  If there are enough LAMBs left over such that
# another henchman could be added as the most senior while obeying the other rules, you must always add and pay that
# henchman.
#
# Note that you may not be able to hand out all the LAMBs. A single LAMB cannot be subdivided. That is, all henchmen
# must get a positive integer number of LAMBs.
#
# Write a function called answer(total_lambs), where total_lambs is the integer number of LAMBs in the handout you
# are trying to divide. It should return an integer which represents the difference between the minimum and maximum
# number of henchmen who can share the LAMBs (that is, being as generous as possible to those you pay and as stingy
# as possible, respectively) while still obeying all of the above rules to avoid a revolt.  For instance, if you had
# 10 LAMBs and were as generous as possible, you could only pay 3 henchmen (1, 2, and 4 LAMBs, in order of ascending
# seniority), whereas if you were as stingy as possible, you could pay 4 henchmen (1, 1, 2, and 3 LAMBs). Therefore,
# answer(10) should return 4-3 = 1.
#
# To keep things interesting, Commander Lambda varies the sizes of the Lucky LAMB payouts: you can expect total_lambs
# to always be between 10 and 1 billion (10 ^ 9).
#
# Languages
# =========
#
# To provide a Python solution, edit solution.py
# To provide a Java solution, edit solution.java
#
# Test cases
# ==========
#
# Inputs:
#     (int) total_lambs = 10
# Output:
#     (int) 1
#
# Inputs:
#     (int) total_lambs = 143
# Output:
#     (int) 3


from math import log, floor, sqrt, ceil

from mpmath.math2 import phi


def get_generous(total_lambs):
    arr = [1, 2]
    ind = 1
    total_lambs -= 3
    while total_lambs > 0:
        to_add = arr[ind] * 2
        total_lambs -= to_add
        if total_lambs >= 0:
            arr.append(to_add)
            ind += 1
        else:
            total_lambs += to_add
            break

    if 2 * arr[len(arr) - 1] >= total_lambs >= arr[len(arr) - 1] + arr[len(arr) - 2]:
        arr.append(total_lambs)

    return len(arr)


def get_generous1(total_lambs):

    n = int(floor(log(total_lambs + 1, 2)))

    f0 = 2 ** (n - 2)
    f1 = 2 ** (n - 1)

    total_lambs -= ((2 ** n) - 1)

    if 2 * f1 >= total_lambs >= f1 + f0:
        return n + 1
    return n


# print(answer(10))
# print(answer(143))
# for i in range(10):
#     print answer(i)
#
# print(get_generous(10**9), get_generous1(10**9))
#
#
# for i in range(10 ** 9, 10 ** 9 + 1000):
#     print i
#     assert get_generous(i) == get_generous1(i), "%s != %s" % (get_generous(i), get_generous1(i),)


def binet_formula(total_lambs):
    return (phi**total_lambs - (-phi)**(-total_lambs)) / sqrt(5)


def func(n):
    return int(log(int(sqrt(5) * (n - 0.5)), 2) / log(phi, 2) - 2)


# print int(phi**(func(i + 2)) / sqrt(5) + 0.5), "here2", get_stingy(i)
# print int(phi**(func(i + 2)) / sqrt(5) + 0.5), "here2", get_stingy(i)


def get_stingy(total_lambs):
    arr = [1, 1]
    ind = 1
    total_lambs -= 2
    while total_lambs > 0:
        to_add = arr[ind] + arr[ind - 1]
        total_lambs -= to_add
        if total_lambs >= 0:
            arr.append(to_add)
            ind += 1
        else:
            total_lambs += to_add
            break

    if 2 * arr[len(arr) - 1] >= total_lambs >= arr[len(arr) - 1] + arr[len(arr) - 2]:
        arr.append(total_lambs)

    return len(arr)


def get_stingy1(total_lambs):
    # print binet_formula(i)
    f1 = int(phi**(func(total_lambs + 2)) / sqrt(5) + 0.5)
    f0 = int(phi**func(total_lambs + 1) / sqrt(5) + 0.5)
    f1_ind = func(total_lambs + 2)

    sum_n = int(phi**(f1_ind + 2) / sqrt(5) + 0.5) - 1

    total_lambs -= sum_n

    if 2 * f1 >= total_lambs >= f1 + f0:
        return f1_ind + 1
    return f1_ind


# for i in range(10, 1000):
#     print i
#     assert get_stingy(i) == get_stingy1(i), "%s != %s" % (get_stingy(i), get_stingy1(i),)


def answer(total_lambs):
    return get_stingy1(total_lambs) - get_generous1(total_lambs)
