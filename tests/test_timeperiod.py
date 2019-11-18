import unittest
from timeperiod import Period


class TestPeriod(unittest.TestCase):

    @staticmethod
    def preparation(customer_name='787513', delta=0, start_event=1, end_event=0) -> Period:
        """
        Function which make setup for Period class instance
        :param customer_name: str, default = '787513'
        :param delta: int, time delta between start and end
        :param start_event: event on the start
        :param end_event: event on the end
        :return: Period class instance
        """
        p = Period()
        p.set_start((customer_name, 1574017545, start_event))
        p.set_end((customer_name, 1574017545 + delta, end_event))
        return p

    def test_start_time_equal_end_time(self):
        # Checking case when start time equal end time
        p = self.preparation()
        self.assertEqual(p.calculate_period_length(), 0)

    def test_start_time_less_then_end_time(self):  # ?? what return must be ??
        # Checking case when start time less then end time
        p = self.preparation(delta=(-600))
        self.assertEqual(p.calculate_period_length(), 0)

    def test_start_time_better_then_end_time(self):
        # Checking case when start time better then end time
        p = self.preparation(delta=9000)
        self.assertEqual(p.calculate_period_length(), 9000)

    def test_end_is_none(self):
        # Checking case when end time equal to None
        p = Period()
        p.set_start(('787513', 1574017545, 1))
        self.assertEqual(p.calculate_period_length(), 0)

    def test_start_is_none(self):  # test case when _start is None
        # Checking case when start time equal to None
        with self.assertRaises(TypeError):
            p = Period()
            p.set_end(('787513', 1574017545, 0))
            p.calculate_period_length()
        # self.assertRaises(TypeError, p.calculate_period_length())

    def test_start_and_end_is_none(self):
        # Checking case when the start time and end time are equal to None
        p = Period()
        self.assertEqual(p.calculate_period_length(), 0)

    def test_that_the_events_are_equivalent(self):
        # Checking case when the start event equal to end event
        p1 = self.preparation(delta=90, end_event=1)
        p2 = self.preparation(delta=100, start_event=0)
        self.assertEqual(p1.calculate_period_length(), 0)
        self.assertEqual(p2.calculate_period_length(), 0)

    def test_start_event_and_end_event_are_zero(self):
        # Checking case when the start event and end events equals to zero
        p = self.preparation(delta=1000, start_event=0, end_event=0)
        self.assertEqual(p.calculate_period_length(), 0)

    def test_start_period_equal_start_search_frame(self):
        # Checking case when the start of period equal to start search frame
        # start_event == 100
        p = self.preparation(delta=1000, start_event=100)
        self.assertEqual(p.calculate_period_length(), 1000)

    def test_end_period_equal_end_search_frame(self):
        # Checking case when the end of period equal to end search frame
        # end_event == 200
        p = self.preparation(delta=2000, end_event=200)
        self.assertEqual(p.calculate_period_length(), 2000)

    def test_start_period_equal_start_search_frame_and_end_period_equal_end_search_frame(self):  # ? what must return ?
        # Checking case when the start event equal 100 and end event equal 200
        # start_event == 100 and end_event == 200
        p = self.preparation(delta=25, start_event=100, end_event=200)
        self.assertEqual(p.calculate_period_length(), 25)

    def test_start_period_equal_start_search_frame_and_end_is_one(self):
        # Checking case when the start event equal 100 and end event equal 1
        p = self.preparation(delta=400, start_event=100, end_event=1)
        self.assertEqual(p.calculate_period_length(), 0)

    def test_start_period_equal_zero_and_end_period_is_200(self):
        # Checking case when the start event equal to 0 and end event equal to 200
        p = self.preparation(delta=500, start_event=0, end_event=200)
        self.assertEqual(p.calculate_period_length(), 0)

    def test_start_period_equal_200_and_end_period_is_100(self):
        # Checking case when the start event equal to 0 and end event equal to 200
        p = self.preparation(delta=500, start_event=200, end_event=100)
        self.assertEqual(p.calculate_period_length(), None)

    def test_range_of_available_values_of_event_variable(self): # Не обработаны случаи, когда event не равно нужным знач
        # Checking cases when the events values are not 1, 2, 100 or 200
        # In this case function must return 0 or None
        available_values = [2, 3, 300, 400, -1, -200]
        p = Period()
        for i in available_values:
            for j in available_values:
                p.set_start(('787513', 1574017545, i))
                p.set_end(('787513', 1574017545 + 200, j))
                self.assertIn(p.calculate_period_length(), [None, 0])


if __name__ == '__main__':
    unittest.main()
