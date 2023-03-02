// 게시판 관리 구현에 필요한 리덕스 관련 코드를 모아 놓은 파일
import { createReducer } from "typesafe-actions";
import { Board } from "../App";

import { createAction } from "redux-actions";
import { fetchBoardApi } from "../lib/api";
import { Dispatch } from "redux";

// 액션 타입
const FETCH = "board/FETCH";
const FETCH_SUCCESS = "board/FETCH_SUCCESS";
const FETCH_FAILURE = "board/FETCH_FAILURE";

// 액션 생성 함수
export const fetchStart = createAction(FETCH);
export const fetchSuccess = createAction(FETCH_SUCCESS, (data: string) => data);
export const fetchFailure = createAction(FETCH_FAILURE, (err: any) => err);

// 게시글 상세 조회 Thunk 생성 함수
export const readBoardThunk =
  (boardNo: string) => async (dispatch: Dispatch) => {
    dispatch(fetchStart());
    try {
      const response = await fetchBoardApi(boardNo);

      dispatch(fetchSuccess(response.data));
    } catch (e) {
      dispatch(fetchFailure(e));

      throw e;
    }
  };

// 상태 인터페이스 정의
export interface BoardState {
  loading: { FETCH: boolean; FETCH_LIST: boolean };
  board: Board;
  boards: Board[];
  error: any;
}

// 초기 상태
const initialState: BoardState = {
  loading: {
    FETCH: false,
    FETCH_LIST: false,
  },
  board: { boardNo: "", title: "", writer: "", content: "", regDate: "" },
  boards: [],
  error: null,
};

// 리듀서 함수 정의
const board = createReducer(initialState, {
  [FETCH]: (state) => ({
    ...state,
    loading: {
      ...state.loading,
      FETCH: true,
    },
  }),
  [FETCH_SUCCESS]: (state, action) => ({
    ...state,
    loading: {
      ...state.loading,
      FETCH: false,
    },
    board: action.payload,
  }),
  [FETCH_FAILURE]: (state, action) => ({
    ...state,
    loading: {
      ...state.loading,
      FETCH: false,
    },
    error: action.payload,
  }),
});

export default board;
