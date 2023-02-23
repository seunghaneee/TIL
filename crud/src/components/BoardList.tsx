import React from "react";
import { Link } from "react-router-dom";
import classes from "../Board.module.css";

import { Board } from "../App";

interface Props {
  readonly boards: Board[];
  readonly isLoading: boolean;
}

// 목록 컴포넌트
const BoardList = ({ boards, isLoading }: Props) => {
  return (
    <div className={classes.centered}>
      <h2>게시판 목록</h2>
      {isLoading && "로딩중"}
      {!isLoading && boards && (
        <>
          <Link to="/create">새로만들기</Link>
          <table className={classes.board_table}>
            <thead>
              <tr>
                <th className={classes.board_no}>번호</th>
                <th className={classes.board_title}>제목</th>
                <th className={classes.board_writer}>작성자</th>
                <th className={classes.board_date}>등록일시</th>
              </tr>
            </thead>
            <tbody>
              {/* 게시글 목록 표시 */}
              {!boards.length && (
                <tr>
                  <td colSpan={4}>List is empty</td>
                </tr>
              )}
              {!!boards.length &&
                boards.map((board) => (
                  <tr key={board.boardNo}>
                    <td align="center">{board.boardNo}</td>
                    <td align="left">
                      <Link to={`/read/${board.boardNo}`}>{board.title}</Link>
                    </td>
                    <td align="right">{board.writer}</td>
                    <td align="center">{board.regDate}</td>
                  </tr>
                ))}
            </tbody>
          </table>
        </>
      )}
    </div>
  );
};

export default BoardList;
