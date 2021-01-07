import React, { Component } from "react";
import { HStack, Link, Box } from "@chakra-ui/react";
import { Link as reactlink } from "react-router-dom";

class Navbar extends Component {
  render() {
    return (
      <Box>
        <HStack spacing="24px">
          <Link as={reactlink} to="/shop">
            Shop
          </Link>
          <Link as={reactlink} to="/contact">
            Contact
          </Link>
          <Link as={reactlink} to="/checkout">
            Checkout
          </Link>
        </HStack>
      </Box>
    );
  }
}

export default Navbar;
