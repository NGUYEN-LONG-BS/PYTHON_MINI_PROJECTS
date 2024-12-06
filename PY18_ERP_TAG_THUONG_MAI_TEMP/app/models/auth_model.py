class AuthModel:
    def authenticate(self, username, password):
        # Check if the username and password match
        # In a real-world scenario, this would query a database
        if username == "admin" and password == "password":
            return True
        return False

    def register(self, username, email, password):
        # Example of a registration process, could be a database insert
        print(f"User {username} registered with email {email}")
        return True
