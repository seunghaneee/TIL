import React from "react";
import { Link } from "react-router-dom";

const BoardList = () => {
  return (
    <div>
      <h2>게시판 목록</h2>
      <Link to="/create">새로만들기</Link>
      <table>
        <thead>
          <tr>
            <th>번호</th>
            <th>제목</th>
            <th>작성자</th>
            <th>등록일시</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>100</td>
            <td>
              <Link to="/read/100">무제</Link>
            </td>
            <td>홍길동</td>
            <td>2020-06-05</td>
          </tr>
        </tbody>
      </table>
    </div>
  );
};

export default BoardList;
