# hello_jupyter_server_proxy
Hello world example of an async web server hosted using jupyter server proxy

# Experimental install

```bash
cd hello_jupyter_server_proxy
pip install -e .
```

# Purpose

This repository provides a minimal example of a 
<a href="https://jupyter-server-proxy.readthedocs.io/en/latest/index.html">
Jupyter server proxy implementation.
</a>
I hope this example will be useful to help people like me
set up more realistic instances of proxy servers.

Below is an outline of the different files in the repository
and their purpose.

# ./bin/async_hello_world_server

This executable script
that starts a trivial "hello world" web server
on a given port.  It is installed as a command line script.

```bash
$ async_hello_world_server 9876 my_base
```

The above starts the server using port 9876 with a "base url" value `my_base`.
The port and base url are passed from the Jupyter server during initialization.

# ./hello_jupyter_server_proxy/async_hello_server.py

This is the Python implementation of the trivial web server.

# ./setup.py

This is the standard setup script for the module.  It installs the
`async_hello_world_server` script.  It also specifies the
an entry point for the module called `jupyter_serverproxy_servers`

```
    'helloServer = hello_jupyter_server_proxy:setup_hello_server'
```

When the Jupyter server starts up it scans the Python installation for these
entry points and uses them to set up proxy server plugins.

# ./hello_jupyter_server_proxy/__init__.py

This is the module initialer file which imports the `setup_hello_server`
function so it can be accessed as `hello_jupyter_server_proxy.setup_hello_server`
by the Jupyter server.

# ./hello_jupyter_server_proxy/jupyter_configuration.py

This file defines the configuration parameters for the plugin.
It specifies the command format for starting the server using
the command line script
```
    'command': ['async_hello_world_server', '{port}', '{base_url}'],
```
and also indicates where to find the icon for the server.

# ./hello_jupyter_server_proxy/icons/logo.svg

This is the icon for the server used by JupyterLab.  Only SVG format
is supported.

# ./hello_jupyter_server_proxy/icons/dog.png

This is the image I wanted to use as an icon, but it's not supported.
