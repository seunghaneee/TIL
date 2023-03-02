import React from "react";
import { Link } from "react-router-dom";

const ItemList = () => {
  return (
    <div>
      <h2>상품 목록</h2>
      <Link to="/create">새로만들기</Link>
      <table>
        <thead>
          <tr>
            <th>상품아이디</th>
            <th>상품평</th>
            <th>상품가격</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td align="center">100</td>
            <td>
              <Link to={`/read/100`}>풍경사진</Link>
            </td>
            <td>1000원</td>
          </tr>
        </tbody>
      </table>
    </div>
  );
};

export default ItemList;
