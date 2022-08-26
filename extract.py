import sys
import os
idf_path = os.environ["IDF_PATH"]  # get value of IDF_PATH from environment
parttool_dir = os.path.join(idf_path, "components", "partition_table")  # parttool.py lives in $IDF_PATH/components/partition_table
sys.path.append(parttool_dir)  # this enables Python to find parttool module
from parttool import *  # import all names inside parttool module

# Create a partool.py target device connected on serial port /dev/ttyUSB1
target = ParttoolTarget("/dev/cu.usbserial-1410")
target.read_partition(PartitionName("storage"), "fatfs.img")
