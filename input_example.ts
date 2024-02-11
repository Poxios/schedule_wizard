interface ISubject {
  name: string;
  time: {
    day: "MON" | "TUE" | "WED" | "THU" | "FRI";
    start: string;
    end: string;
  }[];
}
interface ISubjectGroup {
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
  minSubjectsCount: 2,
  groups: [
    {
      name: "프로그래밍언어", isMandatory: true, subjects: [
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
      name: "마케팅", isMandatory: true, subjects: [
        {
          name: "마케팅", time: [
            { day: "TUE", start: "13:30", end: "14:45" },
            { day: "THU", start: "13:30", end: "14:45" }
          ]
        }
      ]
    },
  ]
}