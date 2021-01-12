import React, { Component } from "react";
import {
  Box,
  Text,
  Image,
  Stat,
  StatNumber,
  VStack,
  Select,
  Divider,
  Flex,
  Button,
  HStack,
} from "@chakra-ui/react";
import axios from "axios";
import { Link } from 'react-router-dom'


class ProductDetail extends Component {
  constructor(props) {
    super(props);
    this.state = {
      productdetail: [],
    };
  }

  componentDidMount() {
    const base_url = process.env.REACT_APP_API_ENDPOINT;
    axios
      .get(`${base_url}/products/${this.props.ip.name}`)
      .then((res) => {
        this.setState({ productdetail: res.data });
      })
      .catch((err) => console.log(err));
  }
  render() {
    return (
      <Box
        display="flex"
        flexDir="column"
        justifyContent="center"
        alignItems="center"
        minH="100vh"
      >
        <Flex direction={["column", "row"]} spacing="100px" w="60vw">
          <Image
            maxW="300px"
            objectFit="cover"
            src={this.props.ip.image}
            alt={this.props.ip.name}
          />
          <VStack w="50vw" paddingLeft="30px" paddingTop="30px">
            <Text>{this.props.ip.name}</Text>
            <Stat>
              <StatNumber>£{this.props.ip.price}</StatNumber>
            </Stat>
            <Text>{this.props.ip.description}</Text>
            <HStack direction={["row"]}>
              <Box>
                <Select placeholder="Size" maxW="5vw" minW="100px">
                  <option value="option1">option 1</option>
                </Select>
              </Box>

             
              <Box>
                <Select placeholder="Colour" maxW="5vw" minW="100px">
                  <option value="Black">Black</option>
                </Select>
              </Box>
            </HStack>
            <Divider orientation="horizontal" />
            <Button onClick={() => (console.log('added product to cart'))}> Buy </Button>
          </VStack>
        </Flex>
      </Box>
    );
  }
}

export default ProductDetail;
