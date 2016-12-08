from pecan import make_app,conf
from test_project import model
from pecan.hooks import TransactionHook

def setup_app(config):

    model.init_model()
    app_conf = dict(config.app)

    return make_app(
        app_conf.pop('root'),
        #static_root = conf.app.static_root,
        #template_path = conf.app.template_path,
        #debug = conf.app.debug,
        #hooks = [
             #TransactionHook(
               # model.start,
               # #model.start_read_only,
               # model.commit,
               # model.rollback,
               # model.clear
             #)
           #],
        logging=getattr(config, 'logging', {}),
        **app_conf
    )
