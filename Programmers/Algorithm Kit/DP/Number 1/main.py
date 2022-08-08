def solution(N, number):
    d = [set([])]
    oper = ["+", "-", "*", "//"]
    for i in range(1, 9):
        s = set([])
        for j in range(1, i):
            for a in d[i-j]:
                for b in d[j]:
                    for k in range(4):
                        value = eval(str(a)+oper[k]+str(b))
                        if value > 0:
                            s.add(value)
        s.add(N*int('1'*i))
        if number in s:
            return i
        d.append(s)
    return -1