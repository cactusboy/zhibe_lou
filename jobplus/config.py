class BaseConfig(object):
    SECRET_KEY = 'SECRET'
    JOB_PER_PAGE = 9
    COMPANY_PER_PAGE = 12

class DevelopmentConfig(BaseConfig):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "mysql://root@localhost:3306/jobplus?charset=utf8"

class ProductionConfig(BaseConfig):
    pass

class TestingConfig(BaseConfig):
    pass

configs = {
        'development': DevelopmentConfig,
        'production': ProductionConfig,
        'testing': TestingConfig
        }

