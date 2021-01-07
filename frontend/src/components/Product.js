/* eslint-disable no-unused-vars */
import React from "react";
import { Grid, Box, Flex, Text, Image, Stack } from "@chakra-ui/react";
import axios from "axios";

class Product extends React.Component {
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
      <Box>
        <Text fontSize='4xl' align="center">Featured Products</Text>
        <Flex h="1000px" padding={4}>
          {this.state.products.map((product, i) => (
            <Stack
              key={i}
              rounded="lg"
              boxShadow="md"
              overflow="hidden"
              h="400px"
              w="200px"
              padding={4}
              align="center"
            >
              <Image
                maxW="100%"
                maxH="100%"
                boxsize="75vh"
                objectFit="cover"
                src={product.image}
                alt={product.name}
              ></Image>
              <Text>{product.name}</Text>
              <Text>${product.price}</Text>
            </Stack>
          ))}
        </Flex>
      </Box>
    );
  }
}

export default Product;
