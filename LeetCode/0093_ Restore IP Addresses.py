'''
Given a string s containing only digits,
return all possible valid IP addresses that can be obtained from s.
You can return them in any order.

A valid IP address consists of exactly four integers,
each integer is between 0 and 255,
separated by single dots and cannot have leading zeros.
For example, "0.1.2.201" and "192.168.1.1" are valid IP addresses and "0.011.255.245", "192.168.1.312" and "192.168@1.1" are invalid IP addresses.
'''


class Solution:
    def restoreIpAddresses(self,s: str):
        # backtracking solution
        result = []

        def generator(full_ip, index):
            # full_ip : To hold the complete IP before it is included in the result
            # index : To obtain the position of the string (s)
            if len(full_ip) == 4:
                if index == len(s): # All string(s) must be used
                    result.append('.'.join(full_ip))
                return

            for i in range(3):
                if not (index+i < len(s)): # out of range
                    return
                else:
                    part = s[index:index+i+1]
                    if 0 <= int(part) <= 255 and len(part) == len(str(int(part))): # Check the range and prevent the number 0 from continuing
                        full_ip.append(part)
                        generator(full_ip,index+i+1)
                        full_ip.pop()

        generator([],0)

        return result