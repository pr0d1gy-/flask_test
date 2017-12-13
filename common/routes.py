from common.views import MainView


def register_routes(blueprint):
    blueprint.add_url_rule('/', view_func=MainView.as_view('main'))
