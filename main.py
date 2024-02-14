from copy import deepcopy
from itertools import combinations


# util for time control
def string_time_to_minutes(time):
    return int(time.split(":")[0]) * 60 + int(time.split(":")[1])


input_data = {
    "minSubjectsCount": 2,
    "groups": [
        {
            "name": "프로그래밍언어",
            "gradeTime": 3,
            "isMandatory": True,
            "subjects": [
                {
                    "name": "프로그래밍언어A",
                    "time": [
                        {"day": "TUE", "start": "10:30", "end": "11:45"},
                        {"day": "THU", "start": "13:30", "end": "14:45"},
                    ],
                },
                {
                    "name": "프로그래밍언어B",
                    "time": [
                        {"day": "TUE", "start": "13:30", "end": "14:45"},
                        {"day": "THU", "start": "10:30", "end": "11:45"},
                    ],
                },
                {
                    "name": "프로그래밍언어C",
                    "time": [
                        {"day": "TUE", "start": "15:00", "end": "16:15"},
                        {"day": "THU", "start": "15:00", "end": "16:15"},
                    ],
                },
            ],
        },
        {
            "name": "마케팅",
            "gradeTime": 3,
            "isMandatory": False,
            "subjects": [
                {
                    "name": "마케팅A",
                    "time": [
                        {"day": "TUE", "start": "13:30", "end": "14:45"},
                        {"day": "THU", "start": "13:30", "end": "14:45"},
                    ],
                }
            ],
        },
        {
            "name": "Entrepreneurship",
            "gradeTime": 3,
            "isMandatory": False,
            "subjects": [
                {
                    "name": "Entrepreneurship (최금선)",
                    "time": [
                        {"day": "THU", "start": "10:30", "end": "11:45"},
                        {"day": "THU", "start": "12:00", "end": "13:15"},
                    ],
                },
                {
                    "name": "Entrepreneurship (박병호)",
                    "time": [
                        {"day": "TUE", "start": "15:00", "end": "16:15"},
                        {"day": "TUE", "start": "16:30", "end": "17:45"},
                    ],
                },
                {
                    "name": "Entrepreneurship (김영수)A",
                    "time": [
                        {"day": "MON", "start": "15:00", "end": "16:15"},
                        {"day": "WED", "start": "15:00", "end": "16:15"},
                    ],
                },
                {
                    "name": "Entrepreneurship (김영수)B",
                    "time": [
                        {"day": "MON", "start": "16:30", "end": "17:45"},
                        {"day": "WED", "start": "16:30", "end": "17:45"},
                    ],
                },
            ],
        },
        {
            "name": "생산시스템관리",
            "gradeTime": 3,
            "isMandatory": False,
            "subjects": [
                {
                    "name": "생산시스템관리(가)",
                    "time": [
                        {"day": "MON", "start": "10:30", "end": "11:45"},
                        {"day": "THU", "start": "12:00", "end": "13:15"},
                    ],
                },
                {
                    "name": "생산시스템관리(나)",
                    "time": [
                        {"day": "MON", "start": "12:00", "end": "13:15"},
                        {"day": "THU", "start": "13:30", "end": "14:45"},
                    ],
                },
                {
                    "name": "생산시스템관리(다)",
                    "time": [
                        {"day": "TUE", "start": "12:00", "end": "13:15"},
                        {"day": "THU", "start": "16:30", "end": "17:45"},
                    ],
                },
            ],
        },
    ],
}


# 1. 컴비네이션으로 전공선택 몇개 고른 경우의 수 모두 구하고 앞에 필수과목 붙여넣음.
# 최소 과목 ~ 최대과목 수까지 돌림.
combination_result = []
mandatory_subjects = list(filter(lambda x: x["isMandatory"], input_data["groups"]))
not_mandatory_subjects = list(
    filter(lambda x: not x["isMandatory"], input_data["groups"])
)

for not_mandatory_subjects_count in range(
    input_data["minSubjectsCount"], len(not_mandatory_subjects) + 1
):
    combination_result += map(
        lambda x: mandatory_subjects + list(x),
        combinations(
            not_mandatory_subjects,
            not_mandatory_subjects_count,  # 선택 과목이 선택될 값
        ),
    )

result_by_combination = []

# 2. 각 경우의 수마다 모든 조합을 구한다.
for combination_candidate in combination_result:

    def recursion(targetDepth: int, schedule_arr: list, result_array: list):
        if targetDepth == len(schedule_arr):
            result_array.append(
                {
                    "freeDays": [],
                    "schedule": deepcopy(schedule_arr),
                    "freeTimeBetweenClasses": {
                        "MON": -1,
                        "TUE": -1,
                        "WED": -1,
                        "THU": -1,
                        "FRI": -1,
                    },
                }
            )
            return

        # 다음 과목과 시간 겹치면 끝
        for next_subject in combination_candidate[len(schedule_arr)]["subjects"]:
            flag = True
            for next_subject_time in next_subject["time"]:
                for schedule in schedule_arr:  # 가지고 있는 모든 과목들 순환
                    for prev_subject_time in schedule["time"]:
                        if next_subject_time["day"] == prev_subject_time["day"]:
                            # 겹치면 바로 끝
                            if (
                                next_subject_time["start"] < prev_subject_time["end"]
                                and next_subject_time["end"]
                                > prev_subject_time["start"]
                            ):
                                flag = False
            if flag:
                recursion(
                    targetDepth,
                    [*deepcopy(schedule_arr), deepcopy(next_subject)],
                    result_array,
                )

    result = []
    recursion(len(combination_candidate), [], result)

    # 3. free_days을 구하고, 각 일의 free time between classes를 구한다
    days = set(["MON", "TUE", "WED", "THU", "FRI"])
    for idx, candidates in enumerate(result):
        used_days = set()
        for subject in candidates["schedule"]:
            for time in subject["time"]:
                used_days.add(time["day"])
        candidates["freeDays"] = list(days - used_days)

    # 각 일의 free time between classes를 구한다 ** 이게 어렵네
    for candidates in result:
        for day in ["MON", "TUE", "WED", "THU", "FRI"]:
            free_time_between_classes = 0
            classes_today = []
            for subject in candidates["schedule"]:
                for time in subject["time"]:
                    if time["day"] == day:
                        classes_today.append(
                            (subject["name"], time["start"], time["end"])
                        )
            classes_today.sort(key=lambda x: x[1])
            for idx, class_today in enumerate(classes_today):
                if idx == 0:
                    continue
                free_time_between_classes += string_time_to_minutes(
                    classes_today[idx][1]
                ) - string_time_to_minutes(classes_today[idx - 1][2])
            candidates["freeTimeBetweenClasses"][day] = free_time_between_classes
    for item in result:
        result_by_combination.append(deepcopy(item))

# ! 정렬
# 정렬 조건
# 1. freeDays가 많은 순서대로
# 1.5. 과목 수가 많은 순서대로
# 2. freeTimeBetweenClasses가 적은 순서대로 (마이너스를 붙여서 오름차순으로 변환)
result_by_combination.sort(
    key=lambda x: (
        len(x["freeDays"]),
        len(x["schedule"]),
        -sum(x["freeTimeBetweenClasses"].values()),
    ),
    reverse=True,
)


# ! 출력
print(result_by_combination)
