import setuptools

# based on https://github.com/ryanlovett/jupyter-shiny-proxy

setuptools.setup(
    name="hello_jupyter_server_proxy",
    version='0.1',
    url="https://github.com/AaronWatters/hello_jupyter_server_proxy",
    author="Aaron Watters",
    description="Jupyter extension to proxy hello world web server",
    packages=[
        'hello_jupyter_server_proxy'
    ],
	keywords=['Jupyter'],
	classifiers=['Framework :: Jupyter'],
    install_requires=[
        'jupyter-server-proxy',
        "aiohttp",
    ],
    entry_points={
        'jupyter_serverproxy_servers': [
            'helloServer = hello_jupyter_server_proxy:setup_hello_server'
        ]
    },
    package_data={
        'hello_jupyter_server_proxy': ['icons/dog.png', 'icons/logo.svg'],
    },
    scripts = [
        "bin/async_hello_world_server",
    ],
)
