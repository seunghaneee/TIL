import { useState } from "react";
import classes from "./Todo.module.css";

interface Props {
  readonly onInsert: (value: string) => void;
}
const TodoInput = ({ onInsert }: Props) => {
  // 새로 입력한 Todo value 정의
  const [value, setValue] = useState("");

  const onChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    setValue(event.target.value);
  };

  const onSubmit = (event: React.FormEvent<HTMLFormElement>) => {
    event.preventDefault();

    onInsert(value);
    setValue("");
  };
  return (
    <div className={classes.input}>
      <form onSubmit={onSubmit}>
        <input
          placeholder="할 일을 입력하세요"
          type="text"
          value={value}
          onChange={onChange}
        />
        <button type="submit">추가</button>
      </form>
    </div>
  );
};

export default TodoInput;
