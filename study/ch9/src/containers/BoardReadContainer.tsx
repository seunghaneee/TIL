import React, { useEffect, useCallback } from "react";
import { useDispatch, useSelector } from "react-redux";
import BoardRead from "../components/BoardRead";
// 사용자가 정의한 상태 인터페이스 가져오기
import { BoardState } from "../modules/board";
import { useParams } from "react-router-dom";

import { fetchBoardApi, removeBoardApi } from "../lib/api";

// 액션 생성 함수 불러오기
import {
  // fetchStart,
  fetchSuccess,
  fetchFailure,
} from "../modules/board";

// 삭제하고 나면 목록으로 돌아가기 위해 useNavigate 사용하기
import { useNavigate } from "react-router-dom";

import { startLoading, endLoading } from "../modules/loading";
import { RootState } from "../modules";

const BoardReadContainer = () => {
  // 스토어 dispatch 접근
  const dispatch = useDispatch();

  // navigate 사용
  const navigate = useNavigate();

  // params 값 참조
  const { boardNo = "" } = useParams<{ boardNo?: string }>();

  // 스토어 상태 조회
  // const { board, isLoading } = useSelector((state: BoardState) => ({
  //   board: state.board,
  //   isLoading: state.loading.FETCH,
  // }));
  const { board, isLoading } = useSelector(({ board, loading }: RootState) => ({
    board: board.board,
    isLoading: loading.FETCH,
  }));
  const readBoard = useCallback(
    async (boardNo: string) => {
      // dispatch(fetchStart());
      dispatch(startLoading("FETCH"));
      try {
        const response = await fetchBoardApi(boardNo);
        dispatch(fetchSuccess(response.data));
        dispatch(endLoading("FETCH"));
      } catch (e) {
        dispatch(fetchFailure(e));
        dispatch(endLoading("FETCH"));

        throw e;
      }
    },
    [dispatch]
  );

  const onRemove = async () => {
    try {
      await removeBoardApi(boardNo);
      alert("삭제되었습니다.");
      navigate("/");
    } catch (e) {
      console.log(e);
    }
  };

  useEffect(() => {
    readBoard(boardNo);
  }, [boardNo, readBoard]);

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
