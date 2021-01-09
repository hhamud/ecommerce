import React, { Component } from "react";
import { AtSignIcon, LockIcon } from "@chakra-ui/icons";
import { Formik, Form, Field, ErrorMessage } from "formik";
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
import { Link } from "react-router-dom";
import axios from "axios";

class Login extends Component {
  constructor(props) {
    super(props);
    this.state = {
      show: false,
      email: "",
      pass: "",
    };
  }

  handleSubmit = (event) => {
    let base_url = process.env.REACT_APP_API_ENDPOINT;
    event.preventDefault();
    const user = JSON.stringify({
      email: this.state.email,
      pass: this.state.pass,
    });
    axios.post(`${base_url}/token/login/`, {user }).then((res) => {
      console.log(res);
      console.log(res.data);
    //   window.location = `${base_url}token/login/` ; //This line of code will redirect you once the submission is succeed
    });
  };
 

  render() {
    return (
      <Formik
        initialValues={{
          email: "",
          pass: "",
        }}
      >
        <Form onSubmit = { this.handleSubmit }>
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
        </Form>
      </Formik>
    );
  }
}

export default Login;
