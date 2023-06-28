import sys
input = sys.stdin.readline

while True:
    s = input().rstrip()
    if s == "":
        break
    steps = s.split(' ')
    n = len(steps)
    k, dip_index = set(), []

    for i in range(n):
        if steps[i] == "dip":
            if i > 0 and steps[i-1] == "jiggle":
                continue
            if i > 1 and steps[i-2] == "jiggle":
                continue
            if i < n-1 and steps[i+1] == "twirl":
                continue
            k.add(1)
            dip_index.append(i)

    if n < 2 or " ".join(steps[-3:]) != "clap stomp clap":
        k.add(2)

    if "twirl" in steps and "hop" not in steps:
        k.add(3)

    if n > 0 and steps[0] == "jiggle":
        k.add(4)

    if "dip" not in steps:
        k.add(5)

    if 1 in k:
        for idx in dip_index:
            steps[idx] = "DIP"
    s = " ".join(steps)

    if not k:
        print("form ok:", s)
    elif len(k) == 1:
        print("form error %d: %s" % (k.pop(), s))
    else:
        ks = sorted(list(k))
        kk = ", ".join(map(str, ks[:-1])) + " and " + str(ks[-1])
        print("form errors %s: %s" % (kk, s))