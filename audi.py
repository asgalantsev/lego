from pybricks.pupdevices import Motor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.tools import wait, StopWatch

A_MOTOR_SPEED = 2000
B_MOTOR_SPEED = 2000
D_MOTOR_SPEED = 1500

# Initialize the motors.
a_motor = Motor(Port.A)
b_motor = Motor(Port.B)
d_motor = Motor(Port.D)

a_motor.control.limits(2000, 2000, 400)
b_motor.control.limits(2000, 2000, 400)


# Make wheels staight
# Seems like my engine for turns is not calibrated
# That's why wheels are straight with 100 degrees
d_motor.run_target(1000, 100)
wait(3000)


while True:

    a_motor.run(A_MOTOR_SPEED)
    b_motor.run(B_MOTOR_SPEED)

    wait(1000)

    if(a_motor.speed() < 200):
        a_motor.stop()
        b_motor.stop()

        wait(1000)

        a_motor.run(-A_MOTOR_SPEED)
        b_motor.run(-B_MOTOR_SPEED)
        wait(1500)
        a_motor.stop()
        b_motor.stop()

        d_motor.run_target(D_MOTOR_SPEED,0)
        wait(3000)

        a_motor.run(A_MOTOR_SPEED)
        b_motor.run(B_MOTOR_SPEED)
        wait(2000)
        a_motor.stop()
        b_motor.stop()

        d_motor.run_target(D_MOTOR_SPEED, 200)
        wait(3000)

        a_motor.run(A_MOTOR_SPEED)
        b_motor.run(B_MOTOR_SPEED)
        wait(2000)
        a_motor.stop()
        b_motor.stop()

        d_motor.run_target(D_MOTOR_SPEED, 100)
        wait(3000)