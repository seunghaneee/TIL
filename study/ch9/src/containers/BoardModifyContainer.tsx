import React, { useCallback, useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useParams, useNavigate } from "react-router-dom";
import BoardModifyForm from "../components/BoardModifyForm";
import { modifyBoardApi, fetchBoardApi } from "../lib/api";
import {
  changeTitle,
  changeContent,
  // fetchStart,
  fetchSuccess,
  fetchFailure,
} from "../modules/board";

// import { BoardState } from "../modules/board";

import { startLoading, endLoading } from "../modules/loading";
import { RootState } from "../modules";

const BoardModifyContainer = () => {
  const navigate = useNavigate();
  const { boardNo = "" } = useParams<{ boardNo?: string }>();

  const dispatch = useDispatch();
  // 스토어 상태 조회
  // const { board, isLoading } = useSelector((state: BoardState) => ({
  //   board: state.board,
  //   isLoading: state.loading.FETCH,
  // }));
  const { board, isLoading } = useSelector(({ board, loading }: RootState) => ({
    board: board.board,
    isLoading: loading.FETCH,
  }));

  // 게시글 상세 조회
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

  // 수정 처리
  const onModify = async (boardNo: string, title: string, content: string) => {
    try {
      await modifyBoardApi(boardNo, title, content);
      alert("수정 완료");

      navigate("/read/" + boardNo);
    } catch (e) {
      console.log(e);
    }
  };

  const onChangeTitle = useCallback(
    (title: string) => {
      return dispatch(changeTitle(title));
    },
    [dispatch]
  );

  const onChangeContent = useCallback(
    (content: string) => {
      return dispatch(changeContent(content));
    },
    [dispatch]
  );

  useEffect(() => {
    readBoard(boardNo);
  }, [boardNo, readBoard]);
  return (
    <div>
      <BoardModifyForm
        board={board}
        isLoading={isLoading}
        onChangeTitle={onChangeTitle}
        onChangeContent={onChangeContent}
        onModify={onModify}
      />
    </div>
  );
};

export default BoardModifyContainer;
