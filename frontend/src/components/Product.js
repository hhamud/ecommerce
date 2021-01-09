/* eslint-disable no-unused-vars */
import React from "react";
import {
  Box,
  Flex,
  Text,
  Image,
  Stack,
  Spacer,
  Wrap,
  WrapItem,
} from "@chakra-ui/react";
import { Link } from "react-router-dom";

class Product extends React.Component {
  render() {
    return (
      <Box>
        <Text fontSize="4xl" align="center">
          Featured Products
        </Text>

        <Wrap h="1000px" padding={4} justify='center'>
          {this.props.products.map((product, i) => (
            <>
              <WrapItem padding={4} >
                <Link to={product.slug} key={i}>
                  <Stack
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
                </Link>
              </WrapItem>
            </>
          ))}
        </Wrap>
      </Box>
    );
  }
}

export default Product;
