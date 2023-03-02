import React, { useEffect, useCallback } from "react";
import { useDispatch, useSelector } from "react-redux";
import BoardList from "../components/BoardList";

import { startLoading, endLoading } from "../modules/loading";
import { RootState } from "../modules";
// 액션 생성 함수 임포트
import {
  // fetchListStart,
  fetchListSuccess,
  fetchListFailure,
} from "../modules/board";
// 서버 api 통신 모듈 임포트
import { fetchBoardListApi } from "../lib/api";

// 사용자가 정의한 상테 인터페이스 가져오기
// import { BoardState } from "../modules/board";

const BoardListContainer = () => {
  const dispatch = useDispatch();

  // 스토어 상태 조회
  // const { boards, isLoading } = useSelector((state: BoardState) => ({
  //   boards: state.boards,
  //   isLoading: state.loading.FETCH_LIST,
  // }));
  const { boards, isLoading } = useSelector(
    ({ board, loading }: RootState) => ({
      boards: board.boards,
      isLoading: loading.FETCH_LIST,
    })
  );

  // 게시글 목록 조회
  const listBoard = useCallback(async () => {
    // dispatch(fetchListStart());
    dispatch(startLoading("FETCH_LIST"));
    try {
      const response = await fetchBoardListApi();

      dispatch(fetchListSuccess(response.data));

      // 로딩 마침 액션 디스패치
      dispatch(endLoading("FETCH_LIST"));
    } catch (e) {
      dispatch(fetchListFailure(e));
      dispatch(endLoading("FETCH_LIST"));
    }
  }, [dispatch]);

  // 마운트될 때 게시글 목록 가져오기
  useEffect(() => {
    listBoard();
  }, [listBoard]);

  return <BoardList boards={boards} isLoading={isLoading} />;
};

export default BoardListContainer;
