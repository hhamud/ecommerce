import React, { Component } from "react";
import { Box } from "@chakra-ui/react";
import mainimage from "../../assets/pexels-ali-pazani-2829367.jpg";

class Main extends Component {
  render() {
    return (
      <Box
        backgroundImage={`url(${mainimage})`}
        h="100vh"
        w="100vw"
        bgAttachment="fixed"
        bgPos="center"
        bgRepeat="no-repeat"
        bgSize="cover"
        zIndex={-1}
      ></Box>
    );
  }
}

export default Main;
