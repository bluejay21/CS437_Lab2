import wheelController

class CarController:

    wheel_c = wheelController.wheelController()
    totalDistance = 0
    headingAngle = 0
    turnConstant = 10/3
    driveConstant = 1

    # Define the potential commands that could be recieved from the Client
    # Dictionary used for readability throughout code
    # commandTypes = {
    #     "FORWARD" : 0,
    #     "BACKWARD" : 1,
    #     "TURNLEFT" : 2,
    #     "TURNRIGHT" : 3,
    #     "NONE" : 4
    # }

    def handleCommand(self, commandStr):
        sec = 0.1
        powLevel = 15

        # print(commandStr)
        cmdStr = commandStr.decode()
        # print(cmdStr)

        returnStr = "COMMAND_NOT_SUPPORTED"
        if(cmdStr == "87"):
            returnStr = "DRIVING_FORWARD"
            # print("HERE1")
            self.wheel_c.forward(sec, powLevel)
            # print("HERE2")
            self.totalDistance = self.totalDistance + self.driveConstant
        elif (cmdStr == "83"):
            returnStr = "DRIVING_BACKWARD"
            self.wheel_c.backward(sec, powLevel)
            self.totalDistance = self.totalDistance - self.driveConstant
        elif (cmdStr == "68"):
            returnStr = "TURNING_RIGHT"
            self.wheel_c.turn_right(sec, powLevel)
            self.headingAngle = self.headingAngle - self.turnConstant
        elif (cmdStr == "65"):
            returnStr = "TURNING_LEFT"
            self.wheel_c.turn_left(sec, powLevel)
            self.headingAngle = self.headingAngle + self.turnConstant
        elif (cmdStr == "INFO"):
            print("INFO")
            returnStr = self.getCarInfo()


        # print(returnStr)

        return returnStr


    def printHello(self):
        print("HELLO!")


    def getCarInfo(self):
        infoStr = str(self.headingAngle) + "," + str(self.totalDistance) + "," + str(self.wheel_c.PiTemp())
        return infoStr
            