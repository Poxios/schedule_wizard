interface ISubject {
  name: string;
  time: {
    day: "MON" | "TUE" | "WED" | "THU" | "FRI";
    start: string;
    end: string;
  }[];
}
interface ISubjectGroup {
  gradeTime: number;
  isMandatory: boolean;
  name: string;
  subjects: ISubject[];
}
type InputType = {
  // 최소 전공선택 몇개는 선택되어야 할지 선택
  minSubjectsCount: number;
  groups: ISubjectGroup[];
};

const input: InputType = {
  minSubjectsCount: 3,
  groups: [
    {
      name: "앱플밍",
      gradeTime: 3,
      isMandatory: true,
      subjects: [
        {
          name: "앱플밍",
          time: [
            { day: "MON", start: "18:00", end: "19:50" },
            { day: "THU", start: "19:30", end: "21:20" },
          ],
        },
      ],
    },
    {
      name: "알고리즘",
      gradeTime: 3,
      isMandatory: true,
      subjects: [
        {
          name: "알고리즘",
          time: [
            { day: "MON", start: "16:30", end: "17:45" },
            { day: "THU", start: "16:30", end: "17:45" },
          ],
        },
      ],
    },
    {
      name: "데이터베이스",
      gradeTime: 3,
      isMandatory: false,
      subjects: [
        {
          name: "데이터베이스1",
          time: [
            { day: "MON", start: "13:30", end: "14:45" },
            { day: "WED", start: "13:30", end: "14:45" },
          ],
        },
        {
          name: "데이터베이스2",
          time: [
            { day: "TUE", start: "12:00", end: "13:15" },
            { day: "TUE", start: "12:00", end: "13:15" },
          ],
        },
        {
          name: "데이터베이스3",
          time: [
            { day: "TUE", start: "15:00", end: "16:15" },
            { day: "TUE", start: "15:00", end: "16:15" },
          ],
        },
      ],
    },
    {
      name: "OS",
      gradeTime: 3,
      isMandatory: false,
      subjects: [
        {
          name: "OS 1",
          time: [
            { day: "MON", start: "10:30", end: "11:45" },
            { day: "WED", start: "10:30", end: "11:45" },
          ],
        },
        {
          name: "OS 2",
          time: [
            { day: "MON", start: "12:00", end: "13:15" },
            { day: "WED", start: "12:00", end: "13:15" },
          ],
        },
        {
          name: "OS 3",
          time: [
            { day: "MON", start: "15:00", end: "16:15" },
            { day: "WED", start: "15:00", end: "16:15" },
          ],
        },
        {
          name: "OS 4 (양)",
          time: [
            { day: "WED", start: "12:00", end: "13:15" },
            { day: "FRI", start: "12:00", end: "13:15" },
          ],
        },
      ],
    },
    {
      name: "확통",
      gradeTime: 3,
      isMandatory: false,
      subjects: [
        {
          name: "확통1 (한진일)",
          time: [
            { day: "MON", start: "15:00", end: "16:15" },
            { day: "WED", start: "10:30", end: "11:45" },
          ],
        },
        {
          name: "확통2 (한진일)",
          time: [
            { day: "MON", start: "10:30", end: "11:45" },
            { day: "TUE", start: "15:00", end: "16:15" },
          ],
        },
        {
          name: "확통3 (이연수)",
          time: [
            { day: "TUE", start: "15:00", end: "16:15" },
            { day: "WED", start: "15:00", end: "16:15" },
          ],
        },
      ],
    },
  ],
};
