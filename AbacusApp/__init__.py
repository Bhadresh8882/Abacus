from flask import Flask, render_template

def create_app():
    app = Flask(__name__,
    static_folder='assets')

    from AbacusApp.blueprints.main.routes import main
    from AbacusApp.blueprints.accounts.routes import accounts
    from AbacusApp.blueprints.services.routes import services

    app.register_blueprint(main)
    app.register_blueprint(accounts)
    app.register_blueprint(services)

    @app.after_request
    def after_request(response):
        response.headers["Chache-Control"] = "no-cache, no-store, must-revalidate"
        return response

    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('error404.html'), 404

    return app