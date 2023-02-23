// 게시물 등록 폼 구성

import React, { useState, useCallback } from "react";
import { Link } from "react-router-dom";
import classes from "../Board.module.css";

// props 타입스크립트 인터페이스 정의
interface Props {
  readonly onRegister: (title: string, content: string, writer: string) => void;
}
const BoardRegisterForm = ({ onRegister }: Props) => {
  // 사용자가 원하는 값을 입력하는 화면 요소에 바인당할 상태를 설정
  const [title, setTitle] = useState("");
  const [content, setContent] = useState("");
  const [writer, setWriter] = useState("");

  // 제목이 사용자의 입력에 의해 변경되면  title 상태값 변경
  const handleChangeTitle = useCallback(
    (event: React.ChangeEvent<HTMLInputElement>) => {
      setTitle(event.target.value);
    },
    []
  );

  // 내용이 변경되면 content 설정함수 호출
  const handleChangeContent = useCallback(
    (event: React.ChangeEvent<HTMLTextAreaElement>) => {
      setContent(event.target.value);
    },
    []
  );

  // 작성자
  const handleChangeWriter = useCallback(
    (event: React.ChangeEvent<HTMLInputElement>) => {
      setWriter(event.target.value);
    },
    []
  );

  // 폼 submit 이벤트 처리
  const handleSubmit = useCallback(
    (e: React.SyntheticEvent) => {
      e.preventDefault();

      // 등록 처리 함수 호출
      onRegister(title, content, writer);
    },
    [title, content, writer, onRegister]
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
                <input type="text" onChange={handleChangeTitle} />
              </td>
            </tr>
            <tr>
              <td>작성자</td>
              <td>
                <input type="text" onChange={handleChangeWriter} />
              </td>
            </tr>
            <tr>
              <td>내용</td>
              <td>
                <textarea rows={5} onChange={handleChangeContent}></textarea>
              </td>
            </tr>
          </tbody>
        </table>

        <div className={classes.align_centered}>
          <button>등록</button>
          <Link to="/">취소</Link>
        </div>
      </form>
    </div>
  );
};

export default BoardRegisterForm;
