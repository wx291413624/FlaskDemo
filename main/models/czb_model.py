# coding: utf-8
from sqlalchemy import CHAR, Column, DECIMAL, DateTime, Enum, Float, String, TIMESTAMP, Text, text, Index
from sqlalchemy.dialects.mysql import BIGINT, INTEGER, TINYINT

from main import app
from . import db


class YfqFwGasInfo(db.Model):
    __tablename__ = 'yfq_fw_gas_info'
    __bind_key__ = 'czb'

    id = Column(INTEGER(11), primary_key=True)
    gas_id = Column(String(50), index=True)
    user_id = Column(INTEGER(11))
    company_id = Column(INTEGER(11))
    gas_name = Column(String(255))
    gas_status = Column(INTEGER(4))
    gas_type = Column(String(5))
    gas_logo_big = Column(String(255))
    gas_logo_small = Column(String(255))
    gas_address = Column(String(255))
    gas_address_longitude = Column(Float(asdecimal=True))
    gas_address_latitude = Column(Float(asdecimal=True))
    province_code = Column(INTEGER(11))
    province_name = Column(String(32))
    city_code = Column(INTEGER(11))
    city_name = Column(String(32))
    county_code = Column(INTEGER(11))
    county_name = Column(String(32))
    gas_phone = Column(String(15))
    gas_star = Column(Float(2))
    gas_order_num = Column(INTEGER(11))
    gas_evaluation_num = Column(INTEGER(11))
    gas_join_dt = Column(DateTime)
    create_dt = Column(DateTime)
    time_settlement = Column(String(50))
    gas_discount = Column(DECIMAL(10, 2))
    activity_type = Column(INTEGER(5))
    gas_owner_name = Column(String(32))
    gas_owner_mobile = Column(String(20))
    gas_finance_name = Column(String(32))
    gas_finance_mobile = Column(String(20))
    gas_manager_name = Column(String(32))
    gas_manager_mobile = Column(String(20))
    nick_name = Column(String(32))
    check_status = Column(INTEGER(4))
    update_dt = Column(DateTime)
    check_dt = Column(DateTime)
    check_user = Column(String(32))
    create_user = Column(String(32))
    update_user = Column(String(32))
    is_activity = Column(INTEGER(11))
    settlement_type = Column(INTEGER(4))
    is_old_area = Column(INTEGER(4), server_default=text("'0'"))
    check_remark = Column(String(500))
    is_test = Column(INTEGER(4), server_default=text("'0'"))
    is_pre_deposit = Column(INTEGER(4), server_default=text("'0'"))
    channel_fee = Column(DECIMAL(10, 5), server_default=text("'0.00000'"))
    business_licence = Column(String(1000))
    account_licence = Column(String(1000))
    invoice_sample = Column(String(1000))
    paid = Column(INTEGER(11), server_default=text("'0'"))
    energy_chain = Column(INTEGER(11), server_default=text("'0'"))
    pay_way = Column(INTEGER(11), server_default=text("'0'"))
    settlement = Column(INTEGER(11), server_default=text("'0'"))
    discount = Column(INTEGER(11), server_default=text("'0'"))
    display_list = Column(String(32))
    platform_list = Column(String(500))
    no_limit_platform_list = Column(String(500))
    invoice_flag = Column(INTEGER(4))
    market_flag = Column(INTEGER(4), server_default=text("'1'"))
    national_flag = Column(INTEGER(4), server_default=text("'1'"))
    switch_time = Column(DateTime)
    invoice_ratio = Column(DECIMAL(10, 5))

    def find_sum(self, lat, lng):
        str_sql = """select d.gas_address_longitude                         lng,
                           d.gas_address_latitude                          lat,
                           round(6378.138 * 2 * asin(sqrt(pow(sin((d.gas_address_latitude * pi() / 180 - """ + str(lat) + """ * pi() / 180) / 2), 2) +
                                                          cos(d.gas_address_latitude * pi() / 180) * cos(""" + str(lat) + """ * pi() / 180) *
                                                          pow(sin((d.gas_address_longitude * pi() / 180 - """ + str(lng) + """ * pi() / 180) / 2),
                                                              2))) * 1000) distance,
                           d.gas_name,
                           d.gas_id,
                           c.oil_no,
                           c.price_official,
                           c.price_activity,
                           c.price_gun,
                           c.price_yfq
                  from yfq_fw_gas_info d
                         left join yfq_fw_oil_price c on d.gas_id = c.gas_id
                  where c.oil_no = 95
                    AND c.status = 1
                    and c.check_status = 1
                    and c.rebate_base = 1
                    and round(6378.138 * 2 * asin(sqrt(pow(sin((d.gas_address_latitude * pi() / 180 - """ + str(lat) + """  * pi() / 180) / 2), 2) +
                                     cos(d.gas_address_latitude * pi() / 180) * cos(""" + str(lat) + """  * pi() / 180) *
                                     pow(sin((d.gas_address_longitude * pi() / 180 -""" + str(lng) + """  * pi() / 180) / 2),
                                         2))) * 1000) <= 20000
                  order by distance ASC"""
        xy = db.session.execute(str_sql, bind=db.get_engine(app, bind='czb')).fetchall()
        return xy


class YfqFwOilPrice(db.Model):
    __tablename__ = 'yfq_fw_oil_price'
    __bind_key__ = 'czb'

    id = Column(INTEGER(11), primary_key=True)
    oil_no = Column(INTEGER(3))
    gas_id = Column(String(50), index=True)
    price_official = Column(DECIMAL(10, 2))
    price_yfq = Column(DECIMAL(10, 2))
    price_gun = Column(DECIMAL(10, 2))
    price_activity = Column(DECIMAL(10, 2))
    rebate = Column(DECIMAL(10, 4))
    last_user_id = Column(INTEGER(11))
    create_dt = Column(DateTime)
    update_dt = Column(DateTime)
    percent = Column(INTEGER(11))
    unit = Column(INTEGER(4))
    unit_name = Column(String(16))
    remark = Column(String(200))
    status = Column(INTEGER(4), server_default=text("'1'"))
    check_status = Column(INTEGER(4), server_default=text("'1'"))
    rebate_base = Column(INTEGER(3), nullable=False)
    rebate_official = Column(DECIMAL(10, 4))
    czb_price_rule = Column(INTEGER(3), nullable=False)
    b_price_yfq = Column(DECIMAL(10, 2))
    b_rebate = Column(DECIMAL(11, 2))
    c_rebate = Column(DECIMAL(11, 2))
