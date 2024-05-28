import unittest
from unittest.mock import Mock
from order import Order, NotificationService, SmsSenderService, SmsPasswordGenerator
from colorama import Fore, Style, Back


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
        sms_pass = SmsPasswordGenerator(mob_num='89194562976', password='1375')
        sms_pass.sms_service = mock_sms_sender

        sms_pass.generate_sms_password()

        mock_sms_sender.send_auth_SMS_password.assert_called_once_with('89194562976', 'Ваш пароль для входа: 1375')
        print("Test passed successfully!")

    def test_generate_password_empty_str(self):
        mock_sms_sender = Mock(spec_set=SmsSenderService)
        # фактический результат
        sms_pass = SmsPasswordGenerator(mob_num='', password='')
        sms_pass.sms_service = mock_sms_sender

        sms_pass.generate_sms_password()

        # ожидаемый результат
        mock_sms_sender.send_auth_SMS_password.assert_called_once_with('89194562976', 'Ваш пароль для входа: 1375')

        # try:
        #     mock_sms_sender.send_auth_SMS_password.assert_called_once_with('89194562976', 'Ваш пароль для входа: 1375')
        #
        # except AssertionError:
        #     print(Fore.GREEN + "\nNegative test passed successfully!" + Fore.RESET)
        # else:
        #     print(Fore.RED + "\nMock-object behavior does not correspond to logic. Check the code!" + Fore.RESET)
