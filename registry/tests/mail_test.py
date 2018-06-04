import unittest
from unittest import mock
from unittest.mock import patch

from .utils import QuiltTestCase

from quilt_server import app
from quilt_server.models import User
from quilt_server.mail import (send_new_user_email, send_invitation_email,
    send_activation_email, send_reset_email)

class MailTestCase(QuiltTestCase):

    def setUp(self):
        super(MailTestCase, self).setUp()

    @patch('quilt_server.mail.send_email')
    def testTemplates(self, send_email):
        # just make sure all templates work
        test_user = User.get_by_name(self.TEST_USER)
        with app.app_context():
            send_new_user_email(self.TEST_USER, self.TEST_USER_EMAIL)
            send_invitation_email(self.TEST_USER_EMAIL, self.OTHER_USER, 'test')
            send_reset_email(test_user, 'test')
            send_activation_email(test_user, 'test')
        pass
