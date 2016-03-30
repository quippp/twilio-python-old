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


class WorkerStatisticsTestCase(IntegrationTestCase):

    def test_fetch_request(self):
        self.holodeck.mock(Response(500, ''))
        
        with self.assertRaises(TwilioException):
            self.client.taskrouter.v1.workspaces(sid="WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                     .workers(sid="WKaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                     .statistics().fetch()
        
        self.holodeck.assert_has_request(Request(
            'get',
            'https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Workers/WKaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Statistics',
        ))

    def test_fetch_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "cumulative": {
                    "activity_durations": [
                        {
                            "avg": 0.0,
                            "friendly_name": "80fa2beb-3a05-11e5-8fc8-98e0d9a1eb73",
                            "max": 0,
                            "min": 0,
                            "sid": "WAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                            "total": 0
                        },
                        {
                            "avg": 0.0,
                            "friendly_name": "817ca1c5-3a05-11e5-9292-98e0d9a1eb73",
                            "max": 0,
                            "min": 0,
                            "sid": "WAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                            "total": 0
                        },
                        {
                            "avg": 0.0,
                            "friendly_name": "Busy",
                            "max": 0,
                            "min": 0,
                            "sid": "WAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                            "total": 0
                        },
                        {
                            "avg": 0.0,
                            "friendly_name": "Idle",
                            "max": 0,
                            "min": 0,
                            "sid": "WAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                            "total": 0
                        },
                        {
                            "avg": 0.0,
                            "friendly_name": "Offline",
                            "max": 0,
                            "min": 0,
                            "sid": "WAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                            "total": 0
                        },
                        {
                            "avg": 0.0,
                            "friendly_name": "Reserved",
                            "max": 0,
                            "min": 0,
                            "sid": "WAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                            "total": 0
                        }
                    ],
                    "end_time": "2015-08-18T16:36:19Z",
                    "reservations_accepted": 0,
                    "reservations_canceled": 0,
                    "reservations_created": 0,
                    "reservations_rejected": 0,
                    "reservations_rescinded": 0,
                    "reservations_timed_out": 0,
                    "start_time": "2015-08-18T16:21:19Z",
                    "tasks_assigned": 0
                },
                "worker_sid": "WKaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "workspace_sid": "WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
            }
            '''
        ))
        
        actual = self.client.taskrouter.v1.workspaces(sid="WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                          .workers(sid="WKaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                          .statistics().fetch()
        
        self.assertIsNotNone(actual)
