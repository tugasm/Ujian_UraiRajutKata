class uraiRajutKata:

    # def urai(self, a):
    #     y = []
    #     z = 0
    #     for i in range(len(a)):
    #         if i == 0:
    #             y.append(a[i])
    #         else:
    #             for j in range(z+1):
    #                 s = a[j]
    #                 y.append(s)
    #         z = z + 1
    #     a = 0
    #     for a in y:
    #         x = print(a, end='')
    #     return x

    def rajut(self, a):
        star = list(a)
        x = 0
        y = 0
        for i in range(0, int(len(star)/2)):
            for j in range(0, i+1):
                x += 1
            a = print(star[x-1], end='')
            y += 1
            if(x == len(star)):
                break
        return a


x = uraiRajutKata()
# print(x.urai('Code'))
# print(x.urai('Python'))
# print(x.urai('Purwadhika'))

print(x.rajut('CCoCodCode'))
print(x.rajut('PPyPytPythPythoPython'))
print(x.rajut('PPuPurPurwPurwaPurwadPurwadhPurwadhiPurwadhikPurwadhika'))
