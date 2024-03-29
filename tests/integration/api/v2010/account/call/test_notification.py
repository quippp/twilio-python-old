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


class NotificationTestCase(IntegrationTestCase):

    def test_fetch_request(self):
        self.holodeck.mock(Response(500, ''))
        
        with self.assertRaises(TwilioException):
            self.client.api.v2010.accounts(sid="ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                 .calls(sid="CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                 .notifications(sid="NOaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa").fetch()
        
        self.holodeck.assert_has_request(Request(
            'get',
            'https://api.twilio.com/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Notifications/NOaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json',
        ))

    def test_fetch_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "api_version": "2008-08-01",
                "call_sid": "CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "date_created": "Tue, 18 Aug 2015 08:46:56 +0000",
                "date_updated": "Tue, 18 Aug 2015 08:46:57 +0000",
                "error_code": "15003",
                "log": "1",
                "message_date": "Tue, 18 Aug 2015 08:46:56 +0000",
                "message_text": "statusCallback=http%3A%2F%2Fexample.com%2Ffoo.xml&ErrorCode=15003&LogLevel=WARN&Msg=Got+HTTP+404+response+to+http%3A%2F%2Fexample.com%2Ffoo.xml",
                "more_info": "https://www.twilio.com/docs/errors/15003",
                "request_method": null,
                "request_url": "",
                "request_variables": "",
                "response_body": "",
                "response_headers": "",
                "sid": "NOaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Notifications/NOaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json"
            }
            '''
        ))
        
        actual = self.client.api.v2010.accounts(sid="ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                      .calls(sid="CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                      .notifications(sid="NOaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa").fetch()
        
        self.assertIsNotNone(actual)

    def test_delete_request(self):
        self.holodeck.mock(Response(500, ''))
        
        with self.assertRaises(TwilioException):
            self.client.api.v2010.accounts(sid="ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                 .calls(sid="CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                 .notifications(sid="NOaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa").delete()
        
        self.holodeck.assert_has_request(Request(
            'delete',
            'https://api.twilio.com/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Notifications/NOaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json',
        ))

    def test_delete_response(self):
        self.holodeck.mock(Response(
            204,
            None,
        ))
        
        actual = self.client.api.v2010.accounts(sid="ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                      .calls(sid="CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                      .notifications(sid="NOaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa").delete()
        
        self.assertTrue(actual)

    def test_list_request(self):
        self.holodeck.mock(Response(500, ''))
        
        with self.assertRaises(TwilioException):
            self.client.api.v2010.accounts(sid="ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                 .calls(sid="CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                 .notifications.list()
        
        self.holodeck.assert_has_request(Request(
            'get',
            'https://api.twilio.com/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Notifications.json',
        ))

    def test_read_full_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "end": 0,
                "first_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Notifications.json?PageSize=50&Page=0",
                "last_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Notifications.json?PageSize=50&Page=0",
                "next_page_uri": null,
                "notifications": [
                    {
                        "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "api_version": "2008-08-01",
                        "call_sid": "CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "date_created": "Tue, 18 Aug 2015 08:46:56 +0000",
                        "date_updated": "Tue, 18 Aug 2015 08:46:57 +0000",
                        "error_code": "15003",
                        "log": "1",
                        "message_date": "Tue, 18 Aug 2015 08:46:56 +0000",
                        "message_text": "statusCallback=http%3A%2F%2Fexample.com%2Ffoo.xml&ErrorCode=15003&LogLevel=WARN&Msg=Got+HTTP+404+response+to+http%3A%2F%2Fexample.com%2Ffoo.xml",
                        "more_info": "https://www.twilio.com/docs/errors/15003",
                        "request_method": null,
                        "request_url": "",
                        "sid": "NOaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Notifications/NOaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                    }
                ],
                "num_pages": 1,
                "page": 0,
                "page_size": 50,
                "previous_page_uri": null,
                "start": 0,
                "total": 1,
                "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Notifications.json"
            }
            '''
        ))
        
        actual = self.client.api.v2010.accounts(sid="ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                      .calls(sid="CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                      .notifications.list()
        
        self.assertIsNotNone(actual)

    def test_read_empty_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "end": 0,
                "first_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Notifications.json?PageSize=50&Page=0",
                "last_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Notifications.json?PageSize=50&Page=0",
                "next_page_uri": null,
                "notifications": [],
                "num_pages": 1,
                "page": 0,
                "page_size": 50,
                "previous_page_uri": null,
                "start": 0,
                "total": 1,
                "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Calls/CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Notifications.json"
            }
            '''
        ))
        
        actual = self.client.api.v2010.accounts(sid="ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                      .calls(sid="CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                      .notifications.list()
        
        self.assertIsNotNone(actual)
