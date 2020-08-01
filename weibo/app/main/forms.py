from flask_login import login_required
from flask_wtf import FlaskForm
from wtforms import (StringField, SubmitField, TextAreaField,
                     BooleanField, SelectField, ValidationError)
from wtforms.validators import DataRequired, Length
from flask_babel import gettext as _
from flask_babel import lazy_gettext as _l

from manage import app
from ..models import Role, User, Post


class PostForm(FlaskForm):
    """
    微博发布表单
    """
    body = TextAreaField(_l('此刻的感想？'), validators=[DataRequired()])
    submit = SubmitField(_l('发布'))


class CommentForm(FlaskForm):
    """
    评论表单
    """
    body = TextAreaField('', validators=[DataRequired()])
    submit = SubmitField(_l('确认'))


class EditProfileForm(FlaskForm):
    """
    用户编辑个人信息表单
    """
    username = StringField(_l('用户名'),
                           validators=[DataRequired(), Length(1, 16)])
    realname = StringField(_l('真实姓名'), validators=[Length(0, 16)])
    sex = SelectField(_l('性别'), choices=[(_l('男'), _l('男')), (_l('女'), _l('女'))], coerce=str)
    location = StringField(_l('地区'), validators=[Length(0, 64)])
    confirmed = BooleanField(_l('保持登陆'))
    about_me = TextAreaField(_l('个人简介'))
    submit = SubmitField(_l('提交'))


class EditProfileAdminForm(FlaskForm):
    """
    管理员编辑个人信息表单
    """
    username = StringField(_l('用户名'),
                           validators=[DataRequired(), Length(1, 16)])
    realname = StringField(_l('真实姓名'), validators=[Length(0, 16)])
    sex = SelectField(_l('性别'), choices=[(_l('男'), _l('男')), (_l('女'), _l('女'))], coerce=str)
    location = StringField(_l('地区'), validators=[Length(0, 64)])
    confirmed = BooleanField(_l('保持登陆'))
    role = SelectField(_l('角色'), coerce=int)
    about_me = TextAreaField(_l('个人简介'))
    submit = SubmitField(_l('提交'))

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 下拉角色选择列表
        self.role.choices = [(role.id, role.name)
                             for role in Role.query.order_by(Role.name).all()]
        self.user = user

    def validate_username(self, filed):
        """ 验证用户名是否已被使用。魔法方法

        :param filed: 用户名数据
        """
        if filed.data != self.user.username and \
                User.query.filter_by(username=filed.data).first():
            raise ValidationError(_l('该用户名已被使用'))


class SearchUserForm(FlaskForm):
    """
    搜索用户表单
    """
    username = StringField(_l('用户名'), validators=[Length(0, 16)])
    submit = SubmitField(_l('搜索'))

