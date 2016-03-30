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


class TaskQueuesStatisticsTestCase(IntegrationTestCase):

    def test_list_request(self):
        self.holodeck.mock(Response(500, ''))
        
        with self.assertRaises(TwilioException):
            self.client.taskrouter.v1.workspaces(sid="WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                     .task_queues \
                                     .statistics.list()
        
        self.holodeck.assert_has_request(Request(
            'get',
            'https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/TaskQueues/Statistics',
        ))

    def test_read_full_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "meta": {
                    "first_page_url": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/TaskQueues/Statistics?PageSize=50&Page=0",
                    "key": "task_queues_statistics",
                    "next_page_url": null,
                    "page": 0,
                    "page_size": 50,
                    "previous_page_url": null,
                    "url": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/TaskQueues/Statistics?PageSize=50&Page=0"
                },
                "task_queues_statistics": [
                    {
                        "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "cumulative": {
                            "avg_task_acceptance_time": 0.0,
                            "end_time": "2015-08-18T00:46:15Z",
                            "reservations_accepted": 0,
                            "reservations_canceled": 0,
                            "reservations_created": 0,
                            "reservations_rejected": 0,
                            "reservations_rescinded": 0,
                            "reservations_timed_out": 0,
                            "start_time": "2015-08-18T00:31:15Z",
                            "tasks_canceled": 0,
                            "tasks_deleted": 0,
                            "tasks_entered": 0,
                            "tasks_moved": 0
                        },
                        "realtime": {
                            "activity_statistics": [
                                {
                                    "friendly_name": "Offline",
                                    "sid": "WAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                                    "workers": 0
                                },
                                {
                                    "friendly_name": "Idle",
                                    "sid": "WAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                                    "workers": 0
                                },
                                {
                                    "friendly_name": "80fa2beb-3a05-11e5-8fc8-98e0d9a1eb73",
                                    "sid": "WAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                                    "workers": 0
                                },
                                {
                                    "friendly_name": "Reserved",
                                    "sid": "WAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                                    "workers": 0
                                },
                                {
                                    "friendly_name": "Busy",
                                    "sid": "WAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                                    "workers": 0
                                },
                                {
                                    "friendly_name": "817ca1c5-3a05-11e5-9292-98e0d9a1eb73",
                                    "sid": "WAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                                    "workers": 0
                                }
                            ],
                            "longest_task_waiting_age": 0,
                            "longest_task_waiting_sid": null,
                            "tasks_by_status": {
                                "assigned": 0,
                                "pending": 0,
                                "reserved": 0
                            },
                            "total_available_workers": 0,
                            "total_eligible_workers": 0,
                            "total_tasks": 0
                        },
                        "task_queue_sid": "WQaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "workspace_sid": "WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                    }
                ]
            }
            '''
        ))
        
        actual = self.client.taskrouter.v1.workspaces(sid="WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                          .task_queues \
                                          .statistics.list()
        
        self.assertIsNotNone(actual)

    def test_read_empty_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "meta": {
                    "first_page_url": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/TaskQueues/Statistics?PageSize=50&Page=0",
                    "key": "task_queues_statistics",
                    "next_page_url": null,
                    "page": 0,
                    "page_size": 50,
                    "previous_page_url": null,
                    "url": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/TaskQueues/Statistics?PageSize=50&Page=0"
                },
                "task_queues_statistics": []
            }
            '''
        ))
        
        actual = self.client.taskrouter.v1.workspaces(sid="WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                          .task_queues \
                                          .statistics.list()
        
        self.assertIsNotNone(actual)
