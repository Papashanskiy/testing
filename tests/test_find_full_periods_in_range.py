import unittest
from datetime import datetime, timedelta
from find_full_periods_in_range import find_full_days_in_period, find_full_weeks_in_period, find_full_month_in_period
from tests.patterns.patterns import Pattern_test_find_full_weeks_in_period, Pattern_test_find_full_month_in_period


class Test_find_full_days_in_period(unittest.TestCase):

    def test_one_day(self):
        # Days between 1/1/2019 and 1/1/2019
        result_date = find_full_days_in_period(datetime(2019, 1, 1), datetime(2019, 1, 1))
        self.assertEqual(len(result_date), 1)  # Number of days between 1/1/2019 and 1/1/2019
        self.assertEqual(result_date[0][0].strftime("%d/%m/%Y %H:%M:%S"), r'01/01/2019 00:00:00')
        self.assertEqual(result_date[0][1].strftime("%d/%m/%Y %H:%M:%S"), r'01/01/2019 23:59:59')
        self.assertEqual(result_date[0][2], '2019.01.01')

    def test_week(self):
        # Number of days between 29/12/2018 and 4/1/2019
        result_date = find_full_days_in_period(datetime(2018, 12, 29), datetime(2019, 1, 4))
        self.assertEqual(len(result_date), 7)  # Number of days must be equal 7
        cur = datetime(2018, 12, 29)
        for i in result_date:  # test first returned tuple
            self.assertEqual(i[0].strftime("%d/%m/%Y %H:%M:%S"), cur.strftime("%d/%m/%Y %H:%M:%S"))
            cur += timedelta(seconds=86400)
        cur = datetime(2018, 12, 29) + timedelta(seconds=86399)
        for i in result_date:  # test second returned tuple
            self.assertEqual(i[1].strftime("%d/%m/%Y %H:%M:%S"), cur.strftime("%d/%m/%Y %H:%M:%S"))
            cur += timedelta(seconds=86400)
        cur = datetime(2018, 12, 29)
        for i in result_date:
            self.assertEqual(i[2], cur.strftime("%Y.%m.%d"))
            cur += timedelta(seconds=86400)

    def test_month(self):
        # Number of days between month 1/7/2003 and 31/7/2003
        result_date = find_full_days_in_period(datetime(2003, 7, 1), datetime(2003, 7, 31))
        self.assertEqual(len(result_date), 31)
        cur = datetime(2003, 7, 1)
        for i in result_date:  # test first returned tuple
            self.assertEqual(i[0].strftime("%d/%m/%Y %H:%M:%S"), cur.strftime("%d/%m/%Y %H:%M:%S"))
            cur += timedelta(seconds=86400)
        cur = datetime(2003, 7, 1) + timedelta(seconds=86399)
        for i in result_date:  # test second returned tuple
            self.assertEqual(i[1].strftime("%d/%m/%Y %H:%M:%S"), cur.strftime("%d/%m/%Y %H:%M:%S"))
            cur += timedelta(seconds=86400)
        cur = datetime(2003, 7, 1)
        for i in result_date:
            self.assertEqual(i[2], cur.strftime("%Y.%m.%d"))
            cur += timedelta(seconds=86400)

    def test_year(self):
        # Number of days between year
        result_date = find_full_days_in_period(datetime(1990, 9, 13), datetime(1991, 9, 12))
        self.assertEqual(len(result_date), 365)
        cur = datetime(1990, 9, 13)
        for i in result_date:  # test first returned tuple
            self.assertEqual(i[0].strftime("%d/%m/%Y %H:%M:%S"), cur.strftime("%d/%m/%Y %H:%M:%S"))
            cur += timedelta(seconds=86400)
        cur = datetime(1990, 9, 13) + timedelta(seconds=86399)
        for i in result_date:  # test second returned tuple
            self.assertEqual(i[1].strftime("%d/%m/%Y %H:%M:%S"), cur.strftime("%d/%m/%Y %H:%M:%S"))
            cur += timedelta(seconds=86400)
        cur = datetime(1990, 9, 13)
        for i in result_date:
            self.assertEqual(i[2], cur.strftime("%Y.%m.%d"))
            cur += timedelta(seconds=86400)

    def test_instances(self):
        # Checking if an objects belong to instances
        result_date = find_full_days_in_period(datetime(2003, 7, 8), datetime(2018, 3, 12))
        self.assertIsInstance(result_date[0][0], datetime)
        self.assertIsInstance(result_date[15][0], datetime)
        self.assertIsInstance(result_date[0][1], datetime)
        self.assertIsInstance(result_date[-1][1], datetime)
        self.assertIsInstance(result_date[0][2], str)

    def test_start_less_then_end_raise(self):
        # Checking case when start date less then end
        self.assertRaises(ValueError, find_full_days_in_period, datetime(2003, 7, 8), datetime(2002, 3, 12))


class Test_find_full_weeks_in_period(unittest.TestCase):

    def test_one_day(self):
        # Result when start and end equals
        result_date = find_full_weeks_in_period(datetime(2010, 6, 6), datetime(2010, 6, 6))
        self.assertEqual(result_date[0][0].strftime("%d/%m/%Y %H:%M:%S"), "06/06/2010 00:00:00")
        self.assertEqual(result_date[0][1].strftime("%d/%m/%Y %H:%M:%S"), "06/06/2010 23:59:59")
        self.assertEqual(result_date[0][2], "2010/22")

    def test_one_week(self):
        # Weeks between 1/1/2019 and 7/1/2019
        result_date = find_full_weeks_in_period(datetime(2019, 1, 1), datetime(2019, 1, 6))
        self.assertEqual(len(result_date), 1)  # Number of days between 1/1/2019 and 1/1/2019
        self.assertEqual(result_date[0][0].strftime("%d/%m/%Y %H:%M:%S"), r'01/01/2019 00:00:00')
        self.assertEqual(result_date[0][1].strftime("%d/%m/%Y %H:%M:%S"), r'06/01/2019 23:59:59')
        self.assertEqual(result_date[0][2], '2019/1')

    def test_month(self):
        # Number of weeks between month 17/12/2026 and 28/1/2027
        start, end = datetime(2026, 12, 17), datetime(2027, 1, 28)
        result_date = find_full_weeks_in_period(start, end)
        self.assertEqual(len(result_date), 7)
        for i in range(len(result_date)):   # test first returned tuple
            self.assertEqual(result_date[i][0].strftime("%d/%m/%Y %H:%M:%S"),
                             Pattern_test_find_full_weeks_in_period.pattern_for_test_month[i][0])
        for i in range(len(result_date)):   # test second returned tuple
            self.assertEqual(result_date[i][1].strftime("%d/%m/%Y %H:%M:%S"),
                             Pattern_test_find_full_weeks_in_period.pattern_for_test_month[i][1])
        for i in range(len(result_date)):
            self.assertEqual(result_date[i][2],
                             Pattern_test_find_full_weeks_in_period.pattern_for_test_month[i][2])

    def test_quantity_of_weeks_in_six_month(self):
        # Checking quantity of the weeks in the six month
        result_date = find_full_weeks_in_period(datetime(1996, 1, 1), datetime(1996, 6, 1))
        self.assertEqual(len(result_date), 22)

    def test_quantity_of_weeks_in_year(self):
        # Checking quantity of the weeks in the year
        result_date = find_full_weeks_in_period(datetime(2000, 5, 24), datetime(2001, 5, 24))
        self.assertEqual(len(result_date), 52)

    def test_quantity_of_weeks_in_big_period(self):
        # Checking quantity of the weeks in the year
        result_date = find_full_weeks_in_period(datetime(2000, 5, 24), datetime(2019, 2, 24))
        self.assertEqual(len(result_date), 979)

    def test_instances(self):
        # Checking if an objects belong to instances
        result_date = find_full_weeks_in_period(datetime(2003, 7, 8), datetime(2018, 3, 12))
        self.assertIsInstance(result_date[0][0], datetime)
        self.assertIsInstance(result_date[15][0], datetime)
        self.assertIsInstance(result_date[0][1], datetime)
        self.assertIsInstance(result_date[-1][1], datetime)
        self.assertIsInstance(result_date[0][2], str)

    def test_start_less_then_end(self):
        # Checking case when start date less then end
        self.assertRaises(ValueError, find_full_weeks_in_period, datetime(2003, 7, 8), datetime(2002, 3, 12))


class Test_find_full_month_in_period(unittest.TestCase):

    def test_start_equal_end(self):
        # Checking the case when start argument equal end argument
        result_date = find_full_month_in_period(datetime(1986, 9, 20), datetime(1986, 9, 20))
        self.assertEqual(len(result_date), 1)
        self.assertEqual(result_date[0][0].strftime("%d/%m/%Y %H:%M:%S"), "20/09/1986 00:00:00")
        self.assertEqual(result_date[0][1].strftime("%d/%m/%Y %H:%M:%S"), "20/09/1986 00:00:00")
        self.assertEqual(result_date[0][2], "1986.09")

    def test_one_month(self):
        # Checking the case when the period is equal to the month
        result_date = find_full_month_in_period(datetime(1990, 9, 1), datetime(1990, 10, 1))
        self.assertEqual(len(result_date), 2)
        for i in range(len(result_date)):
            self.assertEqual(result_date[i][0].strftime("%d/%m/%Y %H:%M:%S"),
                             Pattern_test_find_full_month_in_period.pattern_for_test_month[i][0])
        for i in range(len(result_date)):
            self.assertEqual(result_date[i][1].strftime("%d/%m/%Y %H:%M:%S"),
                             Pattern_test_find_full_month_in_period.pattern_for_test_month[i][1])
        for i in range(len(result_date)):
            self.assertEqual(result_date[i][0].strftime("%Y.%m"),
                             Pattern_test_find_full_month_in_period.pattern_for_test_month[i][2])

    def test_year(self):
        # Checking the case when the period is equal to the year
        result_date = find_full_month_in_period(datetime(1990, 9, 1), datetime(1991, 9, 1))
        self.assertEqual(len(result_date), 13)
        for i in range(len(result_date)):
            self.assertEqual(result_date[i][0].strftime("%d/%m/%Y %H:%M:%S"),
                             Pattern_test_find_full_month_in_period.pattern_for_test_year[i][0])
        for i in range(len(result_date)):
            self.assertEqual(result_date[i][1].strftime("%d/%m/%Y %H:%M:%S"),
                             Pattern_test_find_full_month_in_period.pattern_for_test_year[i][1])
        for i in range(len(result_date)):
            self.assertEqual(result_date[i][0].strftime("%Y.%m"),
                             Pattern_test_find_full_month_in_period.pattern_for_test_year[i][2])

    def test_instances(self):
        # Checking if an objects belong to instances
        result_date = find_full_weeks_in_period(datetime(2003, 7, 8), datetime(2018, 3, 12))
        self.assertIsInstance(result_date[0][0], datetime)
        self.assertIsInstance(result_date[15][0], datetime)
        self.assertIsInstance(result_date[0][1], datetime)
        self.assertIsInstance(result_date[-1][1], datetime)
        self.assertIsInstance(result_date[0][2], str)

    def test_quantity_of_month_in_big_period(self):
        # Checking quantity of the weeks in the year
        result_date = find_full_month_in_period(datetime(1892, 6, 7), datetime(1970, 7, 24))
        self.assertEqual(len(result_date), 938)

    def test_start_less_then_end(self):
        # Checking case when start date less then end
        self.assertRaises(ValueError, find_full_weeks_in_period, datetime(2006, 7, 8), datetime(2006, 3, 12))


if __name__ == '__main__':
    unittest.main()
