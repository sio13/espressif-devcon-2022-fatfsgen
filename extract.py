import sys, os  
sys.path.append(os.path.join(os.environ["IDF_PATH"], "components", "partition_table"))  
from parttool import ParttoolTarget, PartitionName

target = ParttoolTarget("/dev/cu.usbserial-1410")
target.read_partition(PartitionName("storage"), "fatfs.img")
