from collections import Counter
def solution(participant, completion):
    participant, completion = Counter(participant), Counter(completion)
    result = [key for key in participant.keys() if completion.get(key) is None or completion[key] != participant[key]]
    return result[0]
