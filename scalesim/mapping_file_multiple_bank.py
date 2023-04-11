# Memory Map for ScaleSim with 2 Banks
# Bank 0: 10000000 15000000
# Bank 1: 15000000 20000000
bank 0
{
    address-range 10000000 15000000;
    file /path/to/bank0.bin;
}

bank 1
{
    address-range 15000000 20000000;
    file /path/to/bank1.bin;
}

import random

num_banks = 4
bank_size = 1024
total_size = num_banks * bank_size

with open('memory_map.txt', 'w') as f:
    for i in range(num_banks):
        base_addr = i * bank_size
        f.write(f'Bank {i}:\n')
        for j in range(bank_size):
            addr = base_addr + j
          
        
