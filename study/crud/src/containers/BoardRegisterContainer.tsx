// 게시글 등록 기능 수행
// 게시글 등록 폼 컴포넌트 표시

import React from "react";
import BoardRegisterForm from "../components/BoardRegisterForm";
import { useNavigate } from "react-router-dom";

import * as client from "../lib/api";

// 등록 컨테이너 컴포넌트
const BoardRegisterContainer = () => {
  const navigate = useNavigate();

  // 등록 처리
  const onRegister = async (title: string, content: string, writer: string) => {
    try {
      const response = await client.registerBoard(title, content, writer);

      alert("등록되었습니다.");
      navigate("/read/" + response.data.boardNo);
    } catch (e) {
      console.log(e);
    }
  };
  return (
    <div>
      {/* 등록 처리 함수 전달 */}
      <BoardRegisterForm onRegister={onRegister} />
    </div>
  );
};

export default BoardRegisterContainer;
