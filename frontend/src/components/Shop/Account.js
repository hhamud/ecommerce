import React, { Component } from "react";
import { AtSignIcon, LockIcon } from "@chakra-ui/icons";
// eslint-disable-next-line no-unused-vars
import {
  Stack,
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

import AllowAccess from "../Auth/AllowAccess";

class Account extends Component {
  constructor(props) {
    super(props);
    const AT = {
      SHIPPING_ADDRESS: "shipping_address",
      BILLING_ADDRESS: "billing_address",
    };
    this.state = {
      first_name: "",
      last_name: "",
      phone_number: "",
      home_number: "",
      street: "",
      area: "",
      city: "",
      post_code: "",
      country: "",
      address_type: AT,
      default_address: false,
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
        <Stack
          direction={["row", "column"]}
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
            <FormControl id="First Name" isRequired>
              <FormLabel>First Name</FormLabel>
              <InputGroup>
                <Input
                  type="text"
                  borderLeftRadius="0"
                  value={this.state.first_name}
                  onChange={(e) =>
                    this.setState({ first_name: e.target.value })
                  }
                />
              </InputGroup>
            </FormControl>
          </Box>
          <Box>
            <FormControl id="Last Name" isRequired>
              <FormLabel>Last Name</FormLabel>
              <InputGroup>
                <Input
                  type="text"
                  borderLeftRadius="0"
                  value={this.state.last_name}
                  onChange={(e) => this.setState({ last_name: e.target.value })}
                />
              </InputGroup>
            </FormControl>
          </Box>
          <Box>
            <FormControl id="phone number" isRequired>
              <FormLabel>Phone Number</FormLabel>
              <InputGroup>
                <Input
                  type="phonenumber"
                  borderLeftRadius="0"
                  value={this.state.phone_number}
                  onChange={(e) =>
                    this.setState({ phone_number: e.target.value })
                  }
                />
              </InputGroup>
            </FormControl>
          </Box>
          <Box>
            <FormControl id="home_number" isRequired>
              <FormLabel>House Number</FormLabel>
              <InputGroup>
                <Input
                  type="number"
                  borderLeftRadius="0"
                  value={this.state.home_number}
                  onChange={(e) =>
                    this.setState({ home_number: e.target.value })
                  }
                />
              </InputGroup>
            </FormControl>
          </Box>
          <Box>
            <FormControl id="street" isRequired>
              <FormLabel>Street</FormLabel>
              <InputGroup>
                <Input
                  type="text"
                  borderLeftRadius="0"
                  value={this.state.street}
                  onChange={(e) =>
                    this.setState({ street: e.target.value })
                  }
                />
              </InputGroup>
            </FormControl>
          </Box>
          <Box>
            <FormControl id="area" isRequired>
              <FormLabel>Area</FormLabel>
              <InputGroup>
                <Input
                  type="text"
                  borderLeftRadius="0"
                  value={this.state.area}
                  onChange={(e) =>
                    this.setState({ area: e.target.value })
                  }
                />
              </InputGroup>
            </FormControl>
          </Box>
          <Box>
            <FormControl id="city" isRequired>
              <FormLabel>City</FormLabel>
              <InputGroup>
                <Input
                  type="text"
                  borderLeftRadius="0"
                  value={this.state.city}
                  onChange={(e) =>
                    this.setState({ city: e.target.value })
                  }
                />
              </InputGroup>
            </FormControl>
          </Box>
          <Box>
            <FormControl id="country" isRequired>
              <FormLabel>Country</FormLabel>
              <InputGroup>
                <Input
                  type="text"
                  borderLeftRadius="0"
                  value={this.state.country}
                  onChange={(e) =>
                    this.setState({ country: e.target.value })
                  }
                />
              </InputGroup>
            </FormControl>
          </Box>
          <Box>
            <FormControl id="post_code" isRequired>
              <FormLabel>Post Code</FormLabel>
              <InputGroup>
                <Input
                  type="text"
                  borderLeftRadius="0"
                  value={this.state.post_code}
                  onChange={(e) =>
                    this.setState({ post_code: e.target.value })
                  }
                />
              </InputGroup>
            </FormControl>
          </Box>
        </Stack>
      </Box>
    );
  }
}

export default Account;
