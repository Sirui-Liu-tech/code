'''
刘思瑞 2100017810
'''
def transfer(day, month, year):
    y = int(year)
    d = int(day[:-1])
    m = Haab_month.index(month)
    y_t = (y * 365 + m * 20 + d )//260
    rest = (y * 365 + m * 20 + d )%260
    d_t = rest % 20
    n_t = rest % 13 + 1
    return Tzolian_day[d_t] , n_t , y_t

Haab_month = ['pop', 'no', 'zip', 'zotz', 'tzec', 'xul', 'yoxkin', 'mol', 'chen', 'yax', 'zac', 'ceh', 'mac', 'kankin', 'muan', 'pax', 'koyab', 'cumhu', 'uayet' ]
Tzolian_day = ['imix', 'ik', 'akbal', 'kan', 'chicchan', 'cimi', 'manik', 'lamat', 'muluk', 'ok', 'chuen', 'eb', 'ben', 'ix', 'mem', 'cib', 'caban', 'eznab', 'canac', 'ahau']
n = int(input())
print(n)
for i in range(n):
    day , month , year = input().split()
    day_t , num_t , year_t = transfer(day , month , year)
    print(num_t,day_t,year_t)

