from copy import deepcopy
from itertools import combinations


# ! 예시 데이터 Input

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
        # {
        #     "name": "마케팅",
        #     "gradeTime": 3,
        #     "isMandatory": False,
        #     "subjects": [
        #         {
        #             "name": "마케팅A",
        #             "time": [
        #                 {"day": "TUE", "start": "13:30", "end": "14:45"},
        #                 {"day": "THU", "start": "13:30", "end": "14:45"},
        #             ],
        #         }
        #     ],
        # },
        {
            "name": "데이터통신",
            "gradeTime": 3,
            "isMandatory": True,
            "subjects": [
                {
                    "name": "데이터통신A",
                    "time": [
                        {"day": "MON", "start": "09:00", "end": "10:15"},
                        {"day": "WED", "start": "10:30", "end": "11:45"},
                    ],
                },
                {
                    "name": "데이터통신B",
                    "time": [
                        {"day": "MON", "start": "10:30", "end": "11:45"},
                        {"day": "WED", "start": "09:00", "end": "10:15"},
                    ],
                },
                {
                    "name": "데이터통신C",
                    "time": [
                        {"day": "MON", "start": "13:30", "end": "14:45"},
                        {"day": "WED", "start": "12:00", "end": "13:15"},
                    ],
                },
            ],
        },
        {
            "name": "경영정보시스템",
            "gradeTime": 3,
            "isMandatory": True,
            "subjects": [
                {
                    "name": "경영정보시스템A",
                    "time": [
                        {"day": "TUE", "start": "13:30", "end": "14:45"},
                        {"day": "THU", "start": "15:00", "end": "16:15"},
                    ],
                },
                {
                    "name": "경영정보시스템B",
                    "time": [
                        {"day": "TUE", "start": "10:30", "end": "11:45"},
                        {"day": "THU", "start": "10:30", "end": "11:45"},
                    ],
                },
                {
                    "name": "경영정보시스템C",
                    "time": [
                        {"day": "MON", "start": "12:00", "end": "13:15"},
                        {"day": "THU", "start": "13:30", "end": "14:45"},
                    ],
                },
            ],
        },
        # {
        #     "name": "Entrepreneurship",
        #     "gradeTime": 3,
        #     "isMandatory": False,
        #     "subjects": [
        #         {
        #             "name": "Entrepreneurship (최금선)",
        #             "time": [
        #                 {"day": "THU", "start": "10:30", "end": "11:45"},
        #                 {"day": "THU", "start": "12:00", "end": "13:15"},
        #             ],
        #         },
        #         {
        #             "name": "Entrepreneurship (박병호)",
        #             "time": [
        #                 {"day": "TUE", "start": "15:00", "end": "16:15"},
        #                 {"day": "TUE", "start": "16:30", "end": "17:45"},
        #             ],
        #         },
        #         {
        #             "name": "Entrepreneurship (김영수)A",
        #             "time": [
        #                 {"day": "MON", "start": "15:00", "end": "16:15"},
        #                 {"day": "WED", "start": "15:00", "end": "16:15"},
        #             ],
        #         },
        #         {
        #             "name": "Entrepreneurship (김영수)B",
        #             "time": [
        #                 {"day": "MON", "start": "16:30", "end": "17:45"},
        #                 {"day": "WED", "start": "16:30", "end": "17:45"},
        #             ],
        #         },
        #     ],
        # },
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
        {
            "name": "파일처리",
            "gradeTime": 3,
            "isMandatory": False,
            "subjects": [
                {
                    "name": "파일처리(가)",
                    "time": [
                        {"day": "MON", "start": "13:30", "end": "14:45"},
                        {"day": "THU", "start": "12:00", "end": "13:15"},
                    ],
                },
                {
                    "name": "파일처리(나)",
                    "time": [
                        {"day": "TUE", "start": "12:00", "end": "13:15"},
                        {"day": "THU", "start": "15:00", "end": "16:15"},
                    ],
                },
            ],
        },
        {
            "name": "유통물류창업론",
            "gradeTime": 3,
            "isMandatory": True,
            "subjects": [
                {
                    "name": "유통물류창업론",
                    "time": [
                        {"day": "MON", "start": "15:00", "end": "16:15"},
                        {"day": "MON", "start": "16:30", "end": "17:45"},
                    ],
                },
            ],
        },
        {
            "name": "채플",
            "gradeTime": 3,
            "isMandatory": True,
            "subjects": [
                {
                    "name": "채플 (3학년 사회 공대)",
                    "time": [
                        {"day": "TUE", "start": "13:30", "end": "14:20"},
                    ],
                },
                {
                    "name": "채플 (2학년 사회/IT대)",
                    "time": [
                        {"day": "MON", "start": "13:30", "end": "14:20"},
                    ],
                },
                {
                    "name": "채플 (2학년 자연/법/공대)",
                    "time": [
                        {"day": "MON", "start": "15:00", "end": "15:50"},
                    ],
                },
                {
                    "name": "채플 (2학년 이상 / 전체단과대학)",
                    "time": [
                        {"day": "TUE", "start": "16:30", "end": "17:20"},
                    ],
                },
                {
                    "name": "채플 (2학년 인문/경통/경영대)",
                    "time": [
                        {"day": "MON", "start": "10:30", "end": "11:20"},
                    ],
                },
                {
                    "name": "채플 (3학년 인문/경통/경영대)",
                    "time": [
                        {"day": "TUE", "start": "10:30", "end": "11:20"},
                    ],
                },
                {
                    "name": "채플 (3학년 자연/법/IT대)",
                    "time": [
                        {"day": "TUE", "start": "15:00", "end": "15:50"},
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

# ! 선택 (추후 제거 필요)
for item in result_by_combination:
    for subject in item["schedule"]:
        if (
            "경영정보시스템" in subject["name"] or "데이터통신" in subject["name"]
        ) and len(item["schedule"]) == 5:
            real_result.append(item)

# ! 출력
# print(len(result_by_combination))
# print(real_result[0])
print(result_by_combination)
# print(result_by_combination[: len(result_by_combination) / 3])
