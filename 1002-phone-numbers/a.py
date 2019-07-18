KEYS = {
    1: 'ij',
    2: 'abc',
    3: 'def',
    4: 'gh',
    5: 'kl',
    6: 'mn',
    7: 'prs',
    8: 'tuv',
    9: 'wxy',
    0: 'oqz',
}

REV = {}
for n, letters in KEYS.items():
    for l in letters:
        REV[l] = str(n)

NO_SOL = 'No solution.'

# step 1
#
# 7325189087
#
# it -> 18
# your -> 9087
# reality -> 7325189
# real -> 7325
# our -> 087


# step 2
#
# 7325189087
#
# reality -> 7325189
# your -> 9087
# real -> 7325
# our -> 087
# it -> 18

def convert(s: str):
    return ''.join([REV[x] for x in s])


class Substitution:
    def __init__(self, word):
        self.word = word
        self.encoded = convert(word)


def req(number: str, substitutions: list):
    print(number)
    if len(number) == 0:
        return []

    shortest = None
    for subs in substitutions:
        if number.startswith(subs.encoded):
            res = req(number[len(subs.encoded):], substitutions)
            if res is None:
                continue
            elif shortest is None:
                shortest = [subs.word] + res
            elif len(res) + 1 < len(shortest):
                shortest = [subs.word] + res

    return shortest


while True:
    number: str = input()
    if number == '-1':
        break

    words = []
    wc = int(input())
    for _ in range(wc):
        words.append(input())

    words.sort(key=lambda x: len(x), reverse=True)

    substitutions = [Substitution(x) for x in words]

    # number = somestr + X
    # somestr -> ABC
    # 

    ps = [None for _ in range(len(number) + 1)]
    ps[-1] = []
    # print(ps)

    for i in range(len(ps) - 2, -1, -1):
        part = number[i:]

        shortest = None        
        for subs in substitutions:
            if part.startswith(subs.encoded):
                res = ps[i + len(subs.encoded)]
                if res is None:
                    continue
                elif shortest is None:
                    shortest = [subs.word] + res
                elif len(res) + 1 < len(shortest):
                    shortest = [subs.word] + res
        ps[i] = shortest

    # for i in range(0, len(ps)):
    #    print(number[i:], '-', ps[i])

    result = ps[0]

    if result:
        print(' '.join(result))
    else:
        print(NO_SOL)

    
