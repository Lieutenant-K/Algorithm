from collections import defaultdict
def solution(id_list, report, k):
    reported_count = defaultdict(int)
    reporting_id = defaultdict(list)
    for report in set(report):
        report_id, reported_id = report.split(" ")
        reported_count[reported_id] += 1
        reporting_id[report_id].append(reported_id)
    answer = [len([1 for report_id in reporting_id[id] if reported_count[report_id] >= k]) for id in id_list]
    return answer
