### encoding: utf-8 ###

import ayah

from flask import current_app, Markup

from flask import _request_ctx_stack as stack


class AreYouAHuman(object):

    def __init__(self, app = None, **kwargs):

        if app:
            self.init_app(app, **kwargs)

    def init_app(self, app):

        self.ayah = ayah
        self.ayah.configure(app.config['AYAH_PUBLISHER'], app.config['AYAH_SCORING'])

        app.jinja_env.globals['ayah_get_publisher_html'] = self.get_publisher_html

    def get_publisher_html(self):
        return Markup(self.ayah.get_publisher_html())

    def score_result(self):
        ctx = stack.top
        if ctx is not None:
            return self.ayah.score_result(ctx.request.form['session_secret'])
        

