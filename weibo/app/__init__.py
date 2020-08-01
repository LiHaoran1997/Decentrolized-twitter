# coding=utf-8
from flask import Flask
# import Flask
from flask_bootstrap import Bootstrap
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask import request

from app.blockchain import BlockChain
from config import config
from flask_babel import Babel
from app.extensions import babel
from flask_babel import refresh
from app.extensions import Mode

bootstrap = Bootstrap()
db = SQLAlchemy()
mail = Mail()
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'
blockchain=BlockChain()
onBlockchain = Mode(True)

def create_app(config_name):
    """ 工厂函数，用于创建 app 实例

    :param config_name: 配置类型
    :return: app 实例
    """
    refresh()
    app = Flask(__name__, static_folder='static')
    app.config.from_object(config[config_name])
    bootstrap.init_app(app)
    db.init_app(app)
    mail.init_app(app)
    login_manager.init_app(app)
    babel = Babel(app)
    blockchain.blockChainInitCoin()

    if app.config.get('SSL_DISABLE', None):
        from flask_sslify import SSLify
        sslify = SSLify(app)
    from .main import main as main_buleprint            # 注册 main 蓝图
    from .auth import auth as auth_buleprint            # 注册 auth 蓝图
    from .api_v1_0 import api as api_v1_0_buleprint     # 注册 api_v1.0 蓝图
    app.register_blueprint(main_buleprint)
    app.register_blueprint(auth_buleprint, url_prefix='/auth')  # 所有 url 使用 auth 前缀
    app.register_blueprint(api_v1_0_buleprint, url_prefix='/api/v1.0')
    return app



from app import models
from app.main import views


@babel.localeselector
def get_locale():
    # return request.accept_languages.best_match(config['LANGUAGES'])
    return ' zh_Hans_CN'
