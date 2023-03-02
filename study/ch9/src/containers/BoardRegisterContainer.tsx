import React from "react";
import BoardRegisterForm from "../components/BoardRegisterForm";

import { useNavigate } from "react-router-dom";
import { registerBoardApi } from "../lib/api";
const BoardRegisterContainer = () => {
  const navigate = useNavigate();

  const onRegister = async (title: string, content: string, writer: string) => {
    try {
      const response = await registerBoardApi(title, content, writer);
      console.log(response);
      alert("등록 성공");

      navigate("/read/" + response.data.boardNo);
    } catch (e) {
      console.log(e);
    }
  };
  return (
    <div>
      <BoardRegisterForm onRegister={onRegister} />
    </div>
  );
};

export default BoardRegisterContainer;
