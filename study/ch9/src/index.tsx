import React from "react";
import ReactDOM from "react-dom/client";
import "./index.css";
import App from "./App";

import { BrowserRouter } from "react-router-dom";

// 리덕스 적용을 위한 모듈 불러오기
import { createStore } from "redux";
import { Provider } from "react-redux";
// import board from "./modules/board";
import { composeWithDevTools } from "redux-devtools-extension";

// 루트 리듀서 적용
import rootReducer from "./modules";

// const store = createStore(board, composeWithDevTools());
// 루트 리듀서 전달받은 스토어 생성
const store = createStore(rootReducer, composeWithDevTools());

const root = ReactDOM.createRoot(
  document.getElementById("root") as HTMLElement
);
root.render(
  <Provider store={store}>
    <React.StrictMode>
      <BrowserRouter>
        <App />
      </BrowserRouter>
    </React.StrictMode>
  </Provider>
);
