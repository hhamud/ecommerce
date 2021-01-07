import React, { Component } from "react";
import Navbar from "./Navbar";
import CreateAccount from "./CreateAccount";
import { Flex, Box, Spacer, Text } from "@chakra-ui/react";

class Header extends Component {
  render() {
    return (
      <Box
        boxShadow="md"
        bg="whitesmoke"
        rounded="lg"
        position="fixed"
        display='block'
        width='100vw'
      >
        <Box>
          <CreateAccount />
        </Box>
        <Flex padding={4}>
          <Box>
            <Text>Logo</Text>
          </Box>
          <Spacer />
          <Box>
            <Navbar />
          </Box>
        </Flex>
      </Box>
    );
  }
}

export default Header;
