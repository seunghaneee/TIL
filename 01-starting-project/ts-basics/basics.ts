// 기본형 데이터(number, string, boolean)

let age:number = 24;

let userName:string | string[]

let isInstructor: boolean;
isInstructor = true;


// 복잡한 자료형(배열, 객체)

// 배열
let hobbies: string[];

hobbies = ['Sports', 'Cooking']

// 타입 별칭
type Person = {
  name: String,
  age: number
}
// 객체
// let person:any;
// let person: {
//   name: string,
//   age: number,

// };

let person: Person;
person = {
  name: 'Max',
  age: 32
};

// person = {
//   isEmployee: true,
// }

// 객체 배열
// let people: {
//   name: string,
//   age: number,
// }[];

let people: Person[];

// 타입 추론
// string 명시 안해도 사용 가능함
// 유니온 타입
let course: string | number = 'React - The Complete Guide'
course = 12341;

// 함수와 타입

// const add = (a: number, b: number) => {
//   return a + b;
// }


function add(a: number, b: number) {
  return a + b;
}


function print(value: any) {
  console.log(value)
}

// Generics <>

function insertAtBeginning<T>(array: T[], value: T) {
  const newArray = [value, ...array];
  return newArray;
}

const demoArray = [1, 2, 3]

const updatedArray = insertAtBeginning(demoArray, -1) // [-1, 1, 2, 3]
const stringArray = insertAtBeginning(['a', 'b', 'c'], 'd')

// updatedArray[0].split('');