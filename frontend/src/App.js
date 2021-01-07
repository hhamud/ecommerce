/* eslint-disable no-unused-vars */
import React, { Component, Fragment } from "react";
import Header from "./components/Layout/Header";
import Contact from "./components/Layout/Contact";
import Footer from "./components/Layout/Footer";
import Main from "./components/Layout/Main";
import { Switch, Route, withRouter } from "react-router-dom";
import Checkout from "./components/Checkout";
import Login from "./components/Login";
import Account from "./components/Account";
import Product from "./components/Product";

class App extends Component {
  render() {
    return (
      <Switch>
        <Route path="/shop" component={Product} />
        <Route path="/contact" component={Contact} />
        <Route path="/checkout" component={Checkout} />
        <Route path="/login" component={Login} />
        <Route path="/account" component={Account} />
        <Route
          exact path="/"
          render={(props) => (
            <Fragment>
              <Header />
              <Main />
              <Product />
              <Footer />
            </Fragment>
          )}
        ></Route>
      </Switch>
    );
  }
}

export default App;
