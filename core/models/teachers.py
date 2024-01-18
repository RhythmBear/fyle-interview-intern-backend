from core import db
from core.apis.decorators import AuthPrincipal
from core.libs import helpers, assertions
from core import db


class Teacher(db.Model):
    __tablename__ = 'teachers'
    id = db.Column(db.Integer, db.Sequence('teachers_id_seq'), primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    created_at = db.Column(db.TIMESTAMP(timezone=True), default=helpers.get_utc_now, nullable=False)
    updated_at = db.Column(db.TIMESTAMP(timezone=True), default=helpers.get_utc_now, nullable=False, onupdate=helpers.get_utc_now)

    def __repr__(self):
        return '<Teacher %r>' % self.id
    
    @staticmethod
    def get_all_teachers(auth_principal: AuthPrincipal):

        assertions.assert_valid(auth_principal.principal_id is not None, 'only principals can make this request.')
        return Teacher.query.all()
