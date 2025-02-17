from copy import deepcopy
from itertools import combinations
import json
import os

input_data = {
    "minSubjectsCount": 2,
    "groups": [
        {
            "name": "전공종합설계1",
            "gradeTime": 3,
            "isMandatory": True,
            "subjects": [
                {
                    "name": "전공종합설계1-1",
                    "time": [
                        {"day": "MON", "start": "13:30", "end": "14:45"},
                        {"day": "WED", "start": "13:30", "end": "14:45"},
                    ],
                },
                {
                    "name": "전공종합설계1-2",
                    "time": [
                        {"day": "MON", "start": "15:00", "end": "16:15"},
                        {"day": "WED", "start": "15:00", "end": "16:15"},
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
                    "name": "유통물류창업론 (2150050801)",
                    "time": [
                        {"day": "TUE", "start": "15:00", "end": "16:15"},
                        {"day": "TUE", "start": "16:30", "end": "17:45"},
                    ],
                }
            ],
        },
        {
            "name": "컴퓨터학개론",
            "gradeTime": 3,
            "isMandatory": False,
            "subjects": [
                {
                    "name": "컴퓨터학개론 (2150016203(공통-재수강))",
                    "time": [
                        {"day": "MON", "start": "09:00", "end": "10:15"},
                        {"day": "MON", "start": "10:30", "end": "11:45"},
                    ],
                }
            ],
        },
        {
            "name": "벤처중소기업브랜드전략",
            "gradeTime": 3,
            "isMandatory": False,
            "subjects": [
                {
                    "name": "벤처중소기업브랜드전략 (2150630601)",
                    "time": [
                        {"day": "FRI", "start": "09:00", "end": "10:15"},
                        {"day": "FRI", "start": "10:30", "end": "11:45"},
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
                    "name": "Entrepreneurship (2150328201)",
                    "time": [
                        {"day": "TUE", "start": "10:30", "end": "11:45"},
                        {"day": "TUE", "start": "12:00", "end": "13:15"},
                    ],
                },
                {
                    "name": "Entrepreneurship (2150328202)",
                    "time": [
                        {"day": "TUE", "start": "13:30", "end": "14:45"},
                        {"day": "TUE", "start": "15:00", "end": "16:15"},
                    ],
                },
                {
                    "name": "Entrepreneurship (2150328203)",
                    "time": [
                        {"day": "FRI", "start": "13:30", "end": "14:45"},
                        {"day": "FRI", "start": "15:00", "end": "16:15"},
                    ],
                },
                {
                    "name": "Entrepreneurship (2150644001)",
                    "time": [
                        {"day": "WED", "start": "15:00", "end": "16:15"},
                        {"day": "WED", "start": "16:30", "end": "17:45"},
                    ],
                },
                {
                    "name": "Entrepreneurship (2150644002(공통-재수강))",
                    "time": [
                        {"day": "WED", "start": "18:00", "end": "19:15"},
                        {"day": "WED", "start": "19:30", "end": "20:45"},
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
                    "name": "생산시스템관리 (2150361701)",
                    "time": [
                        {"day": "TUE", "start": "10:30", "end": "11:45"},
                        {"day": "WED", "start": "15:00", "end": "16:15"},
                    ],
                },
                {
                    "name": "생산시스템관리 (2150361702)",
                    "time": [
                        {"day": "MON", "start": "12:00", "end": "13:15"},
                        {"day": "WED", "start": "10:30", "end": "11:45"},
                    ],
                },
                {
                    "name": "생산시스템관리 (2150361703)",
                    "time": [
                        {"day": "MON", "start": "13:30", "end": "14:45"},
                        {"day": "WED", "start": "12:00", "end": "13:15"},
                    ],
                },
            ],
        },
        {
            "name": "스타트업비즈니스모델개발론",
            "gradeTime": 3,
            "isMandatory": False,
            "subjects": [
                {
                    "name": "스타트업비즈니스모델개발론 (2150039601)",
                    "time": [
                        {"day": "THU", "start": "13:30", "end": "14:45"},
                        {"day": "THU", "start": "15:00", "end": "16:15"},
                    ],
                }
            ],
        },
        {
            "name": "마케팅",
            "gradeTime": 3,
            "isMandatory": False,
            "subjects": [
                {
                    "name": "마케팅 (2150338201)",
                    "time": [
                        {"day": "WED", "start": "12:00", "end": "13:15"},
                        {"day": "THU", "start": "15:00", "end": "16:15"},
                    ],
                },
                {
                    "name": "마케팅 (2150338202)",
                    "time": [
                        {"day": "TUE", "start": "13:30", "end": "14:45"},
                        {"day": "THU", "start": "13:30", "end": "14:45"},
                    ],
                },
                {
                    "name": "마케팅 (2150338203)",
                    "time": [
                        {"day": "TUE", "start": "10:30", "end": "11:45"},
                        {"day": "THU", "start": "10:30", "end": "11:45"},
                    ],
                },
                {
                    "name": "마케팅 (2150338204(공통-재수강))",
                    "time": [
                        {"day": "THU", "start": "10:30", "end": "11:45"},
                        {"day": "THU", "start": "12:00", "end": "13:15"},
                    ],
                },
            ],
        },
        {
            "name": "경영정보시스템",
            "gradeTime": 3,
            "isMandatory": False,
            "subjects": [
                {
                    "name": "경영정보시스템 (2150558701)",
                    "time": [
                        {"day": "MON", "start": "12:00", "end": "13:15"},
                        {"day": "THU", "start": "12:00", "end": "13:15"},
                    ],
                },
                {
                    "name": "경영정보시스템 (2150558702)",
                    "time": [
                        {"day": "MON", "start": "13:30", "end": "14:45"},
                        {"day": "FRI", "start": "13:30", "end": "14:45"},
                    ],
                },
            ],
        },
        {
            "name": "컴퓨터그래픽스",
            "gradeTime": 3,
            "isMandatory": False,
            "subjects": [
                {
                    "name": "컴퓨터그래픽스 (2150629401)",
                    "time": [
                        {"day": "TUE", "start": "13:30", "end": "14:45"},
                        {"day": "THU", "start": "13:30", "end": "14:45"},
                    ],
                },
                {
                    "name": "컴퓨터그래픽스 (2150629402)",
                    "time": [
                        {"day": "TUE", "start": "15:00", "end": "16:15"},
                        {"day": "THU", "start": "15:00", "end": "16:15"},
                    ],
                },
            ],
        },
        {
            "name": "컴퓨터비전응용",
            "gradeTime": 3,
            "isMandatory": False,
            "subjects": [
                {
                    "name": "컴퓨터비전응용 (2150046101)",
                    "time": [
                        {"day": "WED", "start": "13:30", "end": "14:45"},
                        {"day": "FRI", "start": "13:30", "end": "14:45"},
                    ],
                },
                {
                    "name": "컴퓨터비전응용 (2150046102)",
                    "time": [
                        {"day": "TUE", "start": "13:30", "end": "14:45"},
                        {"day": "THU", "start": "13:30", "end": "14:45"},
                    ],
                },
            ],
        },
        {
            "name": "소비자행동론",
            "gradeTime": 3,
            "isMandatory": False,
            "subjects": [
                {
                    "name": "소비자행동론 (2150672701)",
                    "time": [
                        {"day": "MON", "start": "15:00", "end": "16:15"},
                        {"day": "WED", "start": "15:00", "end": "16:15"},
                    ],
                },
                {
                    "name": "소비자행동론 (2150672702)",
                    "time": [
                        {"day": "MON", "start": "09:00", "end": "10:15"},
                        {"day": "WED", "start": "09:00", "end": "10:15"},
                    ],
                },
                {
                    "name": "소비자행동론 (2150672703)",
                    "time": [
                        {"day": "MON", "start": "10:30", "end": "11:45"},
                        {"day": "WED", "start": "10:30", "end": "11:45"},
                    ],
                },
            ],
        },
        {
            "name": "빅데이터와 Business Intelligence",
            "gradeTime": 3,
            "isMandatory": False,
            "subjects": [
                {
                    "name": "빅데이터와 Business Intelligence (2150572001)",
                    "time": [
                        {"day": "TUE", "start": "16:30", "end": "17:45"},
                        {"day": "TUE", "start": "18:00", "end": "19:15"},
                    ],
                },
            ],
        },
        # {
        #     "name": "데이터베이스응용",
        #     "gradeTime": 3,
        #     "isMandatory": False,
        #     "subjects": [
        #         {
        #             "name": "데이터베이스응용 (2150565701)",
        #             "time": [
        #                 {"day": "MON", "start": "12:00", "end": "13:15"},
        #                 {"day": "WED", "start": "12:00", "end": "13:15"},
        #             ],
        #         },
        #     ],
        # },
        {
            "name": "지능형시스템",
            "gradeTime": 3,
            "isMandatory": False,
            "subjects": [
                {
                    "name": "지능형시스템 (2150534701)",
                    "time": [
                        {"day": "WED", "start": "16:30", "end": "17:45"},
                        {"day": "WED", "start": "18:00", "end": "19:15"},
                    ],
                },
                {
                    "name": "지능형시스템 (2150534702)",
                    "time": [
                        {"day": "MON", "start": "16:30", "end": "17:45"},
                        {"day": "MON", "start": "18:00", "end": "19:15"},
                    ],
                },
            ],
        },
    ],
}

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
        if not ("FRI" in item["freeDays"]):
            real_result.append(item)

# ! 출력
# print(len(result_by_combination))
print(result_by_combination)
# print(result_by_combination[1])
# print(result_by_combination[: len(result_by_combination) / 3])

# 상위 디렉토리의 경로 생성
output_dir = os.path.join(
    os.path.dirname(os.path.dirname(__file__)), "schedule_wizard_react", "src", "assets"
)

# 디렉토리가 없다면 생성
os.makedirs(output_dir, exist_ok=True)

# JSON 파일 경로
output_file = os.path.join(output_dir, "a.json")

# JSON 파일로 저장
with open(output_file, "w", encoding="utf-8") as f:
    json.dump(result_by_combination, f, ensure_ascii=False, indent=2)

print(f"결과가 {output_file}에 저장되었습니다.")
