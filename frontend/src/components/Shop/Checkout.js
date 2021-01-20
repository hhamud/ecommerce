/* eslint-disable no-unused-vars */
import React from "react";

import {
  Drawer,
  DrawerBody,
  DrawerFooter,
  DrawerHeader,
  DrawerOverlay,
  DrawerContent,
  DrawerCloseButton,
  Button,
  useDisclosure,
  Box,
  FormLabel,
  Stack,
  InputGroup,
  InputLeftAddon,
  Textarea,
  Select,
  InputRightAddon,
  Input,
  Text
} from "@chakra-ui/react";

import { AddIcon } from "@chakra-ui/icons";

function Checkout(props) {
  const { isOpen, onOpen, onClose } = useDisclosure();
  const firstField = React.useRef();
  

  return (
    <>
      <Button leftIcon={<AddIcon />} color="black" onClick={onOpen}>
        Bag
      </Button>
      <Drawer
        isOpen={isOpen}
        placement="right"
        initialFocusRef={firstField}
        onClose={onClose}
      >
        <DrawerOverlay>
          <DrawerContent>
            <DrawerCloseButton />
            <DrawerHeader paddingLeft="30px" borderBottomWidth="1px">
              Checkout bag
            </DrawerHeader>

            <DrawerBody>
              <Stack spacing="24px">

                <Box>
                  
                </Box>
              </Stack>
            </DrawerBody>

            <DrawerFooter borderTopWidth="1px">
              <Button variant="outline" mr={3}>
                Clear Cart
              </Button>
              <Button colorScheme="blue">Submit</Button>
            </DrawerFooter>
          </DrawerContent>
        </DrawerOverlay>
      </Drawer>
    </>
  );
}

export default Checkout;
