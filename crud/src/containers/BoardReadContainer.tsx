// 게시글 상세 조회 기능 수행
// 게시글 상세보기 컴포넌트 표시

import React, { useState, useEffect } from "react";
import BoardRead from "../components/BoardRead";
import { useParams, useNavigate } from "react-router-dom";
import * as client from "../lib/api";

import { Board } from "../App";

// 상세조회 컨테이너 컴포넌트
const BoardReadContainer = () => {
  // match 객체의 params 속성값을 참조
  const { boardNo = "" } = useParams<{ boardNo?: string }>();

  const navigate = useNavigate();

  // 컴포넌트 상태 선언
  const [board, setBoard] = useState<Board>();
  const [isLoading, setIsLoading] = useState(false);

  const readBoard = async (boardNo: any) => {
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

  const onRemove = async () => {
    console.log("boardNo=" + boardNo);
    try {
      await client.removeBoard(boardNo);
      alert("삭제완료");
      navigate("/");
    } catch (e) {
      console.log(e);
    }
  };

  return (
    <BoardRead
      boardNo={boardNo}
      board={board}
      isLoading={isLoading}
      onRemove={onRemove}
    />
  );
};

export default BoardReadContainer;
