import React, { Component } from "react";
import { Box } from "@chakra-ui/react";
import mainimage from "../../assets/pexels-ali-pazani-2829367.jpg";

class Main extends Component {
  render() {
    return (
      <Box
        backgroundImage={`url(${mainimage})`}
        h="500px"
        bgAttachment="fixed"
        bgPos="fixed"
        bgRepeat="no-repeat"
        bgSize="cover"
      ></Box>
    );
  }
}

export default Main;
