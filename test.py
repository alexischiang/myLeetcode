class Solution:
    def intToRoman(self, num):
        mystr = ''
        a = num//1000
        mystr += ('M' * a)
        rem = num%1000
        while rem:
            if rem >= 100 and rem < 1000:
                if rem >= 900:
                    rem = rem%900
                    mystr += ('CM')
                elif rem >= 500 and rem < 900:
                    rem = rem%500
                    mystr += ('D')
                elif rem >= 400 and rem < 500:
                    rem = rem%400
                    mystr += ('CD')
                else:
                    rem = rem%100
                    mystr += ('C')
            elif rem >= 10 and rem < 100:
                if rem >= 90:
                    rem = rem%90
                    mystr += ('XC')
                elif rem >= 50 and rem < 90:
                    rem = rem%50
                    mystr += ('L')
                elif rem >= 40 and rem < 50:
                    rem = rem%40
                    mystr += ('XL')
                else:
                    rem = rem%10
                    mystr += ('X')
            elif rem > 0  and rem < 10:
                if rem >= 5:
                    rem = rem%5
                    mystr += ('V')
                elif rem == 4:
                    mystr += ('IV')
                    rem = 0
                else:
                    mystr += (rem * 'I')
                    rem = 0
        return mystr

if __name__ == "__main__":
    x = Solution()
    result = x.intToRoman(1994)
    print(result)