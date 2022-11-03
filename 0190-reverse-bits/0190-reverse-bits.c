uint32_t reverseBits(uint32_t n) {
    
    /*
    uint32_t res = 0;
    
    for(int i = 0; i < 32; i++)
    {
        
        res |= (n & 1) << (31-i);
        n >>= 1;
    }
        
    return res;
    */
    
    
    n = (n << 16) | (n >> 16);
    n = ((n & 0x00FF00FF) << 8) | ((n & 0xFF00FF00) >> 8);
    n = ((n & 0x0F0F0F0F) << 4) | ((n & 0xF0F0F0F0) >> 4);
    n = ((n & 0x33333333) << 2) | ((n & 0xCCCCCCCC) >> 2);
    n = ((n & 0x55555555) << 1) | ((n & 0xAAAAAAAA) >> 1);
    
    return n;
    
}