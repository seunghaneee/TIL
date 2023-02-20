import React from "react";
import TodoItem from "./TodoItem";
import Todo from "../models/todo";

import classes from "./Todos.module.css";

// 리액트에서 props는 언제나 객체 형태이다.

// React.FC 함수형 컴포넌트 정의 / 제네릭 타입
const Todos: React.FC<{ items: Todo[] }> = (props) => {
  return (
    <ul className={classes.todos}>
      {props.items.map((item) => (
        // <li key={item.id}>{item.text}</li>
        <TodoItem key={item.id} text={item.text} />
      ))}
    </ul>
  );
};

export default Todos;
