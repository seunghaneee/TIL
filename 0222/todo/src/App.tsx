import Todos from "./components/Todos";

// 타입스크립트 인터페이스 사용하여 Todo 정의 최상단에 작성해야 한다.
export interface Todo {
  id: number;
  text: string;
  done: boolean;
}
const App = () => {
  return (
    <div>
      <Todos />
    </div>
  );
};

export default App;
