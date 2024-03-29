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


class CredentialListList(ListResource):

    def __init__(self, version, trunk_sid):
        """
        Initialize the CredentialListList
        
        :param Version version: Version that contains the resource
        :param trunk_sid: The trunk_sid
        
        :returns: CredentialListList
        :rtype: CredentialListList
        """
        super(CredentialListList, self).__init__(version)
        
        # Path Solution
        self._solution = {
            'trunk_sid': trunk_sid,
        }
        self._uri = '/Trunks/{trunk_sid}/CredentialLists'.format(**self._solution)

    def create(self, credential_list_sid):
        """
        Create a new CredentialListInstance
        
        :param unicode credential_list_sid: The credential_list_sid
        
        :returns: Newly created CredentialListInstance
        :rtype: CredentialListInstance
        """
        data = values.of({
            'CredentialListSid': credential_list_sid,
        })
        
        payload = self._version.create(
            'POST',
            self._uri,
            data=data,
        )
        
        return CredentialListInstance(
            self._version,
            payload,
            trunk_sid=self._solution['trunk_sid'],
        )

    def stream(self, limit=None, page_size=None):
        """
        Streams CredentialListInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.
        
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
            page_size=limits['page_size'],
        )
        
        return self._version.stream(page, limits['limit'], limits['page_limit'])

    def list(self, limit=None, page_size=None):
        """
        Lists CredentialListInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.
        
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
            limit=limit,
            page_size=page_size,
        ))

    def page(self, page_token=values.unset, page_number=values.unset,
             page_size=values.unset):
        """
        Retrieve a single page of CredentialListInstance records from the API.
        Request is executed immediately
        
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50
        
        :returns: Page of CredentialListInstance
        :rtype: Page
        """
        params = values.of({
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })
        
        response = self._version.page(
            'GET',
            self._uri,
            params=params,
        )
        
        return CredentialListPage(
            self._version,
            response,
            trunk_sid=self._solution['trunk_sid'],
        )

    def get(self, sid):
        """
        Constructs a CredentialListContext
        
        :param sid: The sid
        
        :returns: CredentialListContext
        :rtype: CredentialListContext
        """
        return CredentialListContext(
            self._version,
            trunk_sid=self._solution['trunk_sid'],
            sid=sid,
        )

    def __call__(self, sid):
        """
        Constructs a CredentialListContext
        
        :param sid: The sid
        
        :returns: CredentialListContext
        :rtype: CredentialListContext
        """
        return CredentialListContext(
            self._version,
            trunk_sid=self._solution['trunk_sid'],
            sid=sid,
        )

    def __repr__(self):
        """
        Provide a friendly representation
        
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Trunking.V1.CredentialListList>'


class CredentialListPage(Page):

    def __init__(self, version, response, trunk_sid):
        """
        Initialize the CredentialListPage
        
        :param Version version: Version that contains the resource
        :param Response response: Response from the API
        :param trunk_sid: The trunk_sid
        
        :returns: CredentialListPage
        :rtype: CredentialListPage
        """
        super(CredentialListPage, self).__init__(version, response)
        
        # Path Solution
        self._solution = {
            'trunk_sid': trunk_sid,
        }

    def get_instance(self, payload):
        """
        Build an instance of CredentialListInstance
        
        :param dict payload: Payload response from the API
        
        :returns: CredentialListInstance
        :rtype: CredentialListInstance
        """
        return CredentialListInstance(
            self._version,
            payload,
            trunk_sid=self._solution['trunk_sid'],
        )

    def __repr__(self):
        """
        Provide a friendly representation
        
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Trunking.V1.CredentialListPage>'


class CredentialListContext(InstanceContext):

    def __init__(self, version, trunk_sid, sid):
        """
        Initialize the CredentialListContext
        
        :param Version version: Version that contains the resource
        :param trunk_sid: The trunk_sid
        :param sid: The sid
        
        :returns: CredentialListContext
        :rtype: CredentialListContext
        """
        super(CredentialListContext, self).__init__(version)
        
        # Path Solution
        self._solution = {
            'trunk_sid': trunk_sid,
            'sid': sid,
        }
        self._uri = '/Trunks/{trunk_sid}/CredentialLists/{sid}'.format(**self._solution)

    def fetch(self):
        """
        Fetch a CredentialListInstance
        
        :returns: Fetched CredentialListInstance
        :rtype: CredentialListInstance
        """
        params = values.of({})
        
        payload = self._version.fetch(
            'GET',
            self._uri,
            params=params,
        )
        
        return CredentialListInstance(
            self._version,
            payload,
            trunk_sid=self._solution['trunk_sid'],
            sid=self._solution['sid'],
        )

    def delete(self):
        """
        Deletes the CredentialListInstance
        
        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete('delete', self._uri)

    def __repr__(self):
        """
        Provide a friendly representation
        
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Trunking.V1.CredentialListContext {}>'.format(context)


class CredentialListInstance(InstanceResource):

    def __init__(self, version, payload, trunk_sid, sid=None):
        """
        Initialize the CredentialListInstance
        
        :returns: CredentialListInstance
        :rtype: CredentialListInstance
        """
        super(CredentialListInstance, self).__init__(version)
        
        # Marshaled Properties
        self._properties = {
            'account_sid': payload['account_sid'],
            'sid': payload['sid'],
            'trunk_sid': payload['trunk_sid'],
            'friendly_name': payload['friendly_name'],
            'date_created': deserialize.iso8601_datetime(payload['date_created']),
            'date_updated': deserialize.iso8601_datetime(payload['date_updated']),
            'url': payload['url'],
        }
        
        # Context
        self._context = None
        self._solution = {
            'trunk_sid': trunk_sid,
            'sid': sid or self._properties['sid'],
        }

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions.  All instance actions are proxied to the context
        
        :returns: CredentialListContext for this CredentialListInstance
        :rtype: CredentialListContext
        """
        if self._context is None:
            self._context = CredentialListContext(
                self._version,
                trunk_sid=self._solution['trunk_sid'],
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
    def sid(self):
        """
        :returns: The sid
        :rtype: unicode
        """
        return self._properties['sid']

    @property
    def trunk_sid(self):
        """
        :returns: The trunk_sid
        :rtype: unicode
        """
        return self._properties['trunk_sid']

    @property
    def friendly_name(self):
        """
        :returns: The friendly_name
        :rtype: unicode
        """
        return self._properties['friendly_name']

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
    def url(self):
        """
        :returns: The url
        :rtype: unicode
        """
        return self._properties['url']

    def fetch(self):
        """
        Fetch a CredentialListInstance
        
        :returns: Fetched CredentialListInstance
        :rtype: CredentialListInstance
        """
        return self._proxy.fetch()

    def delete(self):
        """
        Deletes the CredentialListInstance
        
        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._proxy.delete()

    def __repr__(self):
        """
        Provide a friendly representation
        
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Trunking.V1.CredentialListInstance {}>'.format(context)
