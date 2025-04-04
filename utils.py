# 根据scheduleId排序 "1-1-1", "1-1-2" ...
# 手写 O(n^3)
# def sort_schedules(schedules) -> None:
#     n = len(schedules)
#     for i in range(n):
#         sl = schedules[i]["scheduleList"]
#         m = len(sl)
#         for s in range(m):
#             for k in range(s + 1, m):
#                 phase_s, match_s = map(int, sl[s]["scheduleId"].split("-")[1:])
#                 phase_k, match_k = map(int, sl[k]["scheduleId"].split("-")[1:])
#                 if phase_s > phase_k or (phase_s == phase_k and match_s > match_k):
#                     sl[s], sl[k] = sl[k], sl[s]
#         for j in range(i + 1, n):
#             season_id_i = schedules[i]["seasonId"]
#             season_id_j = schedules[j]["seasonId"]
#             if season_id_i > season_id_j:
#                 schedules[i], schedules[j] = schedules[j], schedules[i]


# sort O(nlog(n))
def sort_schedules(schedules) -> None:
    for schedule in schedules:
        schedule['scheduleList'].sort(
            key=lambda item: tuple(map(int, item["scheduleId"].split("-")[1:]))
        )
    schedules.sort(key=lambda item: item["seasonId"])
