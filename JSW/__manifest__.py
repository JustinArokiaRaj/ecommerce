# -*- coding: utf-8 -*-
{
    'name': "Theme JSW",
    'summary': """ The Ultimate Theme""",
    'author':"AgaramSoft",
    'description': """
        Theme by AgaramSoft Team
    """,
    'website': "https://agaramtechs.com",
    'version': '1.0',
    'depends': ['crm', 'base', 'mail','website'],
    'qweb': [
        "static/src/xml/*.xml",
    ],
    'data': [
        'views/assets.xml',
        'views/navbar.xml',
        'views/home_default.xml',
        'views/contactus.xml',
    ],
}
