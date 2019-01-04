import logging
import base64
import json
from odoo.addons.mail.controllers.main import MailController
from odoo import http, modules, tools
from odoo.http import request

_logger = logging.getLogger(__name__)


class WebsiteEcommerce(http.Controller):

    @http.route('/', type='http', auth="public")
    def xls_report(self, **kw):
    	print("Hello Dear>>>>>>>>>>>>>>>>>>")
    	return http.request.redirect('/home')