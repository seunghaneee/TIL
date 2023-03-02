import React from "react";
import { Link } from "react-router-dom";

const BoardModifyForm = () => {
  return (
    <div>
      <h2>게시판 수정</h2>
      <form action="">
        <tbody>
          <tr>
            <td>번호</td>
            <td>
              <input type="text" value="100" disabled />
            </td>
          </tr>
          <tr>
            <td>제목</td>
            <td>
              <input type="text" />
            </td>
          </tr>
          <tr>
            <td>작성자</td>
            <td>
              <input type="text" value="홍길동" disabled />
            </td>
          </tr>
          <tr>
            <td>내용</td>
            <td>
              <textarea rows={5}></textarea>
            </td>
          </tr>
        </tbody>

        <div>
          <button type="submit">수정</button>
          <Link to={`/read/100`}>취소</Link>
        </div>
      </form>
    </div>
  );
};

export default BoardModifyForm;
