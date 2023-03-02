import React, { useState, useCallback } from "react";
import { Link } from "react-router-dom";
import classes from "../Board.module.css";

interface Props {
  readonly onRegister: (title: string, content: string, writer: string) => void;
}
const BoardRegisterForm = ({ onRegister }: Props) => {
  const [title, setTitle] = useState("");
  const [content, setContent] = useState("");
  const [writer, setWriter] = useState("");

  const handleChangeTitle = useCallback(
    (e: React.ChangeEvent<HTMLInputElement>) => {
      setTitle(e.target.value);
    },
    []
  );

  const handleChangeContent = useCallback(
    (e: React.ChangeEvent<HTMLTextAreaElement>) => {
      setContent(e.target.value);
    },
    []
  );

  const handleChangeWriter = useCallback(
    (e: React.ChangeEvent<HTMLInputElement>) => {
      setWriter(e.target.value);
    },
    []
  );

  const handleSubmit = useCallback(
    (e: React.SyntheticEvent) => {
      e.preventDefault();
      onRegister(title, content, writer);
    },
    [title, content, writer]
  );
  return (
    <div className={classes.centered}>
      <h2>게시판 등록</h2>
      <form onSubmit={handleSubmit}>
        <table>
          <tbody>
            <tr>
              <td>제목</td>
              <td>
                <input type="text" value={title} onChange={handleChangeTitle} />
              </td>
            </tr>
            <tr>
              <td>작성자</td>
              <td>
                <input
                  type="text"
                  value={writer}
                  onChange={handleChangeWriter}
                />
              </td>
            </tr>
            <tr>
              <td>내용</td>
              <td>
                <textarea
                  rows={5}
                  value={content}
                  onChange={handleChangeContent}
                ></textarea>
              </td>
            </tr>
          </tbody>
        </table>
        <div className={classes.align_centered}>
          <button type="submit">등록</button>
          <Link to="/">취소</Link>
        </div>
      </form>
    </div>
  );
};

export default BoardRegisterForm;
