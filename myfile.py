from datetime import datetime, timedelta
from find_full_periods_in_range import find_full_days_in_period, find_full_weeks_in_period, find_full_month_in_period

start, end = datetime(2026, 7, 5), datetime(2027, 2, 3)
cur = start + timedelta(seconds=86399) + timedelta(days=5)
c = 7

while cur <= end:
    print(cur)
    cur += timedelta(days=7)
cur -= timedelta(days=7)

if cur < end:
    while cur <= end:
        cur += timedelta(days=1)
    print(cur)

"""
2003-07-06 23:59:59
2003-07-13 23:59:59
2003-07-20 23:59:59
2003-07-27 23:59:59
2003-08-03 23:59:59
"""

"""
             start              |              end               |                                                   
      01/07/2003 00:00:00       |      06/07/2003 23:59:59       | 2003/27                                           
      07/07/2003 00:00:00       |      13/07/2003 23:59:59       | 2003/28                                           
      14/07/2003 00:00:00       |      20/07/2003 23:59:59       | 2003/29                                           
      21/07/2003 00:00:00       |      27/07/2003 23:59:59       | 2003/30                                           
      28/07/2003 00:00:00       |      31/07/2003 23:59:59       | 2003/31
"""

"""
Total weeks: 32
             start              |              end               |                                                   
      05/07/2026 00:00:00       |      05/07/2026 23:59:59       | 2026/27                                           
      06/07/2026 00:00:00       |      12/07/2026 23:59:59       | 2026/28                                           
      13/07/2026 00:00:00       |      19/07/2026 23:59:59       | 2026/29                                           
      20/07/2026 00:00:00       |      26/07/2026 23:59:59       | 2026/30                                           
      27/07/2026 00:00:00       |      02/08/2026 23:59:59       | 2026/31                                           
      03/08/2026 00:00:00       |      09/08/2026 23:59:59       | 2026/32                                           
      10/08/2026 00:00:00       |      16/08/2026 23:59:59       | 2026/33                                           
      17/08/2026 00:00:00       |      23/08/2026 23:59:59       | 2026/34                                           
      24/08/2026 00:00:00       |      30/08/2026 23:59:59       | 2026/35                                           
      31/08/2026 00:00:00       |      06/09/2026 23:59:59       | 2026/36                                           
      07/09/2026 00:00:00       |      13/09/2026 23:59:59       | 2026/37                                           
      14/09/2026 00:00:00       |      20/09/2026 23:59:59       | 2026/38                                           
      21/09/2026 00:00:00       |      27/09/2026 23:59:59       | 2026/39                                           
      28/09/2026 00:00:00       |      04/10/2026 23:59:59       | 2026/40                                           
      05/10/2026 00:00:00       |      11/10/2026 23:59:59       | 2026/41                                           
      12/10/2026 00:00:00       |      18/10/2026 23:59:59       | 2026/42                                           
      19/10/2026 00:00:00       |      25/10/2026 23:59:59       | 2026/43                                           
      26/10/2026 00:00:00       |      01/11/2026 23:59:59       | 2026/44                                           
      02/11/2026 00:00:00       |      08/11/2026 23:59:59       | 2026/45                                           
      09/11/2026 00:00:00       |      15/11/2026 23:59:59       | 2026/46                                           
      16/11/2026 00:00:00       |      22/11/2026 23:59:59       | 2026/47                                           
      23/11/2026 00:00:00       |      29/11/2026 23:59:59       | 2026/48                                           
      30/11/2026 00:00:00       |      06/12/2026 23:59:59       | 2026/49                                           
      07/12/2026 00:00:00       |      13/12/2026 23:59:59       | 2026/50                                           
      14/12/2026 00:00:00       |      20/12/2026 23:59:59       | 2026/51                                           
      21/12/2026 00:00:00       |      27/12/2026 23:59:59       | 2026/52                                           
      28/12/2026 00:00:00       |      03/01/2027 23:59:59       | 2026/53                                           
      04/01/2027 00:00:00       |      10/01/2027 23:59:59       | 2027/1                                            
      11/01/2027 00:00:00       |      17/01/2027 23:59:59       | 2027/2                                            
      18/01/2027 00:00:00       |      24/01/2027 23:59:59       | 2027/3                                            
      25/01/2027 00:00:00       |      31/01/2027 23:59:59       | 2027/4                                            
      01/02/2027 00:00:00       |      03/02/2027 23:59:59       | 2027/5 
"""

def support_output_fun():
    """for i in find_full_weeks_in_period(datetime(2019, 10, 25), datetime(2019, 11, 14)):
            print(i)
        print("*"*100)
        for i in find_full_days_in_period(datetime(2019, 10, 25), datetime(2019, 10, 27)):
            print(i)

        print("*" * 100)
        for i in find_full_month_in_period(datetime(2019, 1, 25), datetime(2019, 1, 25)):
            print(i)"""

    """print(len(find_full_days_in_period(datetime(2018, 1, 1), datetime(2018, 12, 31))))
    print(len(find_full_month_in_period(datetime(2018, 1, 1), datetime(2018, 12, 31))))
    print(len(find_full_weeks_in_period(datetime(2018, 1, 1), datetime(2018, 2, 19))))

    print('*' * 200)
    for i in find_full_weeks_in_period(datetime(2018, 1, 1), datetime(2018, 12, 31)):
        print(i)

    print('*' * 200)
    for i in find_full_weeks_in_period(datetime(2018, 1, 1), datetime(2018, 4, 2)):
        print(i)"""

    print('*' * 200)
    result = find_full_days_in_period(datetime(2018, 12, 29), datetime(2019, 1, 4))
    print("Total days: {}".format(len(result)))
    print(type(result[0]))
    for i in result:
        print("start: {} | end: {} | {}".format(i[0].strftime("%d/%m/%Y %H:%M:%S"),
                                                i[1].strftime("%d/%m/%Y %H:%M:%S"),
                                                i[2]))

    print('*' * 200)
    result = find_full_weeks_in_period(datetime(2018, 12, 29), datetime(2019, 2, 4))
    print("Total weeks: {}".format(len(result)))
    print(type(result[0]))
    for i in result:
        print("start: {} | end: {} | {}".format(i[0].strftime("%d/%m/%Y %H:%M:%S"),
                                                i[1].strftime("%d/%m/%Y %H:%M:%S"),
                                                i[2]))

    print('*' * 200)
    result = find_full_month_in_period(datetime(2018, 12, 29), datetime(2019, 2, 4))
    print("Total month: {}".format(len(result)))
    print(type(result[0]))
    for i in result:
        print("start: {} | end: {} | {}".format(i[0].strftime("%d/%m/%Y %H:%M:%S"),
                                                i[1].strftime("%d/%m/%Y %H:%M:%S"),
                                                i[2]))

    print('*' * 200)
    result = find_full_weeks_in_period(datetime(2003, 7, 1), datetime(2004, 7, 1))
    print("Total weeks: {}".format(len(result)))
    print(" {:^30} | {:^30} | {:^50}".format("start", "end", ""))
    for i in result:
        print(" {:^30} | {:^30} | {:50}".format(i[0].strftime("%d/%m/%Y %H:%M:%S"),
                                                i[1].strftime("%d/%m/%Y %H:%M:%S"),
                                                i[2]))

    print('*' * 200)
    result = find_full_weeks_in_period(datetime(2019, 1, 1), datetime(2019, 1, 6))
    print("Total weeks: {}".format(len(result)))
    print(" {:^30} | {:^30} | {:^50}".format("start", "end", ""))
    for i in result:
        print(" {:^30} | {:^30} | {:50}".format(i[0].strftime("%d/%m/%Y %H:%M:%S"),
                                                i[1].strftime("%d/%m/%Y %H:%M:%S"),
                                                i[2]))

    print('*' * 200)
    result = find_full_weeks_in_period(datetime(2003, 7, 1), datetime(2003, 7, 31))
    print("Total weeks: {}".format(len(result)))
    print(" {:^30} | {:^30} | {:^50}".format("start", "end", ""))
    for i in result:
        print(" {:^30} | {:^30} | {:50}".format(i[0].strftime("%d/%m/%Y %H:%M:%S"),
                                                i[1].strftime("%d/%m/%Y %H:%M:%S"),
                                                i[2]))

    result = find_full_weeks_in_period(datetime(2026, 12, 17), datetime(2027, 1, 28))
    print("Total weeks: {}".format(len(result)))
    print(" {:^30} | {:^30} | {:^50}".format("start", "end", ""))
    for i in result:
        print(" {:^30} | {:^30} | {:50}".format(i[0].strftime("%d/%m/%Y %H:%M:%S"),
                                                i[1].strftime("%d/%m/%Y %H:%M:%S"),
                                                i[2]))

    for i in range(len(result)):
        print(result[i][0].strftime("%d/%m/%Y %H:%M:%S"), result[i][1].strftime("%d/%m/%Y %H:%M:%S"), result[i][2])

    result = find_full_weeks_in_period(datetime(2010, 6, 6), datetime(2010, 6, 6))
    print(result[0][0].strftime("%d/%m/%Y %H:%M:%S"))
    print(result[0][1].strftime("%d/%m/%Y %H:%M:%S"))
    print(result[0][2])

    result = find_full_weeks_in_period(datetime(2000, 5, 24), datetime(2019, 2, 24))
    print(len(result))

    result = find_full_month_in_period(datetime(2000, 5, 24), datetime(2001, 2, 24))
    print("Total weeks: {}".format(len(result)))
    print(" {:^30} | {:^30} | {:^50}".format("start", "end", ""))
    for i in result:
        print(" {:^30} | {:^30} | {:50}".format(i[0].strftime("%d/%m/%Y %H:%M:%S"),
                                                i[1].strftime("%d/%m/%Y %H:%M:%S"),
                                                i[2]))

    result = find_full_month_in_period(datetime(1986, 9, 20), datetime(1986, 9, 20))
    print("Total weeks: {}".format(len(result)))
    print(" {:^30} | {:^30} | {:^50}".format("start", "end", ""))
    for i in result:
        print(" {:^30} | {:^30} | {:50}".format(i[0].strftime("%d/%m/%Y %H:%M:%S"),
                                                i[1].strftime("%d/%m/%Y %H:%M:%S"),
                                                i[2]))

