// 게시글 상세정보

import React from "react";
import { Link } from "react-router-dom";
import classes from "../Board.module.css";

// 사용자가 정의한 타입스크립트 인터페이스 가져오기
import { Board } from "../App";

interface Props {
  readonly boardNo: string;
  readonly board?: Board;
  readonly isLoading: boolean;
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
          <div className={classes.align_centered}>
            <Link to={`/edit/${boardNo}`}>편집</Link>
            <button onClick={onRemove}>삭제</button>
            <Link to="/">목록</Link>
          </div>
        </>
      )}
    </div>
  );
};

export default BoardRead;
