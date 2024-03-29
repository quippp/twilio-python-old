# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /       
"""

from twilio import deserialize
from twilio import values
from twilio.instance_context import InstanceContext
from twilio.instance_resource import InstanceResource
from twilio.list_resource import ListResource
from twilio.page import Page
from twilio.rest.taskrouter.v1.workspace.workflow.workflow_statistics import WorkflowStatisticsList


class WorkflowList(ListResource):

    def __init__(self, version, workspace_sid):
        """
        Initialize the WorkflowList
        
        :param Version version: Version that contains the resource
        :param workspace_sid: The workspace_sid
        
        :returns: WorkflowList
        :rtype: WorkflowList
        """
        super(WorkflowList, self).__init__(version)
        
        # Path Solution
        self._solution = {
            'workspace_sid': workspace_sid,
        }
        self._uri = '/Workspaces/{workspace_sid}/Workflows'.format(**self._solution)

    def stream(self, friendly_name=values.unset, limit=None, page_size=None):
        """
        Streams WorkflowInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.
        
        :param unicode friendly_name: The friendly_name
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)
        
        :returns: Generator that will yield up to limit results
        :rtype: generator
        """
        limits = self._version.read_limits(limit, page_size)
        
        page = self.page(
            friendly_name=friendly_name,
            page_size=limits['page_size'],
        )
        
        return self._version.stream(page, limits['limit'], limits['page_limit'])

    def list(self, friendly_name=values.unset, limit=None, page_size=None):
        """
        Lists WorkflowInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.
        
        :param unicode friendly_name: The friendly_name
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)
        
        :returns: Generator that will yield up to limit results
        :rtype: generator
        """
        return list(self.stream(
            friendly_name=friendly_name,
            limit=limit,
            page_size=page_size,
        ))

    def page(self, friendly_name=values.unset, page_token=values.unset,
             page_number=values.unset, page_size=values.unset):
        """
        Retrieve a single page of WorkflowInstance records from the API.
        Request is executed immediately
        
        :param unicode friendly_name: The friendly_name
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50
        
        :returns: Page of WorkflowInstance
        :rtype: Page
        """
        params = values.of({
            'FriendlyName': friendly_name,
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })
        
        response = self._version.page(
            'GET',
            self._uri,
            params=params,
        )
        
        return WorkflowPage(
            self._version,
            response,
            workspace_sid=self._solution['workspace_sid'],
        )

    def create(self, friendly_name, configuration, assignment_callback_url,
               fallback_assignment_callback_url=values.unset,
               task_reservation_timeout=values.unset):
        """
        Create a new WorkflowInstance
        
        :param unicode friendly_name: The friendly_name
        :param unicode configuration: The configuration
        :param unicode assignment_callback_url: The assignment_callback_url
        :param unicode fallback_assignment_callback_url: The fallback_assignment_callback_url
        :param unicode task_reservation_timeout: The task_reservation_timeout
        
        :returns: Newly created WorkflowInstance
        :rtype: WorkflowInstance
        """
        data = values.of({
            'FriendlyName': friendly_name,
            'Configuration': configuration,
            'AssignmentCallbackUrl': assignment_callback_url,
            'FallbackAssignmentCallbackUrl': fallback_assignment_callback_url,
            'TaskReservationTimeout': task_reservation_timeout,
        })
        
        payload = self._version.create(
            'POST',
            self._uri,
            data=data,
        )
        
        return WorkflowInstance(
            self._version,
            payload,
            workspace_sid=self._solution['workspace_sid'],
        )

    def get(self, sid):
        """
        Constructs a WorkflowContext
        
        :param sid: The sid
        
        :returns: WorkflowContext
        :rtype: WorkflowContext
        """
        return WorkflowContext(
            self._version,
            workspace_sid=self._solution['workspace_sid'],
            sid=sid,
        )

    def __call__(self, sid):
        """
        Constructs a WorkflowContext
        
        :param sid: The sid
        
        :returns: WorkflowContext
        :rtype: WorkflowContext
        """
        return WorkflowContext(
            self._version,
            workspace_sid=self._solution['workspace_sid'],
            sid=sid,
        )

    def __repr__(self):
        """
        Provide a friendly representation
        
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Taskrouter.V1.WorkflowList>'


class WorkflowPage(Page):

    def __init__(self, version, response, workspace_sid):
        """
        Initialize the WorkflowPage
        
        :param Version version: Version that contains the resource
        :param Response response: Response from the API
        :param workspace_sid: The workspace_sid
        
        :returns: WorkflowPage
        :rtype: WorkflowPage
        """
        super(WorkflowPage, self).__init__(version, response)
        
        # Path Solution
        self._solution = {
            'workspace_sid': workspace_sid,
        }

    def get_instance(self, payload):
        """
        Build an instance of WorkflowInstance
        
        :param dict payload: Payload response from the API
        
        :returns: WorkflowInstance
        :rtype: WorkflowInstance
        """
        return WorkflowInstance(
            self._version,
            payload,
            workspace_sid=self._solution['workspace_sid'],
        )

    def __repr__(self):
        """
        Provide a friendly representation
        
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Taskrouter.V1.WorkflowPage>'


class WorkflowContext(InstanceContext):

    def __init__(self, version, workspace_sid, sid):
        """
        Initialize the WorkflowContext
        
        :param Version version: Version that contains the resource
        :param workspace_sid: The workspace_sid
        :param sid: The sid
        
        :returns: WorkflowContext
        :rtype: WorkflowContext
        """
        super(WorkflowContext, self).__init__(version)
        
        # Path Solution
        self._solution = {
            'workspace_sid': workspace_sid,
            'sid': sid,
        }
        self._uri = '/Workspaces/{workspace_sid}/Workflows/{sid}'.format(**self._solution)
        
        # Dependents
        self._statistics = None

    def fetch(self):
        """
        Fetch a WorkflowInstance
        
        :returns: Fetched WorkflowInstance
        :rtype: WorkflowInstance
        """
        params = values.of({})
        
        payload = self._version.fetch(
            'GET',
            self._uri,
            params=params,
        )
        
        return WorkflowInstance(
            self._version,
            payload,
            workspace_sid=self._solution['workspace_sid'],
            sid=self._solution['sid'],
        )

    def update(self, friendly_name=values.unset,
               assignment_callback_url=values.unset,
               fallback_assignment_callback_url=values.unset,
               configuration=values.unset, task_reservation_timeout=values.unset):
        """
        Update the WorkflowInstance
        
        :param unicode friendly_name: The friendly_name
        :param unicode assignment_callback_url: The assignment_callback_url
        :param unicode fallback_assignment_callback_url: The fallback_assignment_callback_url
        :param unicode configuration: The configuration
        :param unicode task_reservation_timeout: The task_reservation_timeout
        
        :returns: Updated WorkflowInstance
        :rtype: WorkflowInstance
        """
        data = values.of({
            'FriendlyName': friendly_name,
            'AssignmentCallbackUrl': assignment_callback_url,
            'FallbackAssignmentCallbackUrl': fallback_assignment_callback_url,
            'Configuration': configuration,
            'TaskReservationTimeout': task_reservation_timeout,
        })
        
        payload = self._version.update(
            'POST',
            self._uri,
            data=data,
        )
        
        return WorkflowInstance(
            self._version,
            payload,
            workspace_sid=self._solution['workspace_sid'],
            sid=self._solution['sid'],
        )

    def delete(self):
        """
        Deletes the WorkflowInstance
        
        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete('delete', self._uri)

    @property
    def statistics(self):
        """
        Access the statistics
        
        :returns: WorkflowStatisticsList
        :rtype: WorkflowStatisticsList
        """
        if self._statistics is None:
            self._statistics = WorkflowStatisticsList(
                self._version,
                workspace_sid=self._solution['workspace_sid'],
                workflow_sid=self._solution['sid'],
            )
        return self._statistics

    def __repr__(self):
        """
        Provide a friendly representation
        
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Taskrouter.V1.WorkflowContext {}>'.format(context)


class WorkflowInstance(InstanceResource):

    def __init__(self, version, payload, workspace_sid, sid=None):
        """
        Initialize the WorkflowInstance
        
        :returns: WorkflowInstance
        :rtype: WorkflowInstance
        """
        super(WorkflowInstance, self).__init__(version)
        
        # Marshaled Properties
        self._properties = {
            'account_sid': payload['account_sid'],
            'assignment_callback_url': payload['assignment_callback_url'],
            'configuration': payload['configuration'],
            'date_created': deserialize.iso8601_datetime(payload['date_created']),
            'date_updated': deserialize.iso8601_datetime(payload['date_updated']),
            'document_content_type': payload['document_content_type'],
            'fallback_assignment_callback_url': payload['fallback_assignment_callback_url'],
            'friendly_name': payload['friendly_name'],
            'sid': payload['sid'],
            'task_reservation_timeout': deserialize.integer(payload['task_reservation_timeout']),
            'workspace_sid': payload['workspace_sid'],
        }
        
        # Context
        self._context = None
        self._solution = {
            'workspace_sid': workspace_sid,
            'sid': sid or self._properties['sid'],
        }

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions.  All instance actions are proxied to the context
        
        :returns: WorkflowContext for this WorkflowInstance
        :rtype: WorkflowContext
        """
        if self._context is None:
            self._context = WorkflowContext(
                self._version,
                workspace_sid=self._solution['workspace_sid'],
                sid=self._solution['sid'],
            )
        return self._context

    @property
    def account_sid(self):
        """
        :returns: The account_sid
        :rtype: unicode
        """
        return self._properties['account_sid']

    @property
    def assignment_callback_url(self):
        """
        :returns: The assignment_callback_url
        :rtype: unicode
        """
        return self._properties['assignment_callback_url']

    @property
    def configuration(self):
        """
        :returns: The configuration
        :rtype: unicode
        """
        return self._properties['configuration']

    @property
    def date_created(self):
        """
        :returns: The date_created
        :rtype: datetime
        """
        return self._properties['date_created']

    @property
    def date_updated(self):
        """
        :returns: The date_updated
        :rtype: datetime
        """
        return self._properties['date_updated']

    @property
    def document_content_type(self):
        """
        :returns: The document_content_type
        :rtype: unicode
        """
        return self._properties['document_content_type']

    @property
    def fallback_assignment_callback_url(self):
        """
        :returns: The fallback_assignment_callback_url
        :rtype: unicode
        """
        return self._properties['fallback_assignment_callback_url']

    @property
    def friendly_name(self):
        """
        :returns: The friendly_name
        :rtype: unicode
        """
        return self._properties['friendly_name']

    @property
    def sid(self):
        """
        :returns: The sid
        :rtype: unicode
        """
        return self._properties['sid']

    @property
    def task_reservation_timeout(self):
        """
        :returns: The task_reservation_timeout
        :rtype: unicode
        """
        return self._properties['task_reservation_timeout']

    @property
    def workspace_sid(self):
        """
        :returns: The workspace_sid
        :rtype: unicode
        """
        return self._properties['workspace_sid']

    def fetch(self):
        """
        Fetch a WorkflowInstance
        
        :returns: Fetched WorkflowInstance
        :rtype: WorkflowInstance
        """
        return self._proxy.fetch()

    def update(self, friendly_name=values.unset,
               assignment_callback_url=values.unset,
               fallback_assignment_callback_url=values.unset,
               configuration=values.unset, task_reservation_timeout=values.unset):
        """
        Update the WorkflowInstance
        
        :param unicode friendly_name: The friendly_name
        :param unicode assignment_callback_url: The assignment_callback_url
        :param unicode fallback_assignment_callback_url: The fallback_assignment_callback_url
        :param unicode configuration: The configuration
        :param unicode task_reservation_timeout: The task_reservation_timeout
        
        :returns: Updated WorkflowInstance
        :rtype: WorkflowInstance
        """
        return self._proxy.update(
            friendly_name=friendly_name,
            assignment_callback_url=assignment_callback_url,
            fallback_assignment_callback_url=fallback_assignment_callback_url,
            configuration=configuration,
            task_reservation_timeout=task_reservation_timeout,
        )

    def delete(self):
        """
        Deletes the WorkflowInstance
        
        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._proxy.delete()

    @property
    def statistics(self):
        """
        Access the statistics
        
        :returns: statistics
        :rtype: statistics
        """
        return self._proxy.statistics

    def __repr__(self):
        """
        Provide a friendly representation
        
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Taskrouter.V1.WorkflowInstance {}>'.format(context)
