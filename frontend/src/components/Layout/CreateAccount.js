import React, { Component } from "react";
import { HStack, Text } from "@chakra-ui/react";

class CreateAccount extends Component {
  render() {
    return (
      <HStack  bg='black' justify={'flex-end'} spacing={3}>
        <Text color="white">Login</Text>
        <Text color="white">Sign up</Text>
      </HStack>
    );
  }
}

export default CreateAccount;
