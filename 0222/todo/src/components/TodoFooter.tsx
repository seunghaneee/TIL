import classes from "./Todo.module.css";
interface Props {
  readonly onClearAll: () => void;
}
const TodoFooter = ({ onClearAll }: Props) => {
  return (
    <div className={classes.footer}>
      <button onClick={() => onClearAll()}>모두 삭제</button>
    </div>
  );
};

export default TodoFooter;
