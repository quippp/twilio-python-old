# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /       
"""

from tests.integration import IntegrationTestCase
from tests.integration.holodeck import Request
from twilio.exceptions import TwilioException
from twilio.http.response import Response


class SmsMessageTestCase(IntegrationTestCase):

    def test_create_request(self):
        self.holodeck.mock(Response(500, ''))
        
        with self.assertRaises(TwilioException):
            self.client.api.v2010.accounts(sid="ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                 .sms \
                                 .messages.create(to="+123456789", from_="+987654321")
        
        values = {
            'To': "+123456789",
            'From': "+987654321",
        }
        
        self.holodeck.assert_has_request(Request(
            'post',
            'https://api.twilio.com/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/SMS/Messages.json',
            data=values,
        ))

    def test_create_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "api_version": "2008-08-01",
                "body": "n",
                "date_created": "Mon, 26 Jul 2010 21:46:42 +0000",
                "date_sent": "Mon, 26 Jul 2010 21:46:44 +0000",
                "date_updated": "Mon, 26 Jul 2010 21:46:44 +0000",
                "direction": "outbound-api",
                "from": "+141586753093",
                "price": "-0.03000",
                "price_unit": "USD",
                "sid": "SMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "status": "sent",
                "to": "+141586753096",
                "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/SMS/Messages/SMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json"
            }
            '''
        ))
        
        actual = self.client.api.v2010.accounts(sid="ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                      .sms \
                                      .messages.create(to="+123456789", from_="+987654321")
        
        self.assertIsNotNone(actual)

    def test_delete_request(self):
        self.holodeck.mock(Response(500, ''))
        
        with self.assertRaises(TwilioException):
            self.client.api.v2010.accounts(sid="ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                 .sms \
                                 .messages(sid="SMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa").delete()
        
        self.holodeck.assert_has_request(Request(
            'delete',
            'https://api.twilio.com/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/SMS/Messages/SMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json',
        ))

    def test_delete_response(self):
        self.holodeck.mock(Response(
            204,
            None,
        ))
        
        actual = self.client.api.v2010.accounts(sid="ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                      .sms \
                                      .messages(sid="SMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa").delete()
        
        self.assertTrue(actual)

    def test_fetch_request(self):
        self.holodeck.mock(Response(500, ''))
        
        with self.assertRaises(TwilioException):
            self.client.api.v2010.accounts(sid="ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                 .sms \
                                 .messages(sid="SMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa").fetch()
        
        self.holodeck.assert_has_request(Request(
            'get',
            'https://api.twilio.com/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/SMS/Messages/SMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json',
        ))

    def test_fetch_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "api_version": "2008-08-01",
                "body": "n",
                "date_created": "Mon, 26 Jul 2010 21:46:42 +0000",
                "date_sent": "Mon, 26 Jul 2010 21:46:44 +0000",
                "date_updated": "Mon, 26 Jul 2010 21:46:44 +0000",
                "direction": "outbound-api",
                "from": "+141586753093",
                "price": "-0.03000",
                "price_unit": "USD",
                "sid": "SMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "status": "sent",
                "to": "+141586753096",
                "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/SMS/Messages/SMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json"
            }
            '''
        ))
        
        actual = self.client.api.v2010.accounts(sid="ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                      .sms \
                                      .messages(sid="SMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa").fetch()
        
        self.assertIsNotNone(actual)

    def test_list_request(self):
        self.holodeck.mock(Response(500, ''))
        
        with self.assertRaises(TwilioException):
            self.client.api.v2010.accounts(sid="ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                 .sms \
                                 .messages.list()
        
        self.holodeck.assert_has_request(Request(
            'get',
            'https://api.twilio.com/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/SMS/Messages.json',
        ))

    def test_read_full_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "end": 0,
                "first_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/SMS/Messages.json?PageSize=1&Page=0",
                "last_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/SMS/Messages.json?PageSize=1&Page=119771",
                "next_page_uri": null,
                "num_pages": 119772,
                "page": 0,
                "page_size": 1,
                "previous_page_uri": null,
                "sms_messages": [
                    {
                        "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "api_version": "2010-04-01",
                        "body": "O Slash: \u00d8, PoP: \ud83d\udca9",
                        "date_created": "Fri, 04 Sep 2015 22:54:39 +0000",
                        "date_sent": "Fri, 04 Sep 2015 22:54:41 +0000",
                        "date_updated": "Fri, 04 Sep 2015 22:54:41 +0000",
                        "direction": "outbound-api",
                        "from": "+14155552345",
                        "num_segments": "1",
                        "price": "-0.00750",
                        "price_unit": "USD",
                        "sid": "SMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "status": "sent",
                        "to": "+14155552345",
                        "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/SMS/Messages/SMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json"
                    }
                ],
                "start": 0,
                "total": 119772,
                "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/SMS/Messages.json?PageSize=1&Page=0"
            }
            '''
        ))
        
        actual = self.client.api.v2010.accounts(sid="ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                      .sms \
                                      .messages.list()
        
        self.assertIsNotNone(actual)

    def test_read_empty_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "end": 0,
                "first_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/SMS/Messages.json?PageSize=1&Page=0",
                "last_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/SMS/Messages.json?PageSize=1&Page=119771",
                "next_page_uri": null,
                "num_pages": 119772,
                "page": 0,
                "page_size": 1,
                "previous_page_uri": null,
                "sms_messages": [],
                "start": 0,
                "total": 119772,
                "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/SMS/Messages.json?PageSize=1&Page=0"
            }
            '''
        ))
        
        actual = self.client.api.v2010.accounts(sid="ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                      .sms \
                                      .messages.list()
        
        self.assertIsNotNone(actual)

    def test_update_request(self):
        self.holodeck.mock(Response(500, ''))
        
        with self.assertRaises(TwilioException):
            self.client.api.v2010.accounts(sid="ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                 .sms \
                                 .messages(sid="SMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa").update()
        
        self.holodeck.assert_has_request(Request(
            'post',
            'https://api.twilio.com/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/SMS/Messages/SMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json',
        ))

    def test_update_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "api_version": "2008-08-01",
                "body": "n",
                "date_created": "Mon, 26 Jul 2010 21:46:42 +0000",
                "date_sent": "Mon, 26 Jul 2010 21:46:44 +0000",
                "date_updated": "Mon, 26 Jul 2010 21:46:44 +0000",
                "direction": "outbound-api",
                "from": "+141586753093",
                "price": "-0.03000",
                "price_unit": "USD",
                "sid": "SMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "status": "sent",
                "to": "+141586753096",
                "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/SMS/Messages/SMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json"
            }
            '''
        ))
        
        actual = self.client.api.v2010.accounts(sid="ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                      .sms \
                                      .messages(sid="SMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa").update()
        
        self.assertIsNotNone(actual)
