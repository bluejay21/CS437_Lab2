import picar_4wd as fc
import time


class wheelController:
    #
    # Define the forward functions
    #

    def forward(self, seconds, powerLevel):
        # return type void
        # This function will have picar move in the forward direction
        # for the requested amount of time and power level input by the user.
        try:
            fc.backward(powerLevel) # The motors are on backwards currently, so fc.backwards is forwards.
            time.sleep(seconds)
        finally:
            fc.stop()

    # def forward(self, powerLevel):
    #     # return type void
    #     # This function will have picar move in the forward direction indefinitely
    #     # for the requested power level input by the user.

    #     fc.backward(powerLevel) # The motors are on backwards currently, so fc.backwards is forwards.



    #
    # Define the backward functions
    #

    def backward(self, seconds, powerLevel):
        # return type void
        # This function will have picar move in the backward direction
        # for the requested amount of time and power level input by the user.
        try:
            fc.forward(powerLevel) # The motors are on backwards currently, so fc.forwards is backwards.
            time.sleep(seconds)
        finally:
            fc.stop()

    # def backward(self, powerLevel):
    #     # return type void
    #     # This function will have picar move in the backward direction indefinitely
    #     # for the requested power level input by the user.
    #     fc.forward(powerLevel) # The motors are on backwards currently, so fc.forwards is backwards.


    #
    # Define the turn functions
    #

    def turn_left(self, seconds, powerLevel):
            try:
                fc.turn_right(powerLevel)
                time.sleep(seconds)
            finally:
                fc.stop()


    def turn_right(self, seconds, powerLevel):
        try:
            fc.turn_left(powerLevel)
            time.sleep(seconds)
        finally:
            fc.stop()


    def stop(self):
        fc.stop();



    def PiTemp(self):
        return fc.cpu_temperature()


if __name__ == "__main__":
    wheel_C = wheelController()
    try:
        wheel_C.forward(1, 10)
    finally:
        wheel_C.stop
