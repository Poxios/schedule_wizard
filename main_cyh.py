from copy import deepcopy
from itertools import combinations
import json

# ! 예시 데이터 Input

input_data = {
    "minSubjectsCount": 2,
    "minGradeTime": 10,
    "maxGradeTime": 20,
    "groups": [
        # [전필] OS
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
                # {
                #     "name": "OS 4 (양)",
                #     "time": [
                #         {"day": "WED", "start": "12:00", "end": "13:15"},
                #         {"day": "FRI", "start": "12:00", "end": "13:15"},
                #     ],
                # },
            ],
        },
        # [융필] 앱플밍
        {
            "name": "앱플밍",
            "gradeTime": 3,
            "isMandatory": False,
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
        # [전필] 알고리즘
        {
            "name": "알고리즘",
            "gradeTime": 3,
            "isMandatory": False,
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
        # [융선, 전선] 신상품계획론
        {
            "name": "신상품계획론",
            "gradeTime": 3,
            "isMandatory": False,
            "subjects": [
                {
                    "name": "신상품계획론_김근배_2150434001",
                    "time": [
                        {"day": "WED", "start": "10:30", "end": "11:45"},
                        {"day": "THU", "start": "10:30", "end": "11:45"},
                    ],
                },
                {
                    "name": "신상품계획론_김근배_2150434002",
                    "time": [
                        {"day": "WED", "start": "13:30", "end": "14:45"},
                        {"day": "THU", "start": "13:30", "end": "14:45"},
                    ],
                },
                # {
                #     "name": "신상품계획론_오현석_2150434003",
                #     "time": [
                #         {"day": "FRI", "start": "18:00", "end": "19:15"},
                #         {"day": "FRI", "start": "19:30", "end": "20:45"},
                #     ],
                # },
                {
                    "name": "신상품계획론_정문선_2150434004",
                    "time": [
                        {"day": "THU", "start": "13:30", "end": "14:45"},
                        {"day": "THU", "start": "15:00", "end": "16:15"},
                    ],
                },
            ],
        },
        # [융선] 컴퓨터비전
        {
            "name": "컴퓨터비전",
            "gradeTime": 3,
            "isMandatory": False,
            "subjects": [
                {
                    "name": "컴퓨터비전_송현주_2150692501",
                    "time": [
                        {"day": "MON", "start": "12:00", "end": "13:15"},
                        {"day": "WED", "start": "10:30", "end": "11:45"},
                    ],
                },
                {
                    "name": "컴퓨터비전_송현주_2150692502",
                    "time": [
                        {"day": "TUE", "start": "12:00", "end": "13:15"},
                        {"day": "THU", "start": "12:00", "end": "13:15"},
                    ],
                },
            ],
        },
        # [전선] 오픈소스기반기초설계
        {
            "name": "오픈소스기반기초설계",
            "gradeTime": 3,
            "isMandatory": False,
            "subjects": [
                {
                    "name": "오픈소스기반기초설계_김익수_2150061301",
                    "time": [
                        {"day": "WED", "start": "09:00", "end": "10:15"},
                        {"day": "WED", "start": "10:30", "end": "11:45"},
                    ],
                }
            ],
        },
        # [전선] 데이터베이스
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
        # [교양] 섬리
        {
            "name": "섬김의리더십",
            "gradeTime": 1,
            "isMandatory": False,
            "subjects": [
                {
                    "name": "섬김의리더십_문정화_2150533701",
                    "time": [{"day": "THU", "start": "14:00", "end": "14:50"}],
                },
                {
                    "name": "섬김의리더십_최춘화_2150533702",
                    "time": [{"day": "MON", "start": "16:00", "end": "16:50"}],
                },
                {
                    "name": "섬김의리더십_문정화_2150533703",
                    "time": [{"day": "TUE", "start": "15:00", "end": "15:50"}],
                },
                {
                    "name": "섬김의리더십_문정화_2150533704",
                    "time": [{"day": "TUE", "start": "16:00", "end": "16:50"}],
                },
                {
                    "name": "섬김의리더십_문정화_2150533705",
                    "time": [{"day": "WED", "start": "14:00", "end": "14:50"}],
                },
                {
                    "name": "섬김의리더십_문정화_2150533706",
                    "time": [{"day": "THU", "start": "15:00", "end": "15:50"}],
                },
                {
                    "name": "섬김의리더십_문정화_2150533707",
                    "time": [{"day": "THU", "start": "16:00", "end": "16:50"}],
                },
                # {
                #     "name": "섬김의리더십_문정화_2150533708",
                #     "time": [{"day": "FRI", "start": "15:00", "end": "15:50"}],
                # },
                # {
                #     "name": "섬김의리더십_문정화_2150533709",
                #     "time": [{"day": "FRI", "start": "16:00", "end": "16:50"}],
                # },
                {
                    "name": "섬김의리더십_최춘화_2150533710",
                    "time": [{"day": "WED", "start": "15:00", "end": "15:50"}],
                },
                {
                    "name": "섬김의리더십_최춘화_2150533711",
                    "time": [{"day": "WED", "start": "16:00", "end": "16:50"}],
                },
                # {
                #     "name": "섬김의리더십_최춘화_2150533712",
                #     "time": [{"day": "FRI", "start": "15:00", "end": "15:50"}],
                # },
                # {
                #     "name": "섬김의리더십_최춘화_2150533713",
                #     "time": [{"day": "FRI", "start": "16:00", "end": "16:50"}],
                # },
                {
                    "name": "섬김의리더십_문정화_2150533714",
                    "time": [{"day": "TUE", "start": "14:00", "end": "14:50"}],
                },
                # {
                #     "name": "섬김의리더십_문정화_2150533715",
                #     "time": [{"day": "FRI", "start": "14:00", "end": "14:50"}],
                # },
            ],
        },
        # 채플
        {
            "name": "비전채플",
            "gradeTime": 0.5,
            "isMandatory": True,
            "subjects": [
                {
                    "name": "비전채플_김회권_2150101508",
                    "time": [{"day": "TUE", "start": "16:30", "end": "17:20"}],
                },
                # {
                #     "name": "비전채플_김회권_2150101509",
                #     "time": [{"day": "MON", "start": "04:00", "end": "04:10"}],
                # },
                {
                    "name": "비전채플_김회권_2150101504",
                    "time": [{"day": "MON", "start": "16:30", "end": "17:20"}],
                },
                {
                    "name": "비전채플_조은식_2150101501",
                    "time": [{"day": "MON", "start": "10:30", "end": "11:20"}],
                },
                {
                    "name": "비전채플_조은식_2150101502",
                    "time": [{"day": "MON", "start": "13:30", "end": "14:20"}],
                },
                {
                    "name": "비전채플_김회권_2150101503",
                    "time": [{"day": "MON", "start": "15:00", "end": "15:50"}],
                },
                {
                    "name": "비전채플_조은식_2150101505",
                    "time": [{"day": "TUE", "start": "10:30", "end": "11:20"}],
                },
                {
                    "name": "비전채플_조은식_2150101506",
                    "time": [{"day": "TUE", "start": "13:30", "end": "14:20"}],
                },
                {
                    "name": "비전채플_김회권_2150101507",
                    "time": [{"day": "TUE", "start": "15:00", "end": "15:50"}],
                },
            ],
        },
        # [융선, 1학년] 확통
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
        # 소비자행동론
        {
            "name": "소비자행동론",
            "gradeTime": 3,
            "isMandatory": False,
            "subjects": [
                {
                    "name": "소비자행동론_이명수_2150610302",
                    "time": [
                        {"day": "WED", "start": "15:00", "end": "16:15"},
                        {"day": "WED", "start": "16:30", "end": "17:45"},
                    ],
                }
            ],
        },
        # [전선, 4학년] 전종설
        {
            "name": "전공종합설계2",
            "gradeTime": 3,
            "isMandatory": False,
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
        # [전선] 정보보안
        {
            "name": "정보보안",
            "gradeTime": 3,
            "isMandatory": False,
            "subjects": [
                {
                    "name": "정보보안_최봉준_2150630801",
                    "time": [
                        {"day": "TUE", "start": "10:30", "end": "11:45"},
                        {"day": "THU", "start": "10:30", "end": "11:45"},
                    ],
                }
            ],
        },
        # [전선] 인공지능 (이거하면 금공강 못함)
        # {
        #     "name": "인공지능",
        #     "gradeTime": 3,
        #     "isMandatory": False,
        #     "subjects": [
        #         {
        #             "name": "인공지능_정다흰_2150188401",
        #             "time": [
        #                 {"day": "TUE", "start": "15:00", "end": "16:15"},
        #                 {"day": "FRI", "start": "13:30", "end": "14:45"},
        #             ],
        #         },
        #         {
        #             "name": "인공지능_정다흰_2150188402",
        #             "time": [
        #                 {"day": "TUE", "start": "16:30", "end": "17:45"},
        #                 {"day": "FRI", "start": "15:00", "end": "16:15"},
        #             ],
        #         },
        #     ],
        # },
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

# ! 어떻게 짰는지 까먹어서 학점 후처리로 추가함.
for item in result_by_combination:
    for idx, element in enumerate(item["schedule"]):
        name_to_find = element["name"]  # 이 이름 가지고 학점 찾아야 됨.
        for subject in input_data["groups"]:
            for subject_detail in subject["subjects"]:
                if subject_detail["name"] == name_to_find:
                    item["schedule"][idx]["gradeTime"] = subject["gradeTime"]
                    item["schedule"][idx]["originalName"] = subject["name"]
    real_result.append(item)


# ! 결과 필터링
real_result = list(
    filter(
        # real_result 안에 있는 items 중 gradeTime 총합이 19 이하인 것만
        lambda x: input_data["minGradeTime"]
        <= sum(map(lambda y: y["gradeTime"], x["schedule"]))
        <= input_data["maxGradeTime"],
        real_result,
    )
)

# ! 출력
print(json.dumps(real_result, ensure_ascii=False))
