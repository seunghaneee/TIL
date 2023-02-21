import { useState } from "react";
import { Todo } from "../App";
import TodoItem from "./TodoItem";
import classes from "./Todo.module.css";

interface Props {
  readonly todos: Todo[];
  // 함수 타입 추가
  readonly onRemove: (id: number) => void;
  readonly onToggle: (id: number) => void;
}
const TodoList = ({ todos, onRemove, onToggle }: Props) => {
  // const [todos] = useState(["todoItem1", "todoItem2", "todoItem3"]);

  return (
    <div className={classes.list}>
      {/* <TodoItem />
      <TodoItem />
      <TodoItem /> */}
      {todos.map((todo) => (
        <TodoItem
          todo={todo}
          key={todo.id}
          onRemove={onRemove}
          onToggle={onToggle}
        />
      ))}
    </div>
  );
};

export default TodoList;
