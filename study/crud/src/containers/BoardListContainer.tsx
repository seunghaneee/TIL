// 게시물 목록 조회 기능 수행
// 게시물 목록 컴포넌트 표시

import React, { useState, useEffect } from "react";
import BoardList from "../components/BoardList";

import * as client from "../lib/api";
import { Board } from "../App";

// 목록조회 컨테이너 컴포넌트
const BoardListContainer = () => {
  const [boards, setBoards] = useState<Board[]>([]);
  const [isLoading, setIsLoading] = useState(false);
  // 게시글 목록 조회
  const listBoard = async () => {
    setIsLoading(true);
    try {
      const response = await client.fetchBoardList();
      setBoards(response.data.reverse());
      // console.log(response.data);
      setIsLoading(false);
    } catch (e) {
      setIsLoading(false);
      throw e;
    }
  };

  useEffect(() => {
    listBoard();
  }, []);
  return <BoardList boards={boards} isLoading={isLoading} />;
};

export default BoardListContainer;
