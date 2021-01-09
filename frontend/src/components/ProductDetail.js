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
  Flex
} from "@chakra-ui/react";
import axios from "axios";

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
    console.log(this.props);
    return (
      <Box
        display="flex"
        flexDir="column"
        justifyContent="center"
        alignItems="center"
        minH="100vh"
      >
        <Flex direction={["column", "row"]} spacing='100px' w='60vw'>
          <Image maxWidth='400px' h='auto' src={this.props.ip.image} />
          <VStack w='50vw'>
            <Text>{this.props.ip.name}</Text>
            <Stat>
              <StatNumber>£{this.props.ip.price}</StatNumber>
            </Stat>
            <Text>{this.props.ip.description}</Text>
            <Select placeholder="Size" maxW='10vw'>
              <option value="option1">option 1</option>
            </Select>
            <Divider orientation='horizontal'/>
          </VStack>
        </Flex>
      </Box>
    );
  }
}

export default ProductDetail;
