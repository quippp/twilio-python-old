import unittest
import datetime

from twilio import serialize
from twilio import values


class Iso8601DateTestCase(unittest.TestCase):

    def test_unset(self):
        value = values.unset
        actual = serialize.iso8601_date(value)
        self.assertEqual(values.unset, actual)

    def test_datetime(self):
        value = datetime.datetime(2015, 1, 2, 12, 0, 0, 0)
        actual = serialize.iso8601_date(value)
        self.assertEqual('2015-01-02', actual)

    def test_datetime_without_time(self):
        value = datetime.datetime(2015, 1, 2)
        actual = serialize.iso8601_date(value)
        self.assertEqual('2015-01-02', actual)

    def test_date(self):
        value = datetime.date(2015, 1, 2)
        actual = serialize.iso8601_date(value)
        self.assertEqual('2015-01-02', actual)

    def test_str(self):
        actual = serialize.iso8601_date('2015-01-02')
        self.assertEqual('2015-01-02', actual)


class Iso8601DateTimeTestCase(unittest.TestCase):

    def test_unset(self):
        value = values.unset
        actual = serialize.iso8601_datetime(value)
        self.assertEqual(values.unset, actual)

    def test_datetime(self):
        value = datetime.datetime(2015, 1, 2, 3, 4, 5, 6)
        actual = serialize.iso8601_datetime(value)
        self.assertEqual('2015-01-02T03:04:05Z', actual)

    def test_datetime_without_time(self):
        value = datetime.datetime(2015, 1, 2)
        actual = serialize.iso8601_datetime(value)
        self.assertEqual('2015-01-02T00:00:00Z', actual)

    def test_date(self):
        value = datetime.date(2015, 1, 2)
        actual = serialize.iso8601_datetime(value)
        self.assertEqual('2015-01-02T00:00:00Z', actual)

    def test_str(self):
        actual = serialize.iso8601_datetime('2015-01-02T03:04:05Z')
        self.assertEqual('2015-01-02T03:04:05Z', actual)
