from copy import deepcopy
from itertools import combinations


# ! 예시 데이터 Input

input_data = {
    "minSubjectsCount": 2,
    "groups": [
        {
            "name": "앱플밍",
            "gradeTime": 3,
            "isMandatory": True,
            "subjects": [
                {
                    "name": "앱플밍",
                    "time": [
                        {"day": "MON", "start": "18:00", "end": "19:50"},
                        {"day": "TUE", "start": "19:30", "end": "21:20"},
                    ],
                },
            ],
        },
        {
            "name": "알고리즘",
            "gradeTime": 3,
            "isMandatory": True,
            "subjects": [
                {
                    "name": "알고리즘",
                    "time": [
                        {"day": "MON", "start": "16:30", "end": "17:45"},
                        {"day": "THU", "start": "16:30", "end": "17:45"},
                    ],
                },
            ],
        },
        {
            "name": "전공종합설계2",
            "gradeTime": 3,
            "isMandatory": True,
            "subjects": [
                {
                    "name": "전종설1",
                    "time": [
                        {"day": "MON", "start": "13:30", "end": "14:45"},
                        {"day": "WED", "start": "13:30", "end": "14:45"},
                    ],
                },
                {
                    "name": "전종설2",
                    "time": [
                        {"day": "MON", "start": "13:30", "end": "14:45"},
                        {"day": "WED", "start": "15:00", "end": "16:15"},
                    ],
                },
            ],
        },
        {
            "name": "데이터베이스",
            "gradeTime": 3,
            "isMandatory": False,
            "subjects": [
                {
                    "name": "데이터베이스1",
                    "time": [
                        {"day": "MON", "start": "13:30", "end": "14:45"},
                        {"day": "WED", "start": "13:30", "end": "14:45"},
                    ],
                },
                {
                    "name": "데이터베이스2",
                    "time": [
                        {"day": "TUE", "start": "12:00", "end": "13:15"},
                        {"day": "THU", "start": "12:00", "end": "13:15"},
                    ],
                },
                {
                    "name": "데이터베이스3",
                    "time": [
                        {"day": "TUE", "start": "15:00", "end": "16:15"},
                        {"day": "THU", "start": "15:00", "end": "16:15"},
                    ],
                },
            ],
        },
        {
            "name": "OS",
            "gradeTime": 3,
            "isMandatory": True,
            "subjects": [
                {
                    "name": "OS 1",
                    "time": [
                        {"day": "MON", "start": "10:30", "end": "11:45"},
                        {"day": "WED", "start": "10:30", "end": "11:45"},
                    ],
                },
                {
                    "name": "OS 2",
                    "time": [
                        {"day": "MON", "start": "12:00", "end": "13:15"},
                        {"day": "WED", "start": "12:00", "end": "13:15"},
                    ],
                },
                {
                    "name": "OS 3",
                    "time": [
                        {"day": "MON", "start": "15:00", "end": "16:15"},
                        {"day": "WED", "start": "15:00", "end": "16:15"},
                    ],
                },
                {
                    "name": "OS 4 (양)",
                    "time": [
                        {"day": "WED", "start": "12:00", "end": "13:15"},
                        {"day": "FRI", "start": "12:00", "end": "13:15"},
                    ],
                },
            ],
        },
        {
            "name": "섬김의리더십",
            "gradeTime": 1,
            "isMandatory": True,
            "subjects": [
                {
                    "name": "섬리1",
                    "time": [
                        {"day": "THU", "start": "14:00", "end": "14:50"},
                    ],
                },
                {
                    "name": "섬리2",
                    "time": [
                        {"day": "MON", "start": "16:00", "end": "16:50"},
                    ],
                },
                {
                    "name": "섬리3",
                    "time": [
                        {"day": "TUE", "start": "15:00", "end": "16:50"},
                    ],
                },
            ],
        },
        {
            "name": "확통",
            "gradeTime": 3,
            "isMandatory": False,
            "subjects": [
                {
                    "name": "확통1 (한진일)",
                    "time": [
                        {"day": "MON", "start": "15:00", "end": "16:15"},
                        {"day": "WED", "start": "10:30", "end": "11:45"},
                    ],
                },
                {
                    "name": "확통2 (한진일)",
                    "time": [
                        {"day": "MON", "start": "10:30", "end": "11:45"},
                        {"day": "TUE", "start": "15:00", "end": "16:15"},
                    ],
                },
                {
                    "name": "확통3 (이연수)",
                    "time": [
                        {"day": "TUE", "start": "15:00", "end": "16:15"},
                        {"day": "WED", "start": "15:00", "end": "16:15"},
                    ],
                },
            ],
        },
    ],
}

# ! 유틸 함수 정의


# 시간표 데이터 불러오기
def string_time_to_minutes(time):
    return int(time.split(":")[0]) * 60 + int(time.split(":")[1])


# ? 전공 선택 최소픽 ~ 최대픽까지 조합 모두 구함
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
            not_mandatory_subjects_count,  # 선택 과목이 몇개 선택될 건지
        ),
    )

result_by_combination = []

# ? 각 전공 선택의 선택 경우마다 조합을 구한다.
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

    # ? 공강 요일 계산
    days = set(["MON", "TUE", "WED", "THU", "FRI"])
    for idx, candidates in enumerate(result):
        used_days = set()
        for subject in candidates["schedule"]:
            for time in subject["time"]:
                used_days.add(time["day"])
        candidates["freeDays"] = list(days - used_days)

    # ? 각 요일 비는 시간 계산
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
result_by_combination.sort(
    key=lambda x: (
        len(x["freeDays"]),  # 공강 요일이 많을 수록 좋다
        len(x["schedule"]),  # 같은 공강 요일 개수라면 많은 과목이 좋다
        -sum(
            x["freeTimeBetweenClasses"].values()
        ),  # 수업 사이에 비는 시간은 적을 수록 좋다.
    ),
    reverse=True,
)

real_result = []

must_be_list = set([])
must_not_be_list = set([])

# ! 선택 (추후 제거 필요)
for item in result_by_combination:
    real_result.append(item)
    # sub_names = set(map(lambda x: x["name"], item["schedule"]))
    # # 포함되어 있으면 안되는 set item 중 하나라도 가지는게 없는 상태
    # if must_not_be_list & sub_names == set():
    #     real_result.append(item)

# ! 출력
# print(len(result_by_combination))
print(real_result)
# print(result_by_combination)
# print(result_by_combination[: len(result_by_combination) / 3])
