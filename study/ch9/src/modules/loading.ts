// REST API 통신할 때 지연현상을 시각적으로 보완하기 위한 리덕스 모듈 파일

import { createAction } from "redux-actions";
import { createReducer } from "typesafe-actions";

// 액션 타입
const START_LOADING = "loading/START_LOADING";
const END_LOADING = "loading/END_LOADING";

// 액션 생성 함수
export const startLoading = createAction(
  START_LOADING,
  (actionType: string) => actionType
);
export const endLoading = createAction(
  END_LOADING,
  (actionType: string) => actionType
);

// 상태 인터페이스 정의
export interface LoadingState {
  // 지연 처리 모듈 생성
  FETCH: boolean;
  FETCH_LIST: boolean;
}

// 초기 상태
const initialState: LoadingState = {
  // ...
  FETCH: false,
  FETCH_LIST: false,
};

// 리듀서 함수 정의
const loading = createReducer(initialState, {
  [START_LOADING]: (state, action) => ({
    ...state,
    [action.payload]: true,
  }),
  [END_LOADING]: (state, action) => ({
    ...state,
    [action.payload]: false,
  }),
});

export default loading;
