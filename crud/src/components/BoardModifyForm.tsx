// 게시글 수정 폼

import React, { useState, useEffect } from "react";
import { Link } from "react-router-dom";
import classes from "../Board.module.css";
import { Board } from "../App";

interface Props {
  readonly board?: Board;
  readonly isLoading: boolean;
  readonly onModify: (boardNo: string, title: string, content: string) => void;
}
function BoardModifyForm({ board, isLoading, onModify }: Props) {
  // 컴포넌트 상태 설정
  const [title, setTitle] = useState("");
  const [content, setContent] = useState("");

  // 제목의 변경 처리
  const handleChangeTitle = (e: React.ChangeEvent<HTMLInputElement>) => {
    setTitle(e.target.value);
  };

  // 내용 변경 처리
  const handleChangeContent = (e: React.ChangeEvent<HTMLTextAreaElement>) => {
    setContent(e.target.value);
  };

  // submit
  const handleSubmit = (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();

    if (!!board) {
      onModify(board.boardNo, title, content);
    }
  };

  // 마운트될 때 게시글 상세정보 가져오기
  useEffect(() => {
    console.log("useEffect board" + board);
    if (board) {
      setTitle(board.title);
      setContent(board.content);
    }
  }, [board]);
  return (
    <div className={classes.centered}>
      <h2>게시판 수정</h2>
      {isLoading && "로딩중..."}
      {!isLoading && board && (
        <>
          <form onSubmit={handleSubmit}>
            <table>
              <tbody>
                <tr>
                  <td>번호</td>
                  <td>
                    <input type="text" value={board.boardNo} disabled />
                  </td>
                </tr>
                <tr>
                  <td>등록일시</td>
                  <td>
                    <input type="text" value={board.regDate} disabled />
                  </td>
                </tr>
                <tr>
                  <td>제목</td>
                  <td>
                    <input
                      type="text"
                      value={title}
                      onChange={handleChangeTitle}
                    />
                  </td>
                </tr>
                <tr>
                  <td>작성자</td>
                  <td>
                    <input type="text" value={board.writer} disabled />
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
              <button type="submit">수정</button>
              <Link to={`/read/${board.boardNo}`}>취소</Link>
            </div>
          </form>
        </>
      )}
    </div>
  );
}

export default BoardModifyForm;
