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


class MessageList(ListResource):

    def __init__(self, version, service_sid, channel_sid):
        """
        Initialize the MessageList
        
        :param Version version: Version that contains the resource
        :param service_sid: The service_sid
        :param channel_sid: The sid
        
        :returns: MessageList
        :rtype: MessageList
        """
        super(MessageList, self).__init__(version)
        
        # Path Solution
        self._solution = {
            'service_sid': service_sid,
            'channel_sid': channel_sid,
        }
        self._uri = '/Services/{service_sid}/Channels/{channel_sid}/Messages'.format(**self._solution)

    def create(self, body, from_=values.unset):
        """
        Create a new MessageInstance
        
        :param unicode body: The body
        :param unicode from_: The from
        
        :returns: Newly created MessageInstance
        :rtype: MessageInstance
        """
        data = values.of({
            'Body': body,
            'From': from_,
        })
        
        payload = self._version.create(
            'POST',
            self._uri,
            data=data,
        )
        
        return MessageInstance(
            self._version,
            payload,
            service_sid=self._solution['service_sid'],
            channel_sid=self._solution['channel_sid'],
        )

    def stream(self, limit=None, page_size=None):
        """
        Streams MessageInstance records from the API as a generator stream.
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
        Lists MessageInstance records from the API as a list.
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
        Retrieve a single page of MessageInstance records from the API.
        Request is executed immediately
        
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50
        
        :returns: Page of MessageInstance
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
        
        return MessagePage(
            self._version,
            response,
            service_sid=self._solution['service_sid'],
            channel_sid=self._solution['channel_sid'],
        )

    def get(self, sid):
        """
        Constructs a MessageContext
        
        :param sid: The sid
        
        :returns: MessageContext
        :rtype: MessageContext
        """
        return MessageContext(
            self._version,
            service_sid=self._solution['service_sid'],
            channel_sid=self._solution['channel_sid'],
            sid=sid,
        )

    def __call__(self, sid):
        """
        Constructs a MessageContext
        
        :param sid: The sid
        
        :returns: MessageContext
        :rtype: MessageContext
        """
        return MessageContext(
            self._version,
            service_sid=self._solution['service_sid'],
            channel_sid=self._solution['channel_sid'],
            sid=sid,
        )

    def __repr__(self):
        """
        Provide a friendly representation
        
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.IpMessaging.V1.MessageList>'


class MessagePage(Page):

    def __init__(self, version, response, service_sid, channel_sid):
        """
        Initialize the MessagePage
        
        :param Version version: Version that contains the resource
        :param Response response: Response from the API
        :param service_sid: The service_sid
        :param channel_sid: The sid
        
        :returns: MessagePage
        :rtype: MessagePage
        """
        super(MessagePage, self).__init__(version, response)
        
        # Path Solution
        self._solution = {
            'service_sid': service_sid,
            'channel_sid': channel_sid,
        }

    def get_instance(self, payload):
        """
        Build an instance of MessageInstance
        
        :param dict payload: Payload response from the API
        
        :returns: MessageInstance
        :rtype: MessageInstance
        """
        return MessageInstance(
            self._version,
            payload,
            service_sid=self._solution['service_sid'],
            channel_sid=self._solution['channel_sid'],
        )

    def __repr__(self):
        """
        Provide a friendly representation
        
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.IpMessaging.V1.MessagePage>'


class MessageContext(InstanceContext):

    def __init__(self, version, service_sid, channel_sid, sid):
        """
        Initialize the MessageContext
        
        :param Version version: Version that contains the resource
        :param service_sid: The service_sid
        :param channel_sid: The channel_sid
        :param sid: The sid
        
        :returns: MessageContext
        :rtype: MessageContext
        """
        super(MessageContext, self).__init__(version)
        
        # Path Solution
        self._solution = {
            'service_sid': service_sid,
            'channel_sid': channel_sid,
            'sid': sid,
        }
        self._uri = '/Services/{service_sid}/Channels/{channel_sid}/Messages/{sid}'.format(**self._solution)

    def fetch(self):
        """
        Fetch a MessageInstance
        
        :returns: Fetched MessageInstance
        :rtype: MessageInstance
        """
        params = values.of({})
        
        payload = self._version.fetch(
            'GET',
            self._uri,
            params=params,
        )
        
        return MessageInstance(
            self._version,
            payload,
            service_sid=self._solution['service_sid'],
            channel_sid=self._solution['channel_sid'],
            sid=self._solution['sid'],
        )

    def __repr__(self):
        """
        Provide a friendly representation
        
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.IpMessaging.V1.MessageContext {}>'.format(context)


class MessageInstance(InstanceResource):

    def __init__(self, version, payload, service_sid, channel_sid, sid=None):
        """
        Initialize the MessageInstance
        
        :returns: MessageInstance
        :rtype: MessageInstance
        """
        super(MessageInstance, self).__init__(version)
        
        # Marshaled Properties
        self._properties = {
            'sid': payload['sid'],
            'account_sid': payload['account_sid'],
            'service_sid': payload['service_sid'],
            'to': payload['to'],
            'date_created': deserialize.iso8601_datetime(payload['date_created']),
            'date_updated': deserialize.iso8601_datetime(payload['date_updated']),
            'was_edited': payload['was_edited'],
            'from_': payload['from'],
            'body': payload['body'],
            'url': payload['url'],
        }
        
        # Context
        self._context = None
        self._solution = {
            'service_sid': service_sid,
            'channel_sid': channel_sid,
            'sid': sid or self._properties['sid'],
        }

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions.  All instance actions are proxied to the context
        
        :returns: MessageContext for this MessageInstance
        :rtype: MessageContext
        """
        if self._context is None:
            self._context = MessageContext(
                self._version,
                service_sid=self._solution['service_sid'],
                channel_sid=self._solution['channel_sid'],
                sid=self._solution['sid'],
            )
        return self._context

    @property
    def sid(self):
        """
        :returns: The sid
        :rtype: unicode
        """
        return self._properties['sid']

    @property
    def account_sid(self):
        """
        :returns: The account_sid
        :rtype: unicode
        """
        return self._properties['account_sid']

    @property
    def service_sid(self):
        """
        :returns: The service_sid
        :rtype: unicode
        """
        return self._properties['service_sid']

    @property
    def to(self):
        """
        :returns: The to
        :rtype: unicode
        """
        return self._properties['to']

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
    def was_edited(self):
        """
        :returns: The was_edited
        :rtype: bool
        """
        return self._properties['was_edited']

    @property
    def from_(self):
        """
        :returns: The from
        :rtype: unicode
        """
        return self._properties['from_']

    @property
    def body(self):
        """
        :returns: The body
        :rtype: unicode
        """
        return self._properties['body']

    @property
    def url(self):
        """
        :returns: The url
        :rtype: unicode
        """
        return self._properties['url']

    def fetch(self):
        """
        Fetch a MessageInstance
        
        :returns: Fetched MessageInstance
        :rtype: MessageInstance
        """
        return self._proxy.fetch()

    def __repr__(self):
        """
        Provide a friendly representation
        
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.IpMessaging.V1.MessageInstance {}>'.format(context)
