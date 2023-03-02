import React from "react";
import { Route, Routes } from "react-router-dom";

import BoardListContainer from "./containers/BoardListContainer";
import BoardModifyContainer from "./containers/BoardModifyContainer";
import BoardReadContainer from "./containers/BoardReadContainer";
import BoardRegisterContainer from "./containers/BoardRegisterContainer";

import "./App.css";

// 타입스크립트 인터페이스 정의
export interface Board {
  readonly boardNo: string;
  readonly title: string;
  readonly writer: string;
  readonly content: string;
  readonly regDate: string;
}

function App() {
  return (
    <Routes>
      <Route path="/" element={<BoardListContainer />}></Route>
      <Route path="/create" element={<BoardRegisterContainer />}></Route>
      <Route path="/edit/:boardNo" element={<BoardModifyContainer />}></Route>
      <Route path="/read/:boardNo" element={<BoardReadContainer />}></Route>
    </Routes>
  );
}

export default App;
