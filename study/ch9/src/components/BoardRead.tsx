import React from "react";
import { Link } from "react-router-dom";
import classes from "../Board.module.css";
import { Board } from "../App";

interface Props {
  readonly boardNo: string;
  readonly board?: Board;
  readonly isLoading: boolean;
  // 삭제 추가
  readonly onRemove: () => void;
}

const BoardRead = ({ boardNo, board, isLoading, onRemove }: Props) => {
  return (
    <div className={classes.centered}>
      <h2>게시판 상세보기</h2>
      {isLoading && "로딩중..."}
      {!isLoading && board && (
        <>
          <table>
            <tbody>
              <tr>
                <td>번호</td>
                <td>
                  <input type="text" value={board.boardNo} readOnly />
                </td>
              </tr>
              <tr>
                <td>등록일시</td>
                <td>
                  <input type="text" value={board.regDate} readOnly />
                </td>
              </tr>
              <tr>
                <td>제목</td>
                <td>
                  <input type="text" value={board.title} readOnly />
                </td>
              </tr>
              <tr>
                <td>작성자</td>
                <td>
                  <input type="text" value={board.writer} readOnly />
                </td>
              </tr>
              <tr>
                <td>내용</td>
                <td>
                  <textarea value={board.content} readOnly></textarea>
                </td>
              </tr>
            </tbody>
          </table>
        </>
      )}
      <div>
        <Link to={`/edit/${boardNo}`}>편집</Link>
        <button onClick={onRemove}>삭제</button>
        <Link to="/">목록</Link>
      </div>
    </div>
  );
};

export default BoardRead;
