# -*- coding: utf-8 -*-
import vrep  # V-rep library
import sys
import time
import math


# This function will convert an angle to the equivalent rotation in the range [-pi,pi]
def ConfineAngle(angle):
    angle = angle % (2.0 * math.pi)
    if (angle < -math.pi):
        angle += (2.0 * math.pi)
    if (angle > math.pi):
        angle -= (2.0 * math.pi)
    return angle


def CalcIK():
    id = linkNum - 1
    while id >= 0:
        retcode, J_pos = vrep.simxGetObjectPosition(clientID, joint_handle[id], -1, vrep.simx_opmode_oneshot_wait)
        retcode, tip = vrep.simxGetObjectPosition(clientID, tip_handle, -1, vrep.simx_opmode_oneshot_wait)

        # Get the vector from the current bone to the end effector position.
        curToEndX = tip[0] - J_pos[0]
        curToEndY = tip[1] - J_pos[1]
        curToEndMag = math.sqrt(curToEndX * curToEndX + curToEndY * curToEndY)

        # Get the vector from the current bone to the target position.
        curToTargetX = target[0] - J_pos[0];
        curToTargetY = target[1] - J_pos[1];
        curToTargetMag = math.sqrt(curToTargetX * curToTargetX + curToTargetY * curToTargetY)

        # Get rotation
        endTargetMag = curToEndMag * curToTargetMag
        if endTargetMag <= 0.0001:  # prevent division by small numbers
            cosRotAng = 1
            sinRotAng = 0
        else:
            cosRotAng = (curToEndX * curToTargetX + curToEndY * curToTargetY) / endTargetMag
            sinRotAng = (curToEndX * curToTargetY - curToEndY * curToTargetX) / endTargetMag

        # Clamp the cosine into range when computing the angle(might be out of rangedue to floating point error)
        rotAng = math.acos(max(-1, min(1, cosRotAng)))
        if sinRotAng < 0.0:
            rotAng = -rotAng

        q[id] = q[id] + rotAng

        # Rotate the current link
        if (id == 0):
            vrep.simxSetJointPosition(clientID, joint_handle[id], ConfineAngle(q[id]) + math.pi / 2,
                                      vrep.simx_opmode_oneshot)
        else:
            vrep.simxSetJointPosition(clientID, joint_handle[id], ConfineAngle(q[id]), vrep.simx_opmode_oneshot)

        # Check for termination
        retcode, tip = vrep.simxGetObjectPosition(clientID, tip_handle, -1, vrep.simx_opmode_oneshot_wait)
        endToTargetX = (target[0] - tip[0])
        endToTargetY = (target[1] - tip[1])
        error = math.sqrt(endToTargetX * endToTargetX + endToTargetY * endToTargetY)
        if (error <= stol):
            # We found a valid solution.
            return 1, error
        id = id - 1

    return 0, error  # cannot get to the target in this iteration


if __name__ == "__main__":
    # Starts a communication thread with the server
    clientID = vrep.simxStart('127.0.0.1', 20001, True, True, 5000, 5)

    # clientID: the client ID, or -1 if the connection to the server was not possible
    if clientID != -1:  # check if client connection successful
        print
        'Connected to remote API server'
    else:
        print
        'Connection not successful'
        sys.exit('Could not connect')  # Exit from Python

    # Retrieves an object handle based on its name.
    errorCode, tip_handle = vrep.simxGetObjectHandle(clientID, 'tip', vrep.simx_opmode_oneshot_wait)
    errorCode, target_handle = vrep.simxGetObjectHandle(clientID, 'target', vrep.simx_opmode_oneshot_wait)
    errorCode, consoleHandle = vrep.simxAuxiliaryConsoleOpen(clientID, 'info', 4, 1 + 4, None, None, None, None,
                                                             vrep.simx_opmode_oneshot_wait)
    joint_handle = [-1, -1, -1]  # store the joint handles
    for i in range(3):
        errorCode, joint_handle[i] = vrep.simxGetObjectHandle(clientID, 'j' + str(i + 1), vrep.simx_opmode_oneshot_wait)

    ilimit = 100  # maximum iteration
    stol = 1e-2  # tolerance
    q = [0, 0, 0]  # initial joint value
    linkNum = 3  # number of links

    retcode, target = vrep.simxGetObjectPosition(clientID, target_handle, -1, vrep.simx_opmode_oneshot_wait)
    retcode, tip = vrep.simxGetObjectPosition(clientID, tip_handle, -1, vrep.simx_opmode_oneshot_wait)

    count = 0
    isOK = 0
    while (not isOK):
        isOK, err = CalcIK()

        vrep.simxAuxiliaryConsolePrint(clientID, consoleHandle, None, vrep.simx_opmode_oneshot_wait)
        count = count + 1
        vrep.simxAuxiliaryConsolePrint(clientID, consoleHandle, str(count) + ' iterations err:' + str(err),
                                       vrep.simx_opmode_oneshot_wait)

        if count > ilimit:
            vrep.simxAuxiliaryConsolePrint(clientID, consoleHandle, "Solution wouldn't converge\r\n",
                                           vrep.simx_opmode_oneshot_wait)
            break
            # time.sleep(0.1)

    # Ends the communication thread. This should be the very last remote API function called on the client side
    vrep.simxFinish(clientID)
