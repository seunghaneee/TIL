import React from "react";
import "./App.css";

import { Route, Routes } from "react-router-dom";

import ItemListContainer from "./containers/ItemListContainer";
import ItemRegisterContainer from "./containers/ItemRegisterContainer";
import ItemModifyContainer from "./containers/ItemModifyContainer";
import ItemReadContainer from "./containers/ItemReadContainer";

export interface Item {
  readonly itemId: string;
  readonly itemName: string;
  readonly price: number;
  readonly description: string;
}
function App() {
  return (
    <Routes>
      <Route path="/" element={<ItemListContainer />} />
      <Route path="/create" element={<ItemRegisterContainer />} />
      <Route path="/edit/:itemId" element={<ItemModifyContainer />} />
      <Route path="/read/:itemId" element={<ItemReadContainer />} />
    </Routes>
  );
}

export default App;
