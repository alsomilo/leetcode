uint32_t reverseBits(uint32_t n) {
    
    uint32_t res = 0, msb = 0x80000000, lsb = 0x00000001;
    int shiftCount = 0;
    
    for(int i = 0; i < 16; i++)
    {
        shiftCount = (31 - (i << 1));
        res |= ((n & msb) >> shiftCount) | ((n & lsb) << shiftCount);
        msb >>= 1;
        lsb <<= 1;
    }
    
    return res;
}