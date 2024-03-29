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


class ValidationRequestList(ListResource):

    def __init__(self, version, account_sid):
        """
        Initialize the ValidationRequestList
        
        :param Version version: Version that contains the resource
        :param account_sid: The account_sid
        
        :returns: ValidationRequestList
        :rtype: ValidationRequestList
        """
        super(ValidationRequestList, self).__init__(version)
        
        # Path Solution
        self._solution = {
            'account_sid': account_sid,
        }
        self._uri = '/Accounts/{account_sid}/OutgoingCallerIds.json'.format(**self._solution)

    def create(self, phone_number, friendly_name=values.unset,
               call_delay=values.unset, extension=values.unset,
               status_callback=values.unset, status_callback_method=values.unset):
        """
        Create a new ValidationRequestInstance
        
        :param unicode phone_number: The phone_number
        :param unicode friendly_name: The friendly_name
        :param unicode call_delay: The call_delay
        :param unicode extension: The extension
        :param unicode status_callback: The status_callback
        :param unicode status_callback_method: The status_callback_method
        
        :returns: Newly created ValidationRequestInstance
        :rtype: ValidationRequestInstance
        """
        data = values.of({
            'PhoneNumber': phone_number,
            'FriendlyName': friendly_name,
            'CallDelay': call_delay,
            'Extension': extension,
            'StatusCallback': status_callback,
            'StatusCallbackMethod': status_callback_method,
        })
        
        payload = self._version.create(
            'POST',
            self._uri,
            data=data,
        )
        
        return ValidationRequestInstance(
            self._version,
            payload,
            account_sid=self._solution['account_sid'],
        )

    def __repr__(self):
        """
        Provide a friendly representation
        
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2010.ValidationRequestList>'


class ValidationRequestPage(Page):

    def __init__(self, version, response, account_sid):
        """
        Initialize the ValidationRequestPage
        
        :param Version version: Version that contains the resource
        :param Response response: Response from the API
        :param account_sid: The account_sid
        
        :returns: ValidationRequestPage
        :rtype: ValidationRequestPage
        """
        super(ValidationRequestPage, self).__init__(version, response)
        
        # Path Solution
        self._solution = {
            'account_sid': account_sid,
        }

    def get_instance(self, payload):
        """
        Build an instance of ValidationRequestInstance
        
        :param dict payload: Payload response from the API
        
        :returns: ValidationRequestInstance
        :rtype: ValidationRequestInstance
        """
        return ValidationRequestInstance(
            self._version,
            payload,
            account_sid=self._solution['account_sid'],
        )

    def __repr__(self):
        """
        Provide a friendly representation
        
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2010.ValidationRequestPage>'


class ValidationRequestInstance(InstanceResource):

    def __init__(self, version, payload, account_sid):
        """
        Initialize the ValidationRequestInstance
        
        :returns: ValidationRequestInstance
        :rtype: ValidationRequestInstance
        """
        super(ValidationRequestInstance, self).__init__(version)
        
        # Marshaled Properties
        self._properties = {
            'account_sid': payload['account_sid'],
            'phone_number': payload['phone_number'],
            'friendly_name': payload['friendly_name'],
            'validation_code': deserialize.integer(payload['validation_code']),
            'call_sid': payload['call_sid'],
        }
        
        # Context
        self._context = None
        self._solution = {
            'account_sid': account_sid,
        }

    @property
    def account_sid(self):
        """
        :returns: The account_sid
        :rtype: unicode
        """
        return self._properties['account_sid']

    @property
    def phone_number(self):
        """
        :returns: The phone_number
        :rtype: unicode
        """
        return self._properties['phone_number']

    @property
    def friendly_name(self):
        """
        :returns: The friendly_name
        :rtype: unicode
        """
        return self._properties['friendly_name']

    @property
    def validation_code(self):
        """
        :returns: The validation_code
        :rtype: unicode
        """
        return self._properties['validation_code']

    @property
    def call_sid(self):
        """
        :returns: The call_sid
        :rtype: unicode
        """
        return self._properties['call_sid']

    def __repr__(self):
        """
        Provide a friendly representation
        
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2010.ValidationRequestInstance>'
