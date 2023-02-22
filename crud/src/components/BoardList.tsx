import React from "react";
import { Link } from "react-router-dom";
import classes from "../Board.module.css";

// 목록 컴포넌트
const BoardList = () => {
  return (
    <div className={classes.centered}>
      <h2>게시판 목록</h2>
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
          <tr>
            <td align="center">100</td>
            <td align="left">
              <Link to="/read/100">무제</Link>
            </td>
            <td align="right">홍길동</td>
            <td align="center">2020-06-05</td>
          </tr>
        </tbody>
      </table>
    </div>
  );
};

export default BoardList;
