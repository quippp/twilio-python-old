# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /       
"""

from twilio import deserialize
from twilio import values
from twilio.instance_resource import InstanceResource
from twilio.list_resource import ListResource
from twilio.page import Page


class DependentPhoneNumberList(ListResource):

    def __init__(self, version, account_sid, address_sid):
        """
        Initialize the DependentPhoneNumberList
        
        :param Version version: Version that contains the resource
        :param account_sid: The account_sid
        :param address_sid: The sid
        
        :returns: DependentPhoneNumberList
        :rtype: DependentPhoneNumberList
        """
        super(DependentPhoneNumberList, self).__init__(version)
        
        # Path Solution
        self._solution = {
            'account_sid': account_sid,
            'address_sid': address_sid,
        }
        self._uri = '/Accounts/{account_sid}/Addresses/{address_sid}/DependentPhoneNumbers.json'.format(**self._solution)

    def stream(self, limit=None, page_size=None):
        """
        Streams DependentPhoneNumberInstance records from the API as a generator stream.
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
        Lists DependentPhoneNumberInstance records from the API as a list.
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
        Retrieve a single page of DependentPhoneNumberInstance records from the API.
        Request is executed immediately
        
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50
        
        :returns: Page of DependentPhoneNumberInstance
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
        
        return DependentPhoneNumberPage(
            self._version,
            response,
            account_sid=self._solution['account_sid'],
            address_sid=self._solution['address_sid'],
        )

    def __repr__(self):
        """
        Provide a friendly representation
        
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2010.DependentPhoneNumberList>'


class DependentPhoneNumberPage(Page):

    def __init__(self, version, response, account_sid, address_sid):
        """
        Initialize the DependentPhoneNumberPage
        
        :param Version version: Version that contains the resource
        :param Response response: Response from the API
        :param account_sid: The account_sid
        :param address_sid: The sid
        
        :returns: DependentPhoneNumberPage
        :rtype: DependentPhoneNumberPage
        """
        super(DependentPhoneNumberPage, self).__init__(version, response)
        
        # Path Solution
        self._solution = {
            'account_sid': account_sid,
            'address_sid': address_sid,
        }

    def get_instance(self, payload):
        """
        Build an instance of DependentPhoneNumberInstance
        
        :param dict payload: Payload response from the API
        
        :returns: DependentPhoneNumberInstance
        :rtype: DependentPhoneNumberInstance
        """
        return DependentPhoneNumberInstance(
            self._version,
            payload,
            account_sid=self._solution['account_sid'],
            address_sid=self._solution['address_sid'],
        )

    def __repr__(self):
        """
        Provide a friendly representation
        
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2010.DependentPhoneNumberPage>'


class DependentPhoneNumberInstance(InstanceResource):

    def __init__(self, version, payload, account_sid, address_sid):
        """
        Initialize the DependentPhoneNumberInstance
        
        :returns: DependentPhoneNumberInstance
        :rtype: DependentPhoneNumberInstance
        """
        super(DependentPhoneNumberInstance, self).__init__(version)
        
        # Marshaled Properties
        self._properties = {
            'friendly_name': payload['friendly_name'],
            'phone_number': payload['phone_number'],
            'lata': payload['lata'],
            'rate_center': payload['rate_center'],
            'latitude': deserialize.decimal(payload['latitude']),
            'longitude': deserialize.decimal(payload['longitude']),
            'region': payload['region'],
            'postal_code': payload['postal_code'],
            'iso_country': payload['iso_country'],
            'address_requirements': payload['address_requirements'],
            'capabilities': payload['capabilities'],
        }
        
        # Context
        self._context = None
        self._solution = {
            'account_sid': account_sid,
            'address_sid': address_sid,
        }

    @property
    def friendly_name(self):
        """
        :returns: The friendly_name
        :rtype: unicode
        """
        return self._properties['friendly_name']

    @property
    def phone_number(self):
        """
        :returns: The phone_number
        :rtype: unicode
        """
        return self._properties['phone_number']

    @property
    def lata(self):
        """
        :returns: The lata
        :rtype: unicode
        """
        return self._properties['lata']

    @property
    def rate_center(self):
        """
        :returns: The rate_center
        :rtype: unicode
        """
        return self._properties['rate_center']

    @property
    def latitude(self):
        """
        :returns: The latitude
        :rtype: unicode
        """
        return self._properties['latitude']

    @property
    def longitude(self):
        """
        :returns: The longitude
        :rtype: unicode
        """
        return self._properties['longitude']

    @property
    def region(self):
        """
        :returns: The region
        :rtype: unicode
        """
        return self._properties['region']

    @property
    def postal_code(self):
        """
        :returns: The postal_code
        :rtype: unicode
        """
        return self._properties['postal_code']

    @property
    def iso_country(self):
        """
        :returns: The iso_country
        :rtype: unicode
        """
        return self._properties['iso_country']

    @property
    def address_requirements(self):
        """
        :returns: The address_requirements
        :rtype: unicode
        """
        return self._properties['address_requirements']

    @property
    def capabilities(self):
        """
        :returns: The capabilities
        :rtype: unicode
        """
        return self._properties['capabilities']

    def __repr__(self):
        """
        Provide a friendly representation
        
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2010.DependentPhoneNumberInstance>'
