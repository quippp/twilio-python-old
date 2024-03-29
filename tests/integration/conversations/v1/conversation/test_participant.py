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


class ParticipantTestCase(IntegrationTestCase):

    def test_list_request(self):
        self.holodeck.mock(Response(500, ''))
        
        with self.assertRaises(TwilioException):
            self.client.conversations.v1.conversations(sid="CVaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                        .participants.list()
        
        self.holodeck.assert_has_request(Request(
            'get',
            'https://conversations.twilio.com/v1/Conversations/CVaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Participants',
        ))

    def test_read_full_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "meta": {
                    "first_page_url": "https://conversations.twilio.com/v1/Conversations/CVaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Participants?PageSize=50&Page=0",
                    "key": "participants",
                    "next_page_url": null,
                    "page": 0,
                    "page_size": 50,
                    "previous_page_url": null,
                    "url": "https://conversations.twilio.com/v1/Conversations/CVaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Participants?PageSize=50&Page=0"
                },
                "participants": [
                    {
                        "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "address": "torkel2@ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.endpoint.twilio.com",
                        "conversation_sid": "CVaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "date_created": "2015-05-13T23:03:12Z",
                        "duration": 685,
                        "end_time": "2015-05-13T23:14:40Z",
                        "sid": "PAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "start_time": "2015-05-13T23:03:15Z",
                        "status": "disconnected",
                        "url": "https://conversations.twilio.com/v1/Conversations/CVaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Participants/PAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                    }
                ]
            }
            '''
        ))
        
        actual = self.client.conversations.v1.conversations(sid="CVaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                             .participants.list()
        
        self.assertIsNotNone(actual)

    def test_read_empty_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "meta": {
                    "first_page_url": "https://conversations.twilio.com/v1/Conversations/CVaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Participants?PageSize=50&Page=0",
                    "key": "participants",
                    "next_page_url": null,
                    "page": 0,
                    "page_size": 50,
                    "previous_page_url": null,
                    "url": "https://conversations.twilio.com/v1/Conversations/CVaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Participants?PageSize=50&Page=0"
                },
                "participants": []
            }
            '''
        ))
        
        actual = self.client.conversations.v1.conversations(sid="CVaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                             .participants.list()
        
        self.assertIsNotNone(actual)

    def test_create_request(self):
        self.holodeck.mock(Response(500, ''))
        
        with self.assertRaises(TwilioException):
            self.client.conversations.v1.conversations(sid="CVaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                        .participants.create(to="+123456789", from_="+987654321")
        
        values = {
            'To': "+123456789",
            'From': "+987654321",
        }
        
        self.holodeck.assert_has_request(Request(
            'post',
            'https://conversations.twilio.com/v1/Conversations/CVaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Participants',
            data=values,
        ))

    def test_create_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "address": "torkel2@ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.endpoint.twilio.com",
                "conversation_sid": "CVaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "date_created": "2015-05-13T23:03:12Z",
                "duration": 685,
                "end_time": "2015-05-13T23:14:40Z",
                "sid": "PAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "start_time": "2015-05-13T23:03:15Z",
                "status": "disconnected",
                "url": "https://conversations.twilio.com/v1/Conversations/CVaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Participants/PAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
            }
            '''
        ))
        
        actual = self.client.conversations.v1.conversations(sid="CVaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                             .participants.create(to="+123456789", from_="+987654321")
        
        self.assertIsNotNone(actual)

    def test_fetch_request(self):
        self.holodeck.mock(Response(500, ''))
        
        with self.assertRaises(TwilioException):
            self.client.conversations.v1.conversations(sid="CVaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                        .participants(sid="PAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa").fetch()
        
        self.holodeck.assert_has_request(Request(
            'get',
            'https://conversations.twilio.com/v1/Conversations/CVaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Participants/PAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa',
        ))

    def test_fetch_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "address": "torkel2@ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.endpoint.twilio.com",
                "conversation_sid": "CVaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "date_created": "2015-05-13T23:03:12Z",
                "duration": 685,
                "end_time": "2015-05-13T23:14:40Z",
                "sid": "PAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "start_time": "2015-05-13T23:03:15Z",
                "status": "disconnected",
                "url": "https://conversations.twilio.com/v1/Conversations/CVaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Participants/PAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
            }
            '''
        ))
        
        actual = self.client.conversations.v1.conversations(sid="CVaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                             .participants(sid="PAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa").fetch()
        
        self.assertIsNotNone(actual)
