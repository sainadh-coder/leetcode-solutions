class Solution:
    def toHex(self, num: int) -> str:
        if num==0:
            return "0"
        if num >0:
            return hex(num)[2:]
        if num<0:
            hex_value = hex(num & 0xFFFFFFFF)[2:]
            return hex_value
        