# %%
from copy import deepcopy
from itertools import combinations

# %%
# util for time control
def string_time_to_minutes(time):
    return int(time.split(':')[0]) * 60 + int(time.split(':')[1])

# %%
input_data = {
    "minSubjectsCount": 2,
    "groups": [
        {
            "name": "프로그래밍언어",
            "gradeTime":3,
            "isMandatory": True,
            "subjects": [
                {
                    "name": "프로그래밍언어A",
                    "time": [
                        {"day": "TUE", "start": "10:30", "end": "11:45"},
                        {"day": "THU", "start": "13:30", "end": "14:45"}
                    ]
                },
                {
                    "name": "프로그래밍언어B",
                    "time": [
                        {"day": "TUE", "start": "13:30", "end": "14:45"},
                        {"day": "THU", "start": "10:30", "end": "11:45"}
                    ]
                },
                {
                    "name": "프로그래밍언어C",
                    "time": [
                        {"day": "TUE", "start": "15:00", "end": "16:15"},
                        {"day": "THU", "start": "15:00", "end": "16:15"}
                    ]
                },
            ]
        },
        {
            "name": "마케팅",
            "gradeTime":3,
            "isMandatory": False,
            "subjects": [
                {
                    "name": "마케팅A",
                    "time": [
                        {"day": "TUE", "start": "13:30", "end": "14:45"},
                        {"day": "THU", "start": "13:30", "end": "14:45"}
                    ]
                }
            ]
        },
        {
            "name": "Entrepreneurship",
            "gradeTime":3,
            "isMandatory": False,
            "subjects": [
                {
                    "name": "Entrepreneurship (최금선)",
                    "time": [
                        {"day": "THU", "start": "10:30", "end": "11:45"},
                        {"day": "THU", "start": "12:00", "end": "13:15"}
                    ]
                },
                {
                    "name": "Entrepreneurship (박병호)",
                    "time": [
                        {"day": "TUE", "start": "15:00", "end": "16:15"},
                        {"day": "TUE", "start": "16:30", "end": "17:45"}
                    ]
                },
                {
                    "name": "Entrepreneurship (김영수)A",
                    "time": [
                        {"day": "MON", "start": "15:00", "end": "16:15"},
                        {"day": "WED", "start": "15:00", "end": "16:15"},
                    ]
                },
                {
                    "name": "Entrepreneurship (김영수)B",
                    "time": [
                        {"day": "MON", "start": "16:30", "end": "17:45"},
                        {"day": "WED", "start": "16:30", "end": "17:45"},
                    ]
                }
            ]
        },
        {
            "name": "생산시스템관리",
            "gradeTime":3,
            "isMandatory": False,
            "subjects": [
                {
                    "name": "생산시스템관리(가)",
                    "time": [
                        {"day": "MON", "start": "10:30", "end": "11:45"},
                        {"day": "THU", "start": "12:00", "end": "13:15"}
                    ]
                },
                {
                    "name": "생산시스템관리(나)",
                    "time": [
                        {"day": "MON", "start": "12:00", "end": "13:15"},
                        {"day": "THU", "start": "13:30", "end": "14:45"}
                    ]
                },
                {
                    "name": "생산시스템관리(다)",
                    "time": [
                        {"day": "TUE", "start": "12:00", "end": "13:15"},
                        {"day": "THU", "start": "16:30", "end": "17:45"},
                    ]
                }
            ]
        },
    ]
}


# %%
# todo: 최소 학점으로 입력받으셈
# 1. 컴비네이션으로 전공선택 몇개 고른 경우의 수 모두 구하기 (최소 학점 넘는 경우의 수)
# 2. 3 -> 3 -> 3 등등 이런 식으로 재귀로 가면서 시간 상 가능한 경우의 수 arr에 다 추가
# 3. free_days_count을 구하고, 각 일의 free time between classes를 구한다


# %%
# 1. 컴비네이션으로 전공선택 몇개 고른 경우의 수 모두 구하기 (최소 학점 넘는 경우의 수)
combination_result = list(combinations(filter(lambda x: not x["isMandatory"], input_data["groups"]), input_data["minSubjectsCount"]))


# %%
# 2. 3 -> 3 -> 3 등등 이런 식으로 재귀로 가면서 시간 상 가능한 경우의 수 arr에 다 추가
def recursion(targetDepth: int, schedule_arr:list,result_array:list):
    if targetDepth == len(schedule_arr):
        result_array.append({
            "freeDays":[],
            "schedule": deepcopy(schedule_arr),
            "freeTimeBetweenClasses":{
                "MON": -1,
                "TUE": -1,
                "WED": -1,
                "THU": -1,
                "FRI": -1
            }
            
        })
        return
    
    # 다음 과목과 시간 겹치면 끝
    for next_subject in input_data['groups'][len(schedule_arr)]['subjects']:
        flag = True
        for next_subject_time in next_subject['time']:
            for schedule in schedule_arr: # 가지고 있는 모든 과목들 순환
                for prev_subject_time in schedule['time']:
                    if next_subject_time['day'] == prev_subject_time['day']:
                        # 겹치면 바로 끝
                        if next_subject_time['start'] < prev_subject_time['end'] and next_subject_time['end'] > prev_subject_time['start']:
                            flag = False
        if flag:
            recursion(targetDepth,[*deepcopy(schedule_arr),deepcopy(next_subject)],result_array)
result=[]
recursion(4,[],result)
print(result)

# %%
# 3. free_days을 구하고, 각 일의 free time between classes를 구한다
days = set(["MON","TUE","WED","THU","FRI"])
for idx,candidates in enumerate(result):
    print(idx)
    used_days = set()
    for subject in candidates["schedule"]:
        # print('prin t sbu')
        # print(subject)
        for time in subject['time']:
            # print(time)
            used_days.add(time['day'])
    # print(days - used_days)
    candidates["freeDays"] = list(days - used_days)


# 각 일의 free time between classes를 구한다 ** 이게 어렵네
for candidates in result:
    for day in ["MON","TUE","WED","THU","FRI"]:
        free_time_between_classes = 0
        classes_today = []
        for subject in candidates["schedule"]:
            for time in subject['time']:
                if time['day'] == day:
                    classes_today.append((subject['name'],time['start'],time['end']))
        classes_today.sort(key=lambda x:x[1])
        for idx, class_today in enumerate(classes_today):
            if idx == 0:
                continue
            free_time_between_classes += (string_time_to_minutes(
                classes_today[idx][1]
            ) - string_time_to_minutes(classes_today[idx - 1][2]))
        candidates["freeTimeBetweenClasses"][day] = free_time_between_classes

print(result)

# json으로 output, 파일로 io 하지말고 args로 io 하자.
# output