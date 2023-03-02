import React, { useEffect } from "react";
// 리덕스 관련 훅
import { useDispatch, useSelector } from "react-redux";

import BoardRead from "../components/BoardRead";

// 게시글 상세 조회 Thunk 생성 함수 임포트
import { readBoardThunk } from "../modules/board";
// 상태 인터페이스 임포트
import { BoardState } from "../modules/board";

import { useParams } from "react-router-dom";

const BoardReadContainer = () => {
  const { boardNo = "" } = useParams<{ boardNo?: string }>();
  const dispatch = useDispatch();
  // 스토어 상태 조회
  const { board, isLoading } = useSelector((state: BoardState) => ({
    board: state.board,
    isLoading: state.loading.FETCH,
  }));

  // 마운트될 때 게시글 상세정보를 가져옴
  useEffect(() => {
    dispatch(readBoardThunk(boardNo));
  });

  return (
    <div>
      <BoardRead boardNo={boardNo} board={board} isLoading={isLoading} />
    </div>
  );
};

export default BoardReadContainer;
