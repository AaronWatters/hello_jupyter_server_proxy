
# Based on
# https://github.com/innovationOUtside/nb_serverproxy_openrefine/blob/main/nb_serverproxy_openrefine/__init__.py

import os
from jupyter_server import serverapp

def get_display_url():
    try:
        server = serverapp.ServerApp._instance
        return server.display_url
    except Exception as e:
        return repr(e)

icon_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'icons', 'logo.svg')

def setup_hello_server():
    return {
        'command': ['async_hello_world_server', '{port}', '{base_url}', get_display_url()],
        'environment': {},
        'launcher_entry': {
            'title': 'HelloServer',
            'icon_path': icon_path,
        }
    }

