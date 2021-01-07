import React, { Component } from "react";
import { HStack} from "@chakra-ui/react";
import { Link } from 'react-router-dom'


class CreateAccount extends Component {
  render() {
    return (
      <HStack  bg='white' justify={'flex-end'} spacing={3}>
        <Link  color="white" to="/login">
            Login
          </Link>
          <Link  color="white" to="/signup">
            Sign Up
          </Link>
      </HStack>
    );
  }
}

export default CreateAccount;
