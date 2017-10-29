"""
The cake is not a lie. Forgot to copy the question....
My bad................................................
"""


def answer(s=''):
    # your code goes here

    res = 0

    for next_div in range(1, len(s) + 1):
        if len(s) % next_div == 0:
            rep_part = s[:next_div]
            temp_str = rep_part * int(len(s) / next_div)
            if temp_str == s:
                res = len(s) / next_div
                break

    return int(res)


print(answer("abcabcabcabc"))
print(answer("abccbaabccba"))
print(answer("dfghjklzxcvbn"))
