import React from "react";
import "./App.css";

import { Route, Routes } from "react-router-dom";
import BoardListContainer from "./containers/BoardListContainer";
import BoardReadContainer from "./containers/BoardReadContainer";
import BoardRegisterContainer from "./containers/BoardRegisterContainer";
import BoardModifyContainer from "./containers/BoardModifyContainer";

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
      <Route path="/" element={<BoardListContainer />} />
      <Route path="/create" element={<BoardRegisterContainer />} />
      <Route path="/edit/:boardNo" element={<BoardModifyContainer />} />
      <Route path="/read/:boardNo" element={<BoardReadContainer />} />
    </Routes>
  );
}

export default App;
