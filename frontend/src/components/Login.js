import React, { Component } from "react";
import { AtSignIcon, LockIcon } from "@chakra-ui/icons";
import {
  VStack,
  Flex,
  Spacer,
  Box,
  Input,
  InputGroup,
  Button,
  InputRightElement,
  InputLeftAddon,
} from "@chakra-ui/react";
import { Link } from 'react-router-dom'


class Login extends Component {
  constructor(props) {
    super(props);
    this.state = {
      show: false,
      email: '',
      password: '', 
    };
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
        <VStack
          w="400px"
          h="200px"
          boxShadow="lg"
          justify="center"
          rounded="lg"
          align="stretch"
          padding={4}
          spacing={3}
        >
          <Box>
            <InputGroup>
              <InputLeftAddon
                pointerEvents="none"
                children={<AtSignIcon color="gray.300" />}
              />
              <Input
                type="email"
                borderLeftRadius="0"
                placeholder="Email Address"
              />
            </InputGroup>
          </Box>
          <Box>
            <InputGroup size="md">
              <InputLeftAddon
                pointerEvents="none"
                children={<LockIcon color="gray.300" />}
              />
              <Input
                pr="4.5rem"
                type={this.state.show ? "text" : "password"}
                placeholder="Enter password"
              />
              <InputRightElement width="4.5rem">
                <Button
                  h="1.75rem"
                  size="sm"
                  onClick={() =>
                    this.setState((PrevState) => ({ show: !PrevState.show }))
                  }
                >
                  {this.state.show ? "Hide" : "Show"}
                </Button>
              </InputRightElement>
            </InputGroup>
          </Box>
          <Flex align='center'>
              <Link to='/'>Forgot Password?</Link>
              <Spacer/>
          <Button
          type='submit'
            loadingText="Logging in"
            colorScheme="teal"
            variant="outline"
          >
            Login
          </Button>
              </Flex>        
          
        </VStack>
      </Box>
    );
  }
}

export default Login;
