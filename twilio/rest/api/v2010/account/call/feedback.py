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


class FeedbackList(ListResource):

    def __init__(self, version, account_sid, call_sid):
        """
        Initialize the FeedbackList
        
        :param Version version: Version that contains the resource
        :param account_sid: The account_sid
        :param call_sid: A 34 character string that uniquely identifies this resource.
        
        :returns: FeedbackList
        :rtype: FeedbackList
        """
        super(FeedbackList, self).__init__(version)
        
        # Path Solution
        self._solution = {
            'account_sid': account_sid,
            'call_sid': call_sid,
        }

    def get(self):
        """
        Constructs a FeedbackContext
        
        :returns: FeedbackContext
        :rtype: FeedbackContext
        """
        return FeedbackContext(
            self._version,
            account_sid=self._solution['account_sid'],
            call_sid=self._solution['call_sid'],
        )

    def __call__(self):
        """
        Constructs a FeedbackContext
        
        :returns: FeedbackContext
        :rtype: FeedbackContext
        """
        return FeedbackContext(
            self._version,
            account_sid=self._solution['account_sid'],
            call_sid=self._solution['call_sid'],
        )

    def __repr__(self):
        """
        Provide a friendly representation
        
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2010.FeedbackList>'


class FeedbackPage(Page):

    def __init__(self, version, response, account_sid, call_sid):
        """
        Initialize the FeedbackPage
        
        :param Version version: Version that contains the resource
        :param Response response: Response from the API
        :param account_sid: The account_sid
        :param call_sid: A 34 character string that uniquely identifies this resource.
        
        :returns: FeedbackPage
        :rtype: FeedbackPage
        """
        super(FeedbackPage, self).__init__(version, response)
        
        # Path Solution
        self._solution = {
            'account_sid': account_sid,
            'call_sid': call_sid,
        }

    def get_instance(self, payload):
        """
        Build an instance of FeedbackInstance
        
        :param dict payload: Payload response from the API
        
        :returns: FeedbackInstance
        :rtype: FeedbackInstance
        """
        return FeedbackInstance(
            self._version,
            payload,
            account_sid=self._solution['account_sid'],
            call_sid=self._solution['call_sid'],
        )

    def __repr__(self):
        """
        Provide a friendly representation
        
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2010.FeedbackPage>'


class FeedbackContext(InstanceContext):

    def __init__(self, version, account_sid, call_sid):
        """
        Initialize the FeedbackContext
        
        :param Version version: Version that contains the resource
        :param account_sid: The account_sid
        :param call_sid: The call sid that uniquely identifies the call
        
        :returns: FeedbackContext
        :rtype: FeedbackContext
        """
        super(FeedbackContext, self).__init__(version)
        
        # Path Solution
        self._solution = {
            'account_sid': account_sid,
            'call_sid': call_sid,
        }
        self._uri = '/Accounts/{account_sid}/Calls/{call_sid}/Feedback.json'.format(**self._solution)

    def create(self, quality_score, issue=values.unset):
        """
        Create a new FeedbackInstance
        
        :param unicode quality_score: The quality_score
        :param feedback.issues issue: The issue
        
        :returns: Newly created FeedbackInstance
        :rtype: FeedbackInstance
        """
        data = values.of({
            'QualityScore': quality_score,
            'Issue': issue,
        })
        
        payload = self._version.create(
            'POST',
            self._uri,
            data=data,
        )
        
        return FeedbackInstance(
            self._version,
            payload,
            account_sid=self._solution['account_sid'],
            call_sid=self._solution['call_sid'],
        )

    def fetch(self):
        """
        Fetch a FeedbackInstance
        
        :returns: Fetched FeedbackInstance
        :rtype: FeedbackInstance
        """
        params = values.of({})
        
        payload = self._version.fetch(
            'GET',
            self._uri,
            params=params,
        )
        
        return FeedbackInstance(
            self._version,
            payload,
            account_sid=self._solution['account_sid'],
            call_sid=self._solution['call_sid'],
        )

    def update(self, quality_score, issue=values.unset):
        """
        Update the FeedbackInstance
        
        :param unicode quality_score: An integer from 1 to 5
        :param feedback.issues issue: Issues experienced during the call
        
        :returns: Updated FeedbackInstance
        :rtype: FeedbackInstance
        """
        data = values.of({
            'QualityScore': quality_score,
            'Issue': issue,
        })
        
        payload = self._version.update(
            'POST',
            self._uri,
            data=data,
        )
        
        return FeedbackInstance(
            self._version,
            payload,
            account_sid=self._solution['account_sid'],
            call_sid=self._solution['call_sid'],
        )

    def __repr__(self):
        """
        Provide a friendly representation
        
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Api.V2010.FeedbackContext {}>'.format(context)


class FeedbackInstance(InstanceResource):

    def __init__(self, version, payload, account_sid, call_sid):
        """
        Initialize the FeedbackInstance
        
        :returns: FeedbackInstance
        :rtype: FeedbackInstance
        """
        super(FeedbackInstance, self).__init__(version)
        
        # Marshaled Properties
        self._properties = {
            'account_sid': payload['account_sid'],
            'date_created': deserialize.rfc2822_datetime(payload['date_created']),
            'date_updated': deserialize.rfc2822_datetime(payload['date_updated']),
            'issues': payload['issues'],
            'quality_score': deserialize.integer(payload['quality_score']),
            'sid': payload['sid'],
        }
        
        # Context
        self._context = None
        self._solution = {
            'account_sid': account_sid,
            'call_sid': call_sid,
        }

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions.  All instance actions are proxied to the context
        
        :returns: FeedbackContext for this FeedbackInstance
        :rtype: FeedbackContext
        """
        if self._context is None:
            self._context = FeedbackContext(
                self._version,
                account_sid=self._solution['account_sid'],
                call_sid=self._solution['call_sid'],
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
    def issues(self):
        """
        :returns: The issues
        :rtype: feedback.issues
        """
        return self._properties['issues']

    @property
    def quality_score(self):
        """
        :returns: 1 to 5 quality score
        :rtype: unicode
        """
        return self._properties['quality_score']

    @property
    def sid(self):
        """
        :returns: The sid
        :rtype: unicode
        """
        return self._properties['sid']

    def create(self, quality_score, issue=values.unset):
        """
        Create a new FeedbackInstance
        
        :param unicode quality_score: The quality_score
        :param feedback.issues issue: The issue
        
        :returns: Newly created FeedbackInstance
        :rtype: FeedbackInstance
        """
        return self._proxy.create(
            quality_score,
            issue=issue,
        )

    def fetch(self):
        """
        Fetch a FeedbackInstance
        
        :returns: Fetched FeedbackInstance
        :rtype: FeedbackInstance
        """
        return self._proxy.fetch()

    def update(self, quality_score, issue=values.unset):
        """
        Update the FeedbackInstance
        
        :param unicode quality_score: An integer from 1 to 5
        :param feedback.issues issue: Issues experienced during the call
        
        :returns: Updated FeedbackInstance
        :rtype: FeedbackInstance
        """
        return self._proxy.update(
            quality_score,
            issue=issue,
        )

    def __repr__(self):
        """
        Provide a friendly representation
        
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Api.V2010.FeedbackInstance {}>'.format(context)
