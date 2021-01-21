import React, { Component } from "react";
import { HStack  , Box } from "@chakra-ui/react";
import { Link } from "react-router-dom";
import Checkout from "../Shop/Checkout";
class Navbar extends Component {
  render() {
    return (
      <Box>
        <HStack spacing="24px">
          <Link  to="/shop">
            Shop
          </Link>
          <Link to="/contact">
            Contact
          </Link>
          <Checkout/>
        </HStack>
      </Box>
    );
  }
}

export default Navbar;
