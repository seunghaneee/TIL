// 게시글 수정 기능 수행
// 게시글 수정 폼 컴포넌트 표시

import React, { useState, useEffect } from "react";
import { useNavigate, useParams } from "react-router-dom";
import BoardModifyForm from "../components/BoardModifyForm";

import * as client from "../lib/api";
import { Board } from "../App";

// 수정 컨테이너 컴포넌트
const BoardModifyContainer = () => {
  const { boardNo = "" } = useParams<{ boardNo?: string }>();
  const navigate = useNavigate();

  const [board, setBoard] = useState<Board>();
  const [isLoading, setIsLoading] = useState(false);

  // 수정 처리
  const onModify = async (boardNo: string, title: string, content: string) => {
    try {
      await client.modifyBoard(boardNo, title, content);
      alert("수정 완료");
      navigate("/read/" + boardNo);
    } catch (e) {
      console.log(e);
    }
  };

  // 게시글 상세 조회
  const readBoard = async (boardNo: string) => {
    setIsLoading(true);
    try {
      const response = await client.fetchBoard(boardNo);
      setBoard(response.data);
      setIsLoading(false);
    } catch (e) {
      throw e;
    }
  };

  useEffect(() => {
    readBoard(boardNo);
  }, [boardNo]);
  return (
    <BoardModifyForm board={board} isLoading={isLoading} onModify={onModify} />
  );
};

export default BoardModifyContainer;
