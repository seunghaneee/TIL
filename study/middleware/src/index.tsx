import React from "react";
import ReactDOM from "react-dom/client";
import "./index.css";
import App from "./App";
import reportWebVitals from "./reportWebVitals";

import { BrowserRouter } from "react-router-dom";

// 리덕스 적용을 위해 필요한 모듈 불러온다.
import { createStore, applyMiddleware } from "redux";
import { Provider } from "react-redux";
import board from "./modules/board";
import { composeWithDevTools } from "redux-devtools-extension";

import ReduxThunk from "redux-thunk";

const store = createStore(
  board,
  composeWithDevTools(applyMiddleware(ReduxThunk))
);
const root = ReactDOM.createRoot(
  document.getElementById("root") as HTMLElement
);
root.render(
  // Provider 컴포넌트를 사용하여 프로젝트에 리덕스를 적용한다.
  <Provider store={store}>
    <BrowserRouter>
      <React.StrictMode>
        <App />
      </React.StrictMode>
    </BrowserRouter>
  </Provider>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
