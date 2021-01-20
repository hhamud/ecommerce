/* eslint-disable no-undef */
import React, { Component } from "react";
import { AtSignIcon, LockIcon } from "@chakra-ui/icons";
// eslint-disable-next-line no-unused-vars
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
  FormControl,
  FormLabel,
} from "@chakra-ui/react";
import axiosInstance from "./AxiosApi";
import { Link } from 'react-router-dom'


class SignUp extends Component {
  constructor(props) {
    super(props);
    this.state = {
      show: false,
      email: "",
      password: "",
    };
  }

  handleSubmit = async (event) => {
    event.preventDefault();
    try {
      const response = await axiosInstance.post("/user/create/", {
        email: this.state.email,
        password: this.state.password,
      });

      //check first if response has what you need => then do your stuff

      axiosInstance.defaults.headers["Authorization"] =
        "JWT " + response.data.access;
      localStorage.setItem("access_token", response.data.access);
      localStorage.setItem("refresh_token", response.data.refresh);

      return data;
    } catch (error) {
      console.log(this.state.email, this.state.password);

      throw error;
    }
  };

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
          h="300px"
          boxShadow="lg"
          justify="center"
          rounded="lg"
          align="stretch"
          padding={4}
          spacing={3}
          as={"form"}
          onSubmit={this.handleSubmit}
        >
          <Box>
            <FormControl id="Email Address" isRequired>
              <FormLabel>Email Address</FormLabel>
              <InputGroup>
                <InputLeftAddon
                  pointerEvents="none"
                  children={<AtSignIcon color="gray.300" />}
                />
                <Input
                  type="email"
                  borderLeftRadius="0"
                  placeholder="Email Address"
                  value={this.state.email}
                  onChange={(e) => this.setState({ email: e.target.value })}
                />
              </InputGroup>
            </FormControl>
          </Box>
          <Box>
            <FormControl id="Password" isRequired>
              <FormLabel>Password</FormLabel>
              <InputGroup size="md">
                <InputLeftAddon
                  pointerEvents="none"
                  children={<LockIcon color="gray.300" />}
                />
                <Input
                  pr="4.5rem"
                  type={this.state.show ? "text" : "password"}
                  placeholder="Enter password"
                  value={this.state.password}
                  onChange={(e) => this.setState({ password: e.target.value })}
                />
                <InputRightElement width="4.5rem">
                  <Button
                    h="1.75rem"
                    size="sm"
                    onClick={() =>
                      this.setState((PrevState) => ({
                        show: !PrevState.show,
                      }))
                    }
                  >
                    {this.state.show ? "Hide" : "Show"}
                  </Button>
                </InputRightElement>
              </InputGroup>
            </FormControl>
          </Box>
          <Flex align="center">
            <Link to="/">Forgot Password?</Link>
            <Spacer />
            <Button
              type="submit"
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

export default SignUp;
