#!/usr/bin/python3
"""
Module for determining if all the boxes can be opened.
"""


def canUnlockAll(boxes):
    """
    Determines if all the boxes can be unlocked with the given keys.

    Param:
    boxes (list of lists): Each indhas a list of keys for the boxes.

    Returns:
    bool: True if all boxes can be opened , otherwise false.
    """

    x = len(boxes)
    open_boxes = [False] * x
    open_boxes[0] = True

    keys = [0]

    while keys:
        c = keys.pop()
        for key in boxes[c]:
            if key < x and not open_boxes[key]:
                open_boxes[key] = True
                keys.append(key)
    return all(open_boxes)
