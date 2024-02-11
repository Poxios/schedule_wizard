interface ISubject {
  name: string;
  time: {
    start: string;
    end: string;
  }[];
}
interface ISubjectGroup {
  isMandatory: boolean;
  name: string;
  subjects: ISubject[];
}
type InputType = ISubjectGroup[];


const input: InputType = [
  { name: "프로그래밍언어", isMandatory: true, subjects: [] },
  { name: "프로그래밍언어", isMandatory: true, subjects: [] },
]