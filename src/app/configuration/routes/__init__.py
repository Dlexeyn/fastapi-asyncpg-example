from app.configuration.routes.routes import Routes
from app.internal.routes import heroes

__routes__ = Routes(routes=(heroes.router, ))
