import csv
import numpy as np
import serial

PORT = "" #COM_
ser = serial.Serial(PORT, 9600, timeout=None)
