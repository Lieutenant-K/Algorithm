def solution(lottos, win_nums):
    answer = []
    grade = [6] + list(range(1, 7))[::-1]
    correct = len([True for a in lottos for b in win_nums if a == b])
    zero = lottos.count(0)
    return [grade[correct+zero],grade[correct]]