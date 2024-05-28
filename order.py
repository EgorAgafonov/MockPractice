import random


class NotificationService:
    def send_notification(self, user_id, message):
        # Код для отправки уведомления
        pass


class Order:
    def __init__(self, user_id, product_name):
        self.user_id = user_id
        self.product_name = product_name
        self.notification_service = NotificationService()

    def process_order(self):
        # Обработка заказа
        message = f"Your order for {self.product_name} has been processed."
        self.notification_service.send_notification(self.user_id, message)


class SmsSenderService:
    def send_auth_SMS_password(self, user_id, message):
        pass


class SmsPasswordGenerator:
    def __init__(self, user_id, pass_lenght):
        self.user_id = user_id
        self.pass_lenght = pass_lenght
        self.sms_service = SmsSenderService()

    def generate_sms_password(self):
        sms_pass = []
        for i in range(0, self.pass_lenght):
            rand_num = str(random.randrange(0, 10))
            sms_pass.append(rand_num)
        result = ''.join(sms_pass)
        message = f"Ваш пароль для входа: {result}"
        self.sms_service.send_auth_SMS_password(self.user_id, message)


