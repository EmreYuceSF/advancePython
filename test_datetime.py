import unittest
import datetime


class TestDateTime(unittest.TestCase):
    the_date = datetime.date(1756, 1, 27)
    
    # variety of timedelta objects to use
    one_hour = datetime.timedelta(hours=1)
    zero_hour = datetime.timedelta(hours=0)
    twenty_four_hours = datetime.timedelta(hours=24)
    one_day = datetime.timedelta(days=1)
    one_hundred_days = datetime.timedelta(100) 
    ten_days = datetime.timedelta(days=10)
    four_weeks = datetime.timedelta(weeks=4)
    negative_one_day = datetime.timedelta(days=-1)
    one_and_half_weeks = datetime.timedelta(weeks=1.5) # 7 + 3.5 = 10 full days + 12 hours
    mix = datetime.timedelta(weeks=52, days=0.5, hours=11, minutes=59, seconds=59, milliseconds=999, microseconds=999) # almost a year (1 microsecond less)
    mix2 = datetime.timedelta(weeks=52, days=0.5, hours=11, minutes=59, seconds=59, milliseconds=999, microseconds=1000) # exact 365 days

    def test_add_one_hour(self):
        expected = datetime.date(1756, 1, 27)
        result = self.the_date + self.one_hour
        self.assertEqual(expected, result)

    def test_sub_one_hour(self):
        expected = datetime.date(1756, 1, 27)
        result = self.the_date - self.one_hour
        self.assertEqual(expected, result)

    def test_add_zero_hour(self):
        expected = datetime.date(1756, 1, 27)
        result = self.the_date + self.zero_hour
        self.assertEqual(expected, result)

    def test_sub_zero_hour(self):
        expected = datetime.date(1756, 1, 27)
        result = self.the_date - self.zero_hour
        self.assertEqual(expected, result)

    def test_add_twenty_four_hours(self):
        expected = datetime.date(1756, 1, 28)
        result = self.the_date + self.twenty_four_hours
        self.assertEqual(expected, result)

    def test_sub_twenty_four_hours(self):
        expected = datetime.date(1756, 1, 26)
        result = self.the_date - self.twenty_four_hours
        self.assertEqual(expected, result)
    
    def test_add_ten_days(self):
        expected = datetime.date(1756, 2, 6)
        result = self.the_date + self.ten_days
        self.assertEqual(expected, result)

    def test_sub_ten_days(self):
        expected = datetime.date(1756, 1, 17)
        result = self.the_date - self.ten_days
        self.assertEqual(expected, result)

    def test_add_four_weeks(self):
        expected = datetime.date(1756,2,24)
        result = self.the_date + self.four_weeks
        self.assertEqual(expected, result)

    def test_sub_four_weeks(self):
        expected = datetime.date(1755,12,30)
        result = self.the_date - self.four_weeks
        self.assertEqual(expected, result)

    def test_add_negative_day(self):
        expected = datetime.date(1756, 1, 26)
        result = self.the_date + self.negative_one_day
        self.assertEqual(expected, result)

    def test_sub_negative_day(self):
        expected = datetime.date(1756, 1, 28)
        result = self.the_date - self.negative_one_day
        self.assertEqual(expected, result)
        
    def test_add_one_hundred_days(self):
        expected = datetime.date(1756,5,6)
        result = self.the_date + self.one_hundred_days
        self.assertEqual(expected, result)
        
    def test_add_sub_hundred_days(self):
        expected = datetime.date(1755,10,19)
        result = self.the_date - self.one_hundred_days
        self.assertEqual(expected, result)
        
    def test_add_one_and_a_half_week(self):
        expected = datetime.date(1756,2,6)
        result = self.the_date + self.one_and_half_weeks
        self.assertEqual(expected, result)
        
    def test_sub_one_and_a_half_week(self):
        expected = datetime.date(1756,1,17)
        result = self.the_date - self.one_and_half_weeks
        self.assertEqual(expected, result) 
        
    def test_add_mix(self):
        expected = datetime.date(1757, 1, 25) # leap year! (feb 29 days in 1756)
        result = self.the_date + self.mix
        self.assertEqual(expected, result)
        
    def test_sub_mix(self):
        expected = datetime.date(1755, 1, 28) 
        result = self.the_date - self.mix
        self.assertEqual(expected, result)
        
    def test_add_mix2(self):
        expected = datetime.date(1757, 1, 26) # leap year! (feb 29 days in 1756)
        result = self.the_date + self.mix2
        self.assertEqual(expected, result)
        
    def test_sub_mix2(self):
        expected = datetime.date(1755, 1, 27) 
        result = self.the_date - self.mix2
        self.assertEqual(expected, result)
            
    def test_add_3650_days(self): # to see if it is calculating the leap years
        expected = datetime.date(1766, 1, 24)  # Adding 3650 days to the_date, accounting for leap years(*1756, *1760, *1764, 1768...)
        result = self.the_date + datetime.timedelta(days=3650)
        self.assertEqual(expected, result)
    
    def test_sub_3650_days(self): # to see if it is calculating the leap years
        expected = datetime.date(1746, 1, 29)  # Adding 3650 days to the_date, accounting for leap years(*1752, *1748, 1744, 1740...)
        result = self.the_date - datetime.timedelta(days=3650)
        self.assertEqual(expected, result)
        
    # that many tests looks good to me   

if __name__ == "__main__":
    unittest.main()

