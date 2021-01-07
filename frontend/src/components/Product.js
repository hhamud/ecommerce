import React, { Component } from "react";
import { Grid, Box, Text, Image } from "@chakra-ui/react";
import axios from "axios";

class Product extends Component {
  componentDidMount() {
    const base_url = process.env.REACT_APP_API_ENDPOINT;
    axios
      .get(`${base_url}/products/`)
      .then((response) => {
        this.setState({ products: response.data });
      })
      .catch((err) => console.log(err));
    console.log(this.state.products);
  }

  render() {
    return (
      <Grid h="1000px" bg="black">
        {this.state.products.map((product) => (
          <Box>
            <Image src={product.image} alt=""></Image>
            <Text>{product.name}</Text>
            <Text>{product.price}</Text>
          </Box>
        ))}
      </Grid>
    );
  }
}

export default Product;
