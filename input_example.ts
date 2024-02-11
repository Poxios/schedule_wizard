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
  groups: ISubjectGroup[]
};


const input: InputType = {
  minSubjectsCount: 3,
  groups: [
    {
      name: "프로그래밍언어", gradeTime: 3, isMandatory: true, subjects: [
        {
          name: "프로그래밍언어", time: [
            { day: "TUE", start: "10:30", end: "11:45" },
            { day: "THU", start: "13:30", end: "14:45" }
          ]
        },
        {
          name: "프로그래밍언어", time: [
            { day: "TUE", start: "13:30", end: "14:45" },
            { day: "THU", start: "10:30", end: "11:45" }
          ]
        },
        {
          name: "프로그래밍언어", time: [
            { day: "TUE", start: "15:00", end: "16:15" },
            { day: "THU", start: "15:00", end: "16:15" }
          ]
        },
      ]
    },
    {
      name: "마케팅", gradeTime: 3, isMandatory: false, subjects: [
        {
          name: "마케팅", time: [
            { day: "TUE", start: "13:30", end: "14:45" },
            { day: "THU", start: "13:30", end: "14:45" }
          ]
        }
      ]
    },
    {
      name: "Entrepreneurship", gradeTime: 3, isMandatory: false, subjects: [
        {
          name: "Entrepreneurship (최금선)", time: [
            { day: "THU", start: "10:30", end: "11:45" },
            { day: "THU", start: "12:00", end: "13:15" }
          ]
        },
        {
          name: "Entrepreneurship (박병호)", time: [
            { day: "TUE", start: "15:00", end: "16:15" },
            { day: "TUE", start: "16:30", end: "17:45" }
          ]
        },
        {
          name: "Entrepreneurship (김영수)", time: [
            { day: "MON", start: "15:00", end: "16:15" },
            { day: "WED", start: "15:00", end: "16:15" },
          ]
        },
        {
          name: "Entrepreneurship (김영수)", time: [
            { day: "MON", start: "16:30", end: "17:45" },
            { day: "WED", start: "16:30", end: "17:45" },
          ]
        }
      ]
    },
    {
      name: "생산시스템관리", gradeTime: 3, isMandatory: false, subjects: [
        {
          name: "생산시스템관리(가)", time: [
            { day: "MON", start: "10:30", end: "11:45" },
            { day: "THU", start: "12:00", end: "13:15" }
          ]
        },
        {
          name: "생산시스템관리(나)", time: [
            { day: "MON", start: "12:00", end: "13:15" },
            { day: "THU", start: "13:30", end: "14:45" }
          ]
        },
        {
          name: "생산시스템관리(다)", time: [
            { day: "TUE", start: "12:00", end: "13:15" },
            { day: "THU", start: "16:30", end: "17:45" },
          ]
        }
      ]
    },
  ]
}