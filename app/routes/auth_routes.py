from flask import Blueprint

auth_routes = Blueprint('auth_routes', __name__)

# Add your routes here
@auth_routes.route('/some-auth-route', methods=['GET'])
def some_auth_route():
    return "Auth route working!"
