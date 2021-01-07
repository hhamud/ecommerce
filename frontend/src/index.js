import React from "react";
import ReactDOM from "react-dom";
import "./index.css";
import { ChakraProvider } from "@chakra-ui/react";
import { BrowserRouter as Router } from "react-router-dom";
import App from "./App";




ReactDOM.render(
  <Router>
    <ChakraProvider>
      <App/>
    </ChakraProvider>
  </Router>,
  document.getElementById("root")
);
