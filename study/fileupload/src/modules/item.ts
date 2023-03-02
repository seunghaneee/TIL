// 상품 관리 구현에 필요한 리덕스 관련 코드를 모아 놓은 파일
import { createReducer } from "typesafe-actions";
import { Item } from "../App";

// 상품 사가 함수 작성
export function* itemSaga() {}

// 상태 인터페이스 정의
export interface ItemState {
  item: Item;
  items: Item[];
  error: any;
}

// 초기상태
const initialState: ItemState = {
  item: { itemId: "", itemName: "", price: 0, description: "" },
  items: [],
  error: null,
};

// 리듀서 함수 정의
const item = createReducer(initialState, {});

export default item;
