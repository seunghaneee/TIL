import "./App.css";

// 라우트 전용 컴포넌트 불러오기
import { Route, Routes } from "react-router-dom";
// 게시판 컴포넌트 불러오기
import BoardListContainer from "./containers/BoardListContainer";
import BoardRegisterContainer from "./containers/BoardRegisterContainer";
import BoardModifyContainer from "./containers/BoardModifyContainer";
import BoardReadContainer from "./containers/BoardReadContainer";

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
