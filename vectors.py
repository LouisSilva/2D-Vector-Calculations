"""Vectors.py: Can add, subtract, multiply, scale, calculate the dot product and calculate the convex combination of 2D vectors"""

import math
from time import sleep


class Vector:

    # Take vector1, vector2 and p (a boolean which determines whether to print the output) as parameters
    @staticmethod
    def add(v1, v2, p):
        # create a new vector by adding the two vectors
        vN = [v1[0] + v2[0], v1[1] + v2[1]]

        # if p is true then print the output
        if p:
            print("Add: " + str(v1) + " to " + str(v2) + " = " + str(vN))

        # return the new vector
        return vN

    # same as the last function but subraction instead
    @staticmethod
    def subtract(v1, v2, p):
        vN = [v1[0] - v2[0], v1[1] - v2[1]]
        if p:
            print("Subtract: " + str(v1) + " from " + str(v2) + " = " + str(vN))
        return vN

    # same as the last function but multiplication instead
    @staticmethod
    def multiply(v1, v2, p):
        vN = [v1[0] * v2[0], v1[1] * v2[1]]
        if p:
            print("Multiply: " + str(v1) + " by " + str(v2) + " = " + str(vN))
        return vN

    # same as the last function but scaling instead
    @staticmethod
    def scale(v, scale_factor, p):
        vN = [v[0] * scale_factor, v[1] * scale_factor]
        if p:
            print("Scale " + str(v) + " by " + str(scale_factor) + " = " + str(vN))
        return vN

    # same as the last function but calculates the dot product instead
    @staticmethod
    def dotProduct(v1, v2, p):
        vN = [v1[0] * v2[0] + v1[1] * v2[1]]
        if p:
            print("Dot product of: " + str(v1) + " and " + str(v2) + " = " + str(vN))
        return vN

    # takes the same parameters as the other functions but calculates the convex combination
    @staticmethod
    def convexCombination(v1, v2, p):
        # for each vector raise it to the power of 2, add them and then square root the result to get the magnitude
        magnitudeV1A = [math.sqrt(pow(v1[0], 2) + pow(v1[1], 2))]
        magnitudeV2A = [math.sqrt(pow(v2[0], 2) + pow(v2[1], 2))]

        # convert the magnitude to a float
        magnitudeV1 = float(magnitudeV1A[0])
        magnitudeV2 = float(magnitudeV2A[0])

        # calculate the dot product of the two vectors and convert the result to a float
        dotProductA = Vector.dotProduct(v1, v2, False)
        dotProduct = float(dotProductA[0])

        # calculate angle and then convert it back to degrees
        cosineRadians = math.acos(dotProduct / (magnitudeV1 * magnitudeV2))
        cosineDegrees = math.degrees(cosineRadians)

        # if p is true then print the result
        if p:
            print("Convex Combination of " + str(v1) + " and " + str(v2) + " = " + str(cosineDegrees))

        # return the result
        return cosineDegrees


if __name__ == "__main__":
    # complete some tasks
    Vector().add([3, 2], [6, 8], True)
    Vector().subtract([3, 2], [6, 8], True)
    Vector().multiply([3, 2], [6, 8], True)
    Vector().scale([3, 2], 5, True)
    Vector().dotProduct([3, 2], [6, 8], True)
    Vector().convexCombination([3, 4], [4, 3], True)
