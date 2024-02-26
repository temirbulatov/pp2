def sntocam(word):
        import re
        return ''.join(x.capitalize() or '_' for x in word.split('_'))

print(sntocam('today_i_passed_lin_alg_midterm'))