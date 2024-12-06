class AuthController:
    def __init__(self, login_view, register_view, auth_model):
        self.login_view = login_view
        self.register_view = register_view
        self.auth_model = auth_model
        
        # Binding the views to the controller
        self.login_view.set_controller(self)
        self.register_view.set_controller(self)

    def login(self, username, password):
        if self.auth_model.authenticate(username, password):
            print("Login Successful")
        else:
            print("Login Failed")

    def register(self, username, email, password):
        if self.auth_model.register(username, email, password):
            print("Registration Successful")
        else:
            print("Registration Failed")
