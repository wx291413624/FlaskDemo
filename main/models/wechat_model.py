from . import db
from sqlalchemy import CHAR, Column, DECIMAL, DateTime, Enum, Float, String, TIMESTAMP, Text, text
from sqlalchemy.dialects.mysql import BIGINT, INTEGER, TINYINT


class WechatMaterial(db.Model):
    __tablename__ = 'wechat_material'

    id = Column(INTEGER(11), primary_key=True, unique=True)
    media_id = Column(Text)
    url = Column(Text)
    material_type = Column(Text)
    type = Column(INTEGER(11))
    create_time = Column(TIMESTAMP)
    desc = Column(Text)
    key = Column(Text)
    state = Column(INTEGER(11))
    is_use = Column(INTEGER(11))

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update_commit(self):
        db.session.commit()
