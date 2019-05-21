# coding: utf-8
from sqlalchemy import CHAR, Column, DECIMAL, DateTime, Enum, Float, String, TIMESTAMP, Text, text
from sqlalchemy.dialects.mysql import BIGINT, INTEGER, TINYINT
from sqlalchemy.ext.declarative import declarative_base

from . import db


class Balance(db.Model):
    __tablename__ = 'balance'

    id = Column(INTEGER(11), primary_key=True, unique=True)
    user_id = Column(INTEGER(11))
    sum = Column(INTEGER(11))
    surplus = Column(INTEGER(11))
    create_time = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    update_time = Column(TIMESTAMP)


class Bank(db.Model):
    __tablename__ = 'bank'

    id = Column(INTEGER(11), primary_key=True, unique=True)
    user_id = Column(INTEGER(11))
    real_name = Column(String(255))
    crad = Column(String(255))
    id_crad = Column(String(255))
    phone = Column(String(255))
    branch = Column(String(255))


class BlanceDetail(db.Model):
    __tablename__ = 'blance_detail'

    id = Column(INTEGER(11), primary_key=True, unique=True)
    user_id = Column(String(255))
    money = Column(INTEGER(11))
    type = Column(String(255))
    circulation = Column(String(255))
    create_time = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    resource = Column(String(255))
    resource_id = Column(String(255))


class CCityDictionary(db.Model):
    __tablename__ = 'c_city_dictionary'

    id = Column(INTEGER(11), primary_key=True)
    citycode = Column(INTEGER(11), index=True)
    province_num = Column(INTEGER(11))
    city_num = Column(INTEGER(11))
    county_num = Column(INTEGER(11))
    name = Column(String(20))
    num_level = Column(INTEGER(11))
    longitude = Column(Float(asdecimal=True))
    latitude = Column(Float(asdecimal=True))


class DActivity(db.Model):
    __tablename__ = 'd_activity'

    id = Column(INTEGER(11), primary_key=True, unique=True)
    activity_name = Column(String(255))
    activity_type = Column(String(255))
    activity_type_id = Column(INTEGER(11))


class DGasLabel(db.Model):
    __tablename__ = 'd_gas_label'

    id = Column(INTEGER(11), primary_key=True, unique=True)
    name = Column(String(20))
    name_id = Column(INTEGER(11))
    is_del = Column(TINYINT(1))


class DGasService(db.Model):
    __tablename__ = 'd_gas_service'

    id = Column(INTEGER(11), primary_key=True)
    service_name = Column(String(20))
    service_type_name = Column(String(20))
    service_type_id = Column(INTEGER(11))
    service_abstract = Column(String(100))


class DOilBrand(db.Model):
    __tablename__ = 'd_oil_brand'

    id = Column(INTEGER(11), primary_key=True)
    oil_brand_name = Column(String(255))


class DOilNum(db.Model):
    __tablename__ = 'd_oil_num'

    id = Column(INTEGER(11), primary_key=True)
    oil_num = Column(String(255), nullable=False)
    oil_alias_id = Column(INTEGER(11))
    unit = Column(INTEGER(4))
    unit_name = Column(String(16))


class DPayment(db.Model):
    __tablename__ = 'd_payment'

    id = Column(INTEGER(11), primary_key=True)
    payment_name = Column(String(20))
    payment_type = Column(String(20))
    payment_type_id = Column(INTEGER(11))


class GasActivity(db.Model):
    __tablename__ = 'gas_activity'

    id = Column(INTEGER(11), primary_key=True)
    gas_id = Column(String(50))
    activity_id = Column(String(50))
    activity_title = Column(String(100))
    activity_type = Column(String(20))
    activity_abstract = Column(String(300))
    activity_cope = Column(String(100))
    is_VIP = Column(TINYINT(4))
    is_updated = Column(TINYINT(4))
    start_dt = Column(DateTime)
    end_dt = Column(DateTime)
    update_dt = Column(DateTime)
    create_dt = Column(DateTime)
    version = Column(INTEGER(11), server_default=text("'0'"))
    status = Column(Enum(u'???', u'???'), server_default=text("'???'"))
    is_del = Column(TINYINT(1))


class GasBaseInfo(db.Model):
    __tablename__ = 'gas_base_info'

    id = Column(INTEGER(11), primary_key=True)
    gas_id = Column(String(50))
    gas_name = Column(String(255))
    nick_name = Column(String(32))
    gas_status = Column(INTEGER(4))
    gas_type = Column(String(10))
    gas_brand = Column(String(10))
    gas_address = Column(String(255))
    gas_address_longitude = Column(Float(asdecimal=True))
    gas_address_latitude = Column(Float(asdecimal=True))
    province_code = Column(INTEGER(11))
    province_name = Column(String(32))
    city_code = Column(INTEGER(11))
    city_name = Column(String(32))
    county_code = Column(INTEGER(11))
    county_name = Column(String(32))
    gas_contact = Column(String(255))
    gas_linkman = Column(String(20))
    create_user = Column(String(32))
    update_user = Column(String(32))
    is_del = Column(TINYINT(1))
    isGasoline = Column(TINYINT(4))
    isDieselOil = Column(TINYINT(4))
    isGas = Column(TINYINT(4))
    isSelfService = Column(TINYINT(4))
    update_dt = Column(DateTime)
    create_dt = Column(DateTime)
    version = Column(INTEGER(11))


class GasCardInfo(db.Model):
    __tablename__ = 'gas_card_info'

    id = Column(INTEGER(11), primary_key=True)
    gas_id = Column(String(50))
    type = Column(String(50))
    salesTime = Column(String(50))
    amount = Column(String(50))
    strategies = Column(String(50))
    conditions = Column(String(50))
    is_del = Column(TINYINT(1))
    version = Column(INTEGER(11))


class GasChange(db.Model):
    __tablename__ = 'gas_change'

    id = Column(INTEGER(11), primary_key=True, unique=True)
    task_name = Column(String(255))
    gas_id = Column(INTEGER(11))
    user_id = Column(INTEGER(11))
    user_name = Column(String(255))
    money = Column(DECIMAL(10, 0))
    status = Column(String(10))
    create_time = Column(TIMESTAMP, server_default=text("CURRENT_TIMESTAMP"))
    update_time = Column(TIMESTAMP)
    operate = Column(String(255))
    operate_id = Column(String(255))


class GasNameChange(db.Model):
    __tablename__ = 'gas_name_change'

    id = Column(INTEGER(11), primary_key=True, unique=True)
    gas_id = Column(String(255))
    task_name = Column(String(255))
    oldOil = Column(String(255))
    newOil = Column(String(255))
    money = Column(DECIMAL(10, 0))
    user = Column(String(255))
    user_id = Column(INTEGER(11))
    status = Column(String(255))
    operate = Column(String(255))
    operate_id = Column(INTEGER(11))
    create_time = Column(TIMESTAMP)


class GasOilPrice(db.Model):
    __tablename__ = 'gas_oil_price'

    id = Column(INTEGER(11), primary_key=True)
    gas_id = Column(String(50))
    oil_num_id = Column(INTEGER(11))
    oil_num = Column(String(10))
    oil_type = Column(INTEGER(11))
    price_official = Column(DECIMAL(10, 2))
    unit_name = Column(String(10))
    create_dt = Column(DateTime)
    update_dt = Column(DateTime)
    is_del = Column(TINYINT(1))
    version = Column(INTEGER(11))


class GasPayment(db.Model):
    __tablename__ = 'gas_payment'

    id = Column(INTEGER(11), primary_key=True)
    gas_id = Column(String(50))
    payment_id = Column(INTEGER(11))
    payment_type_id = Column(INTEGER(11))
    payment_name = Column(String(20))
    payment_type_name = Column(String(20))
    is_del = Column(TINYINT(1))
    create_dt = Column(DateTime)
    version = Column(INTEGER(11))


class GasSelfService(db.Model):
    __tablename__ = 'gas_self_service'

    id = Column(INTEGER(11), primary_key=True)
    gas_id = Column(String(50))
    oil_num = Column(String(10))
    is_del = Column(TINYINT(1))
    version = Column(INTEGER(11))


class GasService(db.Model):
    __tablename__ = 'gas_service'

    id = Column(INTEGER(11), primary_key=True)
    gas_id = Column(String(50))
    service_id = Column(INTEGER(11))
    service_type_id = Column(INTEGER(11))
    service_name = Column(String(20))
    service_type_name = Column(String(20))
    is_del = Column(TINYINT(1))
    create_dt = Column(DateTime)
    version = Column(INTEGER(11))


class MqDeadsMessage(db.Model):
    __tablename__ = 'mq_deads_message'

    id = Column(INTEGER(11), primary_key=True)
    message = Column(String(1000))
    exchange = Column(String(255))
    error_desc = Column(Text)
    router = Column(String(255))
    create_date = Column(TIMESTAMP, server_default=text("CURRENT_TIMESTAMP"))


class MqProduceLog0(db.Model):
    __tablename__ = 'mq_produce_log_0'

    id = Column(BIGINT(20), primary_key=True, server_default=text("'0'"))
    exchange_name = Column(String(50))
    router_key = Column(String(100))
    message = Column(String(1024))
    status = Column(Enum(u'WAIT', u'FAIL', u'COMMITED', u'ROLLBACK'))
    create_time = Column(TIMESTAMP, server_default=text("CURRENT_TIMESTAMP"))
    uid = Column(String(50))


class MqProduceLog1(db.Model):
    __tablename__ = 'mq_produce_log_1'

    id = Column(BIGINT(20), primary_key=True, server_default=text("'0'"))
    exchange_name = Column(String(50))
    router_key = Column(String(100))
    message = Column(String(1024))
    status = Column(Enum(u'WAIT', u'FAIL', u'COMMITED', u'ROLLBACK'))
    create_time = Column(TIMESTAMP, server_default=text("CURRENT_TIMESTAMP"))
    uid = Column(String(50))


class MqProduceLog2(db.Model):
    __tablename__ = 'mq_produce_log_2'

    id = Column(BIGINT(20), primary_key=True, server_default=text("'0'"))
    exchange_name = Column(String(50))
    router_key = Column(String(100))
    message = Column(String(1024))
    status = Column(Enum(u'WAIT', u'FAIL', u'COMMITED', u'ROLLBACK'))
    create_time = Column(TIMESTAMP, server_default=text("CURRENT_TIMESTAMP"))
    uid = Column(String(50))


class MqProduceLog3(db.Model):
    __tablename__ = 'mq_produce_log_3'

    id = Column(BIGINT(20), primary_key=True, server_default=text("'0'"))
    exchange_name = Column(String(50))
    router_key = Column(String(100))
    message = Column(String(1024))
    status = Column(Enum(u'WAIT', u'FAIL', u'COMMITED', u'ROLLBACK'))
    create_time = Column(TIMESTAMP, server_default=text("CURRENT_TIMESTAMP"))
    uid = Column(String(50))


class SysDept(db.Model):
    __tablename__ = 'sys_dept'

    DEPT_ID = Column(BIGINT(20), primary_key=True)
    PID = Column(BIGINT(20))
    PIDS = Column(String(512))
    SIMPLE_NAME = Column(String(45))
    FULL_NAME = Column(String(255))
    DESCRIPTION = Column(String(255))
    VERSION = Column(INTEGER(11))
    SORT = Column(INTEGER(11))
    CREATE_TIME = Column(DateTime)
    UPDATE_TIME = Column(DateTime)
    CREATE_USER = Column(BIGINT(20))
    UPDATE_USER = Column(BIGINT(20))


class SysDict(db.Model):
    __tablename__ = 'sys_dict'

    DICT_ID = Column(BIGINT(20), primary_key=True)
    PID = Column(BIGINT(20))
    NAME = Column(String(255))
    CODE = Column(String(255))
    DESCRIPTION = Column(String(255))
    SORT = Column(INTEGER(11))
    CREATE_TIME = Column(DateTime)
    UPDATE_TIME = Column(DateTime)
    CREATE_USER = Column(BIGINT(20))
    UPDATE_USER = Column(BIGINT(20))


class SysFileInfo(db.Model):
    __tablename__ = 'sys_file_info'

    FILE_ID = Column(String(50), primary_key=True)
    FILE_DATA = Column(Text)
    CREATE_TIME = Column(DateTime)
    UPDATE_TIME = Column(DateTime)
    CREATE_USER = Column(BIGINT(20))
    UPDATE_USER = Column(BIGINT(20))


class SysLoginLog(db.Model):
    __tablename__ = 'sys_login_log'

    LOGIN_LOG_ID = Column(BIGINT(20), primary_key=True)
    LOG_NAME = Column(String(255))
    USER_ID = Column(BIGINT(20))
    CREATE_TIME = Column(DateTime)
    SUCCEED = Column(String(255))
    MESSAGE = Column(Text)
    IP_ADDRESS = Column(String(255))


class SysMenu(db.Model):
    __tablename__ = 'sys_menu'

    MENU_ID = Column(BIGINT(20), primary_key=True)
    CODE = Column(String(255))
    PCODE = Column(String(255))
    PCODES = Column(String(255))
    NAME = Column(String(255))
    ICON = Column(String(255))
    URL = Column(String(255))
    SORT = Column(INTEGER(65))
    LEVELS = Column(INTEGER(65))
    MENU_FLAG = Column(String(32))
    DESCRIPTION = Column(String(255))
    STATUS = Column(String(32), server_default=text("'ENABLE'"))
    NEW_PAGE_FLAG = Column(String(32))
    OPEN_FLAG = Column(String(32))
    CREATE_TIME = Column(DateTime)
    UPDATE_TIME = Column(DateTime)
    CREATE_USER = Column(BIGINT(20))
    UPDATE_USER = Column(BIGINT(20))


class SysNotice(db.Model):
    __tablename__ = 'sys_notice'

    NOTICE_ID = Column(BIGINT(20), primary_key=True)
    TITLE = Column(String(255))
    CONTENT = Column(Text)
    CREATE_TIME = Column(DateTime)
    CREATE_USER = Column(BIGINT(20))
    UPDATE_TIME = Column(DateTime)
    UPDATE_USER = Column(BIGINT(20))


class SysOperationLog(db.Model):
    __tablename__ = 'sys_operation_log'

    OPERATION_LOG_ID = Column(BIGINT(20), primary_key=True)
    LOG_TYPE = Column(String(32))
    LOG_NAME = Column(String(255))
    USER_ID = Column(BIGINT(65))
    CLASS_NAME = Column(String(255))
    METHOD = Column(Text)
    CREATE_TIME = Column(DateTime)
    SUCCEED = Column(String(32))
    MESSAGE = Column(Text)


class SysRelation(db.Model):
    __tablename__ = 'sys_relation'

    RELATION_ID = Column(BIGINT(20), primary_key=True)
    MENU_ID = Column(BIGINT(20))
    ROLE_ID = Column(BIGINT(20))


class SysRole(db.Model):
    __tablename__ = 'sys_role'

    ROLE_ID = Column(BIGINT(20), primary_key=True)
    PID = Column(BIGINT(20))
    NAME = Column(String(255))
    DESCRIPTION = Column(String(255))
    SORT = Column(INTEGER(11))
    VERSION = Column(INTEGER(11))
    CREATE_TIME = Column(DateTime)
    UPDATE_TIME = Column(DateTime)
    CREATE_USER = Column(BIGINT(20))
    UPDATE_USER = Column(BIGINT(20))


class SysSmsLog(db.Model):
    __tablename__ = 'sys_sms_log'

    id = Column(INTEGER(11), primary_key=True)
    msg_id = Column(String(32), nullable=False)
    service_code = Column(Enum(u'MARKET', u'NOTICE', u'VERIFY_CODE'), nullable=False)
    service_provider = Column(Enum(u'WEIWANG', u'BAIWU', u'LINGKAI', u'SMAY', u'NEXMO'), nullable=False)
    sys_code = Column(Enum(u'GP_MARKET', u'GP_BAO'), nullable=False)
    mobile = Column(CHAR(15), nullable=False)
    msg_content = Column(Text, nullable=False)
    create_date = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP"))


class SysUser(db.Model):
    __tablename__ = 'sys_user'

    USER_ID = Column(BIGINT(20), primary_key=True)
    AVATAR = Column(String(255))
    ACCOUNT = Column(String(45))
    PASSWORD = Column(String(45))
    SALT = Column(String(45))
    NAME = Column(String(45))
    BIRTHDAY = Column(DateTime)
    SEX = Column(String(32))
    EMAIL = Column(String(45))
    PHONE = Column(String(45))
    ROLE_ID = Column(String(255))
    DEPT_ID = Column(BIGINT(20))
    STATUS = Column(String(32))
    CREATE_TIME = Column(DateTime)
    CREATE_USER = Column(BIGINT(20))
    UPDATE_TIME = Column(DateTime)
    UPDATE_USER = Column(BIGINT(20))
    VERSION = Column(INTEGER(11))


class ErrandsManIdentity(db.Model):
    __tablename__ = 'errands_man_identity'

    id = Column(INTEGER(11), primary_key=True, unique=True)
    user_id = Column(INTEGER(11))
    openid = Column(String(30))
    unionid = Column(String(30))
    errands_name = Column(String(10))
    city = Column(String(10))
    region = Column(String(10))
    street = Column(String(10))
    city_code = Column(String(10))
    region_code = Column(String(10))
    street_code = Column(String(10))
    address = Column(String(200))
    sex = Column(INTEGER(11))
    occupation = Column(String(30))
    create_time = Column(TIMESTAMP)
    update_time = Column(TIMESTAMP)


class User(db.Model):
    __tablename__ = 'user'

    id = Column(INTEGER(11), primary_key=True, unique=True)
    unionid = Column(String(255))
    openid = Column(String(255))
    nick_name = Column(String(255))
    is_errands_man = Column(INTEGER(11))
    head_img_url = Column(String(255))
    sex = Column(String(10))
    phone = Column(String(255))
    create_time = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    update_time = Column(TIMESTAMP)
    is_del = Column(TINYINT(4))

    def save(self):
        db.session.add(self)
        db.session.commit()
        return self

    def to_json(self):
        str_json = {
            "id": self.id,
            "unionid": self.unionid,
            "openid": self.openid,
            "nickName": self.nick_name,
            "headImgUrl": self.head_img_url,
            "sex": self.sex,
            "phone": self.phone,
            "createTime": str(self.create_time),
            "updateTime": str(self.update_time),
            "isDel": self.is_del,
            "isErrandsMan": self.is_errands_man
        }
        return str_json
