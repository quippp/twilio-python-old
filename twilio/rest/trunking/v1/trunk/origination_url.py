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


class OriginationUrlList(ListResource):

    def __init__(self, version, trunk_sid):
        """
        Initialize the OriginationUrlList
        
        :param Version version: Version that contains the resource
        :param trunk_sid: The trunk_sid
        
        :returns: OriginationUrlList
        :rtype: OriginationUrlList
        """
        super(OriginationUrlList, self).__init__(version)
        
        # Path Solution
        self._solution = {
            'trunk_sid': trunk_sid,
        }
        self._uri = '/Trunks/{trunk_sid}/OriginationUrls'.format(**self._solution)

    def create(self, weight, priority, enabled, friendly_name, sip_url):
        """
        Create a new OriginationUrlInstance
        
        :param unicode weight: The weight
        :param unicode priority: The priority
        :param bool enabled: The enabled
        :param unicode friendly_name: The friendly_name
        :param unicode sip_url: The sip_url
        
        :returns: Newly created OriginationUrlInstance
        :rtype: OriginationUrlInstance
        """
        data = values.of({
            'Weight': weight,
            'Priority': priority,
            'Enabled': enabled,
            'FriendlyName': friendly_name,
            'SipUrl': sip_url,
        })
        
        payload = self._version.create(
            'POST',
            self._uri,
            data=data,
        )
        
        return OriginationUrlInstance(
            self._version,
            payload,
            trunk_sid=self._solution['trunk_sid'],
        )

    def stream(self, limit=None, page_size=None):
        """
        Streams OriginationUrlInstance records from the API as a generator stream.
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
        Lists OriginationUrlInstance records from the API as a list.
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
        Retrieve a single page of OriginationUrlInstance records from the API.
        Request is executed immediately
        
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50
        
        :returns: Page of OriginationUrlInstance
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
        
        return OriginationUrlPage(
            self._version,
            response,
            trunk_sid=self._solution['trunk_sid'],
        )

    def get(self, sid):
        """
        Constructs a OriginationUrlContext
        
        :param sid: The sid
        
        :returns: OriginationUrlContext
        :rtype: OriginationUrlContext
        """
        return OriginationUrlContext(
            self._version,
            trunk_sid=self._solution['trunk_sid'],
            sid=sid,
        )

    def __call__(self, sid):
        """
        Constructs a OriginationUrlContext
        
        :param sid: The sid
        
        :returns: OriginationUrlContext
        :rtype: OriginationUrlContext
        """
        return OriginationUrlContext(
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
        return '<Twilio.Trunking.V1.OriginationUrlList>'


class OriginationUrlPage(Page):

    def __init__(self, version, response, trunk_sid):
        """
        Initialize the OriginationUrlPage
        
        :param Version version: Version that contains the resource
        :param Response response: Response from the API
        :param trunk_sid: The trunk_sid
        
        :returns: OriginationUrlPage
        :rtype: OriginationUrlPage
        """
        super(OriginationUrlPage, self).__init__(version, response)
        
        # Path Solution
        self._solution = {
            'trunk_sid': trunk_sid,
        }

    def get_instance(self, payload):
        """
        Build an instance of OriginationUrlInstance
        
        :param dict payload: Payload response from the API
        
        :returns: OriginationUrlInstance
        :rtype: OriginationUrlInstance
        """
        return OriginationUrlInstance(
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
        return '<Twilio.Trunking.V1.OriginationUrlPage>'


class OriginationUrlContext(InstanceContext):

    def __init__(self, version, trunk_sid, sid):
        """
        Initialize the OriginationUrlContext
        
        :param Version version: Version that contains the resource
        :param trunk_sid: The trunk_sid
        :param sid: The sid
        
        :returns: OriginationUrlContext
        :rtype: OriginationUrlContext
        """
        super(OriginationUrlContext, self).__init__(version)
        
        # Path Solution
        self._solution = {
            'trunk_sid': trunk_sid,
            'sid': sid,
        }
        self._uri = '/Trunks/{trunk_sid}/OriginationUrls/{sid}'.format(**self._solution)

    def fetch(self):
        """
        Fetch a OriginationUrlInstance
        
        :returns: Fetched OriginationUrlInstance
        :rtype: OriginationUrlInstance
        """
        params = values.of({})
        
        payload = self._version.fetch(
            'GET',
            self._uri,
            params=params,
        )
        
        return OriginationUrlInstance(
            self._version,
            payload,
            trunk_sid=self._solution['trunk_sid'],
            sid=self._solution['sid'],
        )

    def delete(self):
        """
        Deletes the OriginationUrlInstance
        
        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete('delete', self._uri)

    def update(self, weight=values.unset, priority=values.unset,
               enabled=values.unset, friendly_name=values.unset,
               sip_url=values.unset):
        """
        Update the OriginationUrlInstance
        
        :param unicode weight: The weight
        :param unicode priority: The priority
        :param bool enabled: The enabled
        :param unicode friendly_name: The friendly_name
        :param unicode sip_url: The sip_url
        
        :returns: Updated OriginationUrlInstance
        :rtype: OriginationUrlInstance
        """
        data = values.of({
            'Weight': weight,
            'Priority': priority,
            'Enabled': enabled,
            'FriendlyName': friendly_name,
            'SipUrl': sip_url,
        })
        
        payload = self._version.update(
            'POST',
            self._uri,
            data=data,
        )
        
        return OriginationUrlInstance(
            self._version,
            payload,
            trunk_sid=self._solution['trunk_sid'],
            sid=self._solution['sid'],
        )

    def __repr__(self):
        """
        Provide a friendly representation
        
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Trunking.V1.OriginationUrlContext {}>'.format(context)


class OriginationUrlInstance(InstanceResource):

    def __init__(self, version, payload, trunk_sid, sid=None):
        """
        Initialize the OriginationUrlInstance
        
        :returns: OriginationUrlInstance
        :rtype: OriginationUrlInstance
        """
        super(OriginationUrlInstance, self).__init__(version)
        
        # Marshaled Properties
        self._properties = {
            'account_sid': payload['account_sid'],
            'sid': payload['sid'],
            'trunk_sid': payload['trunk_sid'],
            'weight': deserialize.integer(payload['weight']),
            'enabled': payload['enabled'],
            'sip_url': payload['sip_url'],
            'friendly_name': payload['friendly_name'],
            'priority': deserialize.integer(payload['priority']),
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
        
        :returns: OriginationUrlContext for this OriginationUrlInstance
        :rtype: OriginationUrlContext
        """
        if self._context is None:
            self._context = OriginationUrlContext(
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
    def weight(self):
        """
        :returns: The weight
        :rtype: unicode
        """
        return self._properties['weight']

    @property
    def enabled(self):
        """
        :returns: The enabled
        :rtype: bool
        """
        return self._properties['enabled']

    @property
    def sip_url(self):
        """
        :returns: The sip_url
        :rtype: unicode
        """
        return self._properties['sip_url']

    @property
    def friendly_name(self):
        """
        :returns: The friendly_name
        :rtype: unicode
        """
        return self._properties['friendly_name']

    @property
    def priority(self):
        """
        :returns: The priority
        :rtype: unicode
        """
        return self._properties['priority']

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
        Fetch a OriginationUrlInstance
        
        :returns: Fetched OriginationUrlInstance
        :rtype: OriginationUrlInstance
        """
        return self._proxy.fetch()

    def delete(self):
        """
        Deletes the OriginationUrlInstance
        
        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._proxy.delete()

    def update(self, weight=values.unset, priority=values.unset,
               enabled=values.unset, friendly_name=values.unset,
               sip_url=values.unset):
        """
        Update the OriginationUrlInstance
        
        :param unicode weight: The weight
        :param unicode priority: The priority
        :param bool enabled: The enabled
        :param unicode friendly_name: The friendly_name
        :param unicode sip_url: The sip_url
        
        :returns: Updated OriginationUrlInstance
        :rtype: OriginationUrlInstance
        """
        return self._proxy.update(
            weight=weight,
            priority=priority,
            enabled=enabled,
            friendly_name=friendly_name,
            sip_url=sip_url,
        )

    def __repr__(self):
        """
        Provide a friendly representation
        
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Trunking.V1.OriginationUrlInstance {}>'.format(context)
