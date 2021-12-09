"""HTTP handler to shut down the Jupyter server.
"""
from tornado import ioloop
from tornado import web

from jupyter_server.base.handlers import JupyterHandler
from jupyter_server.services.auth.decorator import authorized


AUTH_RESOURCE = "server"


class ShutdownHandler(JupyterHandler):
    auth_resource = AUTH_RESOURCE

    @web.authenticated
    @authorized
    async def post(self):
        self.log.info("Shutting down on /api/shutdown request.")

        await self.serverapp._cleanup()

        ioloop.IOLoop.current().stop()


default_handlers = [
    (r"/api/shutdown", ShutdownHandler),
]
