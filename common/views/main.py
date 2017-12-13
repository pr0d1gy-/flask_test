from flask.views import MethodView
from flask import render_template


class MainView(MethodView):

    def get(self):
        return render_template('common/main.html')
