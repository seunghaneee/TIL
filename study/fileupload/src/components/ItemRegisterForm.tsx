import React, { useState, useCallback } from "react";
import { Link } from "react-router-dom";

interface Props {
  readonly onRegister: (
    itemName: string,
    price: number,
    description: string,
    file: File
  ) => void;
}
const ItemRegisterForm = ({ onRegister }: Props) => {
  // 바인딩
  const [itemName, setItemName] = useState("");
  const [price, setPrice] = useState(0);
  const [description, setDescription] = useState("");
  const [file, setFile] = useState<File>();

  const handleChangeItemName = useCallback(
    (event: React.ChangeEvent<HTMLInputElement>) => {
      setItemName(event.target.value);
    },
    []
  );

  const handleChangePrice = useCallback(
    (e: React.ChangeEvent<HTMLInputElement>) => {
      setPrice(parseInt(e.target.value));
    },
    []
  );

  const handleChangeDescription = useCallback(
    (event: React.ChangeEvent<HTMLTextAreaElement>) => {
      setDescription(event.target.value);
    },
    []
  );

  const handleChangeFile = useCallback(
    (event: React.ChangeEvent<HTMLInputElement>) => {
      if (event.target.files) {
        console.log(event.target.files[0]);

        setFile(event.target.files[0]);
      }
    },
    []
  );

  const handleSubmit = useCallback(
    (e: React.FormEvent<HTMLFormElement>) => {
      e.preventDefault();
      if (file) {
        onRegister(itemName, price, description, file);
      }
    },
    [onRegister, itemName, price, description, file]
  );

  return (
    <div>
      <h2>상품등록</h2>
      <form onSubmit={handleSubmit}>
        <table>
          <tbody>
            <tr>
              <td>상품명</td>
              <td>
                <input
                  type="text"
                  value={itemName}
                  onChange={handleChangeItemName}
                />
              </td>
            </tr>
            <tr>
              <td>상품가격</td>
              <td>
                <input type="text" value={price} onChange={handleChangePrice} />
                원
              </td>
            </tr>
            <tr>
              <td>상품파일</td>
              <td>
                <input type="file" onChange={handleChangeFile} />
              </td>
            </tr>
            <tr>
              <td>상품설명</td>
              <td>
                <textarea
                  rows={5}
                  value={description}
                  onChange={handleChangeDescription}
                ></textarea>
              </td>
            </tr>
          </tbody>
        </table>
        <div>
          <button type="submit">등록</button>
          <Link to="/">취소</Link>
        </div>
      </form>
    </div>
  );
};

export default ItemRegisterForm;
