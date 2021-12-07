# -*- coding: utf-8 -*-
"""
In this file your task is to write the solver function!
"""
import math

INF = 100000

ANGLE_SETS = {
    "NVB": (-INF, -40, -25),
    "NB": (-40, -25, -10),
    "N": (-20, -10, 0),
    "ZO": (-5, 0, 5),
    "P": (0, 10, 20),
    "PB": (10, 25, 40),
    "PVB": (25, 40, INF)
}

ANGULAR_SPEED_SETS = {
    "NB": (-INF, -8, -3),
    "N": (-6, -3, 0),
    "ZO": (-1, 0, 1),
    "P": (0, 3, 6),
    "PB": (3, 8, INF)
}

TRACTION_FORCE_SETS = {
    "NVVB": (-INF, -32, -24),
    "NVB": (-32, -24, -16),
    "NB": (-24, -16, -8),
    "N": (-16, -8, 0),
    "Z": (-8, 0, 8),
    "P": (0, 8, 16),
    "PB": (8, 16, 24),
    "PVB": (16, 24, 32),
    "PVVB": (24, 32, INF)
}

RULE_TABLE = {
    ("PVB", "PB"): "PVVB",
    ("PVB", "P"): "PVVB",
    ("PVB", "ZO"): "PVB",
    ("PVB", "N"): "PB",
    ("PVB", "NB"): "P",

    ("PB", "PB"): "PVVB",
    ("PB", "P"): "PVB",
    ("PB", "ZO"): "PB",
    ("PB", "N"): "P",
    ("PB", "NB"): "Z",

    ("P", "PB"): "PVB",
    ("P", "P"): "PB",
    ("P", "ZO"): "P",
    ("P", "N"): "Z",
    ("P", "NB"): "N",

    ("ZO", "PB"): "PB",
    ("ZO", "P"): "P",
    ("ZO", "ZO"): "Z",
    ("ZO", "N"): "N",
    ("ZO", "NB"): "NB",

    ("N", "PB"): "P",
    ("N", "P"): "Z",
    ("N", "ZO"): "N",
    ("N", "N"): "NB",
    ("N", "NB"): "NVB",

    ("NB", "PB"): "Z",
    ("NB", "P"): "N",
    ("NB", "ZO"): "NB",
    ("NB", "N"): "NVB",
    ("NB", "NB"): "NVVB",

    ("NVB", "PB"): "N",
    ("NVB", "P"): "NB",
    ("NVB", "ZO"): "NVB",
    ("NVB", "N"): "NVVB",
    ("NVB", "NB"): "NVVB",
}

def solver(t,w):
    """
    Parameters
    ----------
    t : TYPE: float
        DESCRIPTION: the angle theta
    w : TYPE: float
        DESCRIPTION: the angular speed omega

    Returns
    -------
    F : TYPE: float
        DESCRIPTION: the force that must be applied to the cart
    or
    
    None :if we have a division by zero

    """
    # pre-compute membership degrees for theta and omega
    tMemberships = computeMemberships(t, ANGLE_SETS)
    wMemberships = computeMemberships(w, ANGULAR_SPEED_SETS)

    # compute membership degrees of F
    fMemberships = {}
    for rule, consequence in RULE_TABLE.items():
        tSet, wSet = rule
        tMembershipDegree = tMemberships[tSet]
        wMembershipDegree = wMemberships[wSet]
        fMembershipDegree = min(tMembershipDegree, wMembershipDegree)

        if consequence not in fMemberships or fMemberships[consequence] < fMembershipDegree:
            fMemberships[consequence] = fMembershipDegree

    # compute weighted average
    numerator = 0
    denominator = 0
    for set, degree in fMemberships.items():
        _, f, _ = TRACTION_FORCE_SETS[set]
        numerator += degree * f
        denominator += degree
    if denominator == 0:
        return None

    return numerator / denominator

def computeMemberships(x, setMap):
    # Compute the set that x belongs to and the corresponding membership degree
    memberships = {}
    for set, triangle in setMap.items():
        a, b, c = triangle
        degree = triangularMembershipFunction(x, a, b, c)

        memberships[set] = degree

    return memberships


def triangularMembershipFunction(x, a, b, c):
    return max(0, min((x - a) / (b - a), 1, (c - x) / (c - b)))
