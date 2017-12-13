from profile.views import LogoutView, LoginView, RegistrationView


def register_routes(blueprint):
    blueprint.add_url_rule(
        '/logout', view_func=LogoutView.as_view('logout'))
    blueprint.add_url_rule(
        '/login', view_func=LoginView.as_view('login'))
    blueprint.add_url_rule(
        '/registration', view_func=RegistrationView.as_view('registration'))
