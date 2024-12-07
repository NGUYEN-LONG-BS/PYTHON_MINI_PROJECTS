class Notification:
    def __init__(self, user_id, message, notification_type, is_read=False):
        self.user_id = user_id
        self.message = message
        self.notification_type = notification_type  # e.g., 'message', 'alert', 'reminder'
        self.is_read = is_read
        
    def mark_as_read(self):
        self.is_read = True
