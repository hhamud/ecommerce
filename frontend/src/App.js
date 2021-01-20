/* eslint-disable no-unused-vars */
import React, { Component, Fragment } from "react";
import Header from "./components/Layout/Header";
import Contact from "./components/Layout/Contact";
import Footer from "./components/Layout/Footer";
import Main from "./components/Layout/Main";
import { Switch, Route } from "react-router-dom";
import Login from "./components/Auth/Login";
import SignUp from "./components/Auth/SignUp";
import Account from "./components/Shop/Account";
import Product from "./components/Shop/Product";
import ProductDetail from "./components/Shop/ProductDetail";
import axios from "axios";

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      products: [],
    };
  }

  componentDidMount() {
    const base_url = process.env.REACT_APP_API_ENDPOINT;
    axios
      .get(`${base_url}/products/`)
      .then((res) => {
        this.setState({ products: res.data });
      })
      .catch((err) => console.log(err));
  }

  render() {
    return (
      <Switch>
        <Route path="/shop" component={Product} />
        <Route path="/contact" component={Contact} />
        <Route path="/login" component={Login} />
        <Route path="/signup" component={SignUp} />
        <Route path="/account" component={Account} />
        <Route exact path="/">
          <Fragment>
            <Header />
            <Main />
            <Product products={this.state.products} />
            <Footer />
          </Fragment>
        </Route>
        {this.state.products.map((product, i) => (
          <Route path={`/${product.slug}`} key={i}>
            <Fragment>
              <Header />
              <ProductDetail ip={product} />
              <Footer />
            </Fragment>
          </Route>
        ))}
      </Switch>
    );
  }
}

export default App;
