from jupyter_server.services.auth.authorizer import Authorizer


class ReadOnly(Authorizer):
    """Authorizer that makes Jupyter Server a read-only server."""

    def is_authorized(self, handler, user, action, resource):
        """Only allows `read` operations."""
        if action != "read":
            return False
        return True


c.ServerApp.authorizer_class = ReadOnly
