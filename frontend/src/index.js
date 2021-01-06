import React, { Fragment } from "react";
import ReactDOM from "react-dom";
import "./index.css";
import { ChakraProvider } from "@chakra-ui/react";
import Header from "./components/Layout/Header";
import Contact from "./components/Layout/Contact";
import Footer from "./components/Layout/Footer";
import Main from "./components/Layout/Main";
import { BrowserRouter as Router, Switch, Route } from "react-router-dom";
import Checkout from "./components/Checkout";
import Login from "./components/Login";
import Account from "./components/Account";


ReactDOM.render(
  <Router>
    <ChakraProvider>
      <Switch>
        <Route
          path="/"
          render={(props) => (
            <Fragment>
              <Header />
              <Main/>
              <Footer />
            </Fragment>
          )}
        ></Route>
        <Route path="/shop" component={} />
        <Route path="/contact" component={Contact} />
        <Route path="/checkout" component={Checkout} />
        <Route path="/login" component={Login} />
        <Route path="/account" component={Account} />
      </Switch>
    </ChakraProvider>
  </Router>,
  document.getElementById("root")
);
