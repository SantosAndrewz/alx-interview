#!/usr/bin/python3
"""
- Module for a method that determines if a given data-set represents a valid
UTF-8 encoding.
Returns: True if data is valid UTF-8 encoding, else return False.
"""


def validUTF8(data):
    """
    Method determines if a given data set represents a valid UTF-8 encoding.

    Parameters:
    data(List[int]): A list of integers where each integer is one byte of data

    Returns:
    bool: True if the data valid UTF-8 encoding, else return False.
    """
    num_bytes = 0

    start_bit_mask = 1 << 7
    cont_bit_mask = 1 << 6

    for byte in data:
        lead_one_mask = 1 << 7

        if num_bytes == 0:
            while lead_one_mask & byte:
                num_bytes += 1
                lead_one_mask >>= 1

            if num_bytes == 0:
                continue
            if num_bytes == 1 or num_bytes > 4:
                return False
        else:
            if not (byte & start_bit_mask and not (byte & cont_bit_mask)):
                return False
        num_bytes -= 1
    return num_bytes == 0
