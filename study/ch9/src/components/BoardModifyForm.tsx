import React from "react";
import { Link } from "react-router-dom";
import classes from "../Board.module.css";

import { Board } from "../App";

interface Props {
  readonly board?: Board;
  readonly isLoading: boolean;
  readonly onModify: (boardNo: string, title: string, content: string) => void;
  readonly onChangeTitle: (title: string) => void;
  readonly onChangeContent: (content: string) => void;
}

const BoardModifyForm = ({
  board,
  isLoading,
  onChangeTitle,
  onChangeContent,
  onModify,
}: Props) => {
  const handleChangeTitle = (e: React.ChangeEvent<HTMLInputElement>) => {
    onChangeTitle(e.target.value);
  };

  const handleChangeContent = (e: React.ChangeEvent<HTMLTextAreaElement>) => {
    onChangeContent(e.target.value);
  };

  const handleSubmit = (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();

    if (!!board) {
      onModify(board.boardNo, board.title, board.content);
    }
  };
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
                  <td>제목</td>
                  <td>
                    <input
                      type="text"
                      value={board.title}
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
                      value={board.content}
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
};

export default BoardModifyForm;
