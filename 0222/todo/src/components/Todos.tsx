import { useState, useRef, useCallback } from "react";

import TodoHeader from "./TodoHeader";
import TodoInput from "./TodoInput";
import TodoList from "./TodoList";
import TodoFooter from "./TodoFooter";

import { Todo } from "../App";
const Todos = () => {
  // const [todos] = useState([
  //   {
  //     id: 1,
  //     text: "todoItem1",
  //     done: true,
  //   },
  //   {
  //     id: 2,
  //     text: "todoItem2",
  //     done: false,
  //   },
  //   {
  //     id: 3,
  //     text: "todoItem3",
  //     done: false,
  //   },
  // ]);

  const [todos, setTodos] = useState<Todo[]>([]);

  const nextId = useRef(1);

  // const onInsert = (text: string) => {
  //   const todo = {
  //     id: nextId.current,
  //     text,
  //     done: false,
  //   };
  const onInsert = useCallback((text: string) => {
    const todo = {
      id: nextId.current,
      text,
      done: false,
    };

    // setTodos(todos.concat(todo));
    // 함수형 업데이트 방식으로 변경 (성능 향상)
    setTodos((todos) => todos.concat(todo));

    nextId.current += 1;
  }, []);

  const onRemove = useCallback((id: number) => {
    // setTodos(todos.filter((todo) => todo.id !== id));
    setTodos((todos) => todos.filter((todo) => todo.id !== id));
  }, []);

  const onToggle = useCallback((id: number) => {
    // setTodos(
    //   todos.map((todo) =>
    //     todo.id === id ? { ...todo, done: !todo.done } : todo
    //   )
    // );
    setTodos((todos) =>
      todos.map((todo) =>
        todo.id === id ? { ...todo, done: !todo.done } : todo
      )
    );
  }, []);

  const onClearAll = useCallback(() => {
    // setTodos([]);
    setTodos(() => []);
  }, []);

  return (
    <div>
      <TodoHeader />
      <TodoInput onInsert={onInsert} />
      <TodoList todos={todos} onRemove={onRemove} onToggle={onToggle} />
      <TodoFooter onClearAll={onClearAll} />
    </div>
  );
};

export default Todos;
