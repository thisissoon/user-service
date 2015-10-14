class EmailService(object):
    """ Abstract method for sending emails
    """

    def __init__(self, obj):
        self.obj = obj

    def prepare_payload(self):
        """ Parse self.obj to another object which is understandable for an email
        service
        """
        return None

    def send(self):
        """ Send a request to an email service
        """
        pass


class VerificationEmail(EmailService):

    def set_body(self, object):
        return {
            'key': self.obj.key,
            'username': self.obj.user.username,
            'email': self.obj.user.email
        }
