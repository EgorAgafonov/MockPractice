import unittest
from unittest.mock import Mock
from order import Order, NotificationService, SmsSenderService, SmsPasswordGenerator


# class TestOrder(unittest.TestCase):
#     def test_process_order(self):
#         mock_notification_service = Mock(spec_set=NotificationService)
#         order = Order(user_id=123, product_name="Product")
#         order.notification_service = mock_notification_service
#
#         order.process_order()
#
#         mock_notification_service.send_notification.assert_called_once_with(123, "Your order for Product has been "
#                                                                                  "processed.")
#         print("Test passed successfully!")
#
#
# if __name__ == '__main__':
#     unittest.main()

class Test_SmsGenerator(unittest.TestCase):
    def test_generate_sms_password(self):
        mock_sms_sender = Mock(spec_set=SmsSenderService)
        sms_pass = SmsPasswordGenerator(user_id=123, pass_lenght=5)
        sms_pass.sms_service = mock_sms_sender

        sms_pass.generate_sms_password()

        mock_sms_sender.send_auth_SMS_password.assert_called_once_with(123, "Ваш пароль для входа: 64380")
