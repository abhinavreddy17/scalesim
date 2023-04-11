# Memory Map for ScaleSim with 2 Banks
# Bank 0: 0x00000000 - 0x7FFFFFFF
# Bank 1: 0x80000000 - 0xFFFFFFFF

bank 0
{
    address-range 0x00000000 0x7FFFFFFF;
    file /path/to/bank0.bin;
}

bank 1
{
    address-range 0x80000000 0xFFFFFFFF;
    file /path/to/bank1.bin;
}
