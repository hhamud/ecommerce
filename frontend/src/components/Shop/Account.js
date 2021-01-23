import React, { Component } from "react";
// eslint-disable-next-line no-unused-vars
import {
  Box,
  Input,
  InputGroup,
  Button,
  FormControl,
  FormLabel,
  SimpleGrid,
} from "@chakra-ui/react";
import axiosInstance from "../Auth/AxiosApi";

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

  AllowAccess = async () => {
    try {
      let id = this.props.location.state.user_id;
      let response = await axiosInstance.get(`/account/${id}/details/`);
      const message = response.data;
      this.setState({
        first_name: message.first_name,
        last_name: message.last_name,
        phone_number: message.phone_number,
        home_number: message.home_number,
        street: message.street,
        area: message.area,
        city: message.city,
        post_code: message.post_code,
        country: message.country,
        address_type: message.address_type,
        default_address: message.default_address,
      });
      return message;
    } catch (error) {
      console.log("Error: ", JSON.stringify(error, null, 4));
      throw error;
    }
  };

  componentDidMount() {
    this.AllowAccess();
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
        <SimpleGrid
          columns={{ sm: 1, md: 2, lg: 3 }}
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
                  placeholder={this.state.first_name}
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
                  placeholder={this.state.last_name}
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
                  placeholder={this.state.phone_number}
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
                  placeholder={this.state.home_number}
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
                  placeholder={this.state.street}
                  type="text"
                  borderLeftRadius="0"
                  value={this.state.street}
                  onChange={(e) => this.setState({ street: e.target.value })}
                />
              </InputGroup>
            </FormControl>
          </Box>
          <Box>
            <FormControl id="area" isRequired>
              <FormLabel>Area</FormLabel>
              <InputGroup>
                <Input
                  placeholder={this.state.area}
                  type="text"
                  borderLeftRadius="0"
                  value={this.state.area}
                  onChange={(e) => this.setState({ area: e.target.value })}
                />
              </InputGroup>
            </FormControl>
          </Box>
          <Box>
            <FormControl id="city" isRequired>
              <FormLabel>City</FormLabel>
              <InputGroup>
                <Input
                  placeholder={this.state.city}
                  type="text"
                  borderLeftRadius="0"
                  value={this.state.city}
                  onChange={(e) => this.setState({ city: e.target.value })}
                />
              </InputGroup>
            </FormControl>
          </Box>
          <Box>
            <FormControl id="country" isRequired>
              <FormLabel>Country</FormLabel>
              <InputGroup>
                <Input
                  placeholder={this.state.country}
                  type="text"
                  borderLeftRadius="0"
                  value={this.state.country}
                  onChange={(e) => this.setState({ country: e.target.value })}
                />
              </InputGroup>
            </FormControl>
          </Box>
          <Box>
            <FormControl id="post_code" isRequired>
              <FormLabel>Post Code</FormLabel>
              <InputGroup>
                <Input
                  placeholder={this.state.post_code}
                  type="text"
                  borderLeftRadius="0"
                  value={this.state.post_code}
                  onChange={(e) => this.setState({ post_code: e.target.value })}
                />
              </InputGroup>
            </FormControl>
          </Box>
          <Button
            type="submit"
            loadingText="Logging in"
            colorScheme="teal"
            variant="outline"
            maxW="100px"
          >
            Submit
          </Button>
        </SimpleGrid>
      </Box>
    );
  }
}

export default Account;
