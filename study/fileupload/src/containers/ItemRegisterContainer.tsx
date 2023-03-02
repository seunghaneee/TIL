import React from "react";
import ItemRegisterForm from "../components/ItemRegisterForm";

import { useNavigate } from "react-router-dom";
import axios from "axios";

const ItemRegisterContainer = () => {
  const navigate = useNavigate();
  const onRegister = (
    itemName: string,
    price: number,
    description: string,
    file: File
  ) => {
    const itemObject = {
      itemName: itemName,
      price: price,
      description: description,
    };
    // FormData 객체 생성
    const formData = new FormData();
    formData.append("file", file);
    formData.append("item", JSON.stringify(itemObject));

    // 파일 업로드
    axios
      .post("/items", formData, {
        headers: {
          "Content-Type": "multipart/form-data",
        },
      })
      .then((res) => {
        alert("등록되었습니다.");
        navigate("/read/" + res.data.itemId);
      })
      .catch((err) => {
        alert(err);
      });
  };

  return (
    <div>
      <ItemRegisterForm onRegister={onRegister} />
    </div>
  );
};

export default ItemRegisterContainer;
