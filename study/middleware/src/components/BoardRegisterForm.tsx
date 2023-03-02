import React, { useState, useCallback } from "react";
import { Link } from "react-router-dom";

interface Props {
  readonly onRegister: (title: string, content: string, writer: string) => void;
}
const BoardRegisterForm = ({ onRegister }: Props) => {
  // 사용자가 원하는 값을 입력하는 화면 요소에 바인딩할 상태를 설정
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
    (e: React.FormEvent<HTMLFormElement>) => {
      e.preventDefault();
      onRegister(title, content, writer);
    },
    [title, content, writer, onRegister]
  );

  return (
    <div>
      <h2>게시판 등록</h2>
      <form onSubmit={handleSubmit}>
        <div>
          <label htmlFor="title">제목</label>
          <input type="text" value={title} onChange={handleChangeTitle} />
        </div>
        <div>
          <label htmlFor="writer">작성자</label>
          <input type="text" value={writer} onChange={handleChangeWriter} />
        </div>
        <div>
          <label htmlFor="content">내용</label>
          <textarea
            rows={5}
            value={content}
            onChange={handleChangeContent}
          ></textarea>
        </div>
        <div>
          <button type="submit">등록</button>
          <Link to="/">취소</Link>
        </div>
      </form>
    </div>
  );
};

export default BoardRegisterForm;
