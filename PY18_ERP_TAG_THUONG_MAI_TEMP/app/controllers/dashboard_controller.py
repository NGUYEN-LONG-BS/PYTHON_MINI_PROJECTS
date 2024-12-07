class DashboardController:
    def __init__(self, dashboard_view, dashboard_model):
        self.dashboard_view = dashboard_view
        self.dashboard_model = dashboard_model
        self.dashboard_view.set_controller(self)

    def load_dashboard_data(self):
        data = self.dashboard_model.get_data()
        self.dashboard_view.update_view(data)
