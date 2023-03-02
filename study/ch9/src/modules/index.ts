// 루트 리듀서 정의
import { combineReducers } from "redux";

import board from "./board";
import loading from "./loading";

// 상태 인터페이스 임포트
import { BoardState } from "../modules/board";
import { LoadingState } from "../modules/loading";

// 루트 상태 인터페이스
export interface RootState {
  board: BoardState;
  loading: LoadingState;
}

// 루트 리듀서
const rootReducer = combineReducers({
  //...
  board,
  loading,
});

export default rootReducer;
