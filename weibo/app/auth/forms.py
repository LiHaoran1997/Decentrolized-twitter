from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import (DataRequired, Length, Email,
                                EqualTo, ValidationError)

from ..models import User
from flask_babel import gettext as _
from flask_babel import lazy_gettext as _l


class LoginForm(FlaskForm):
    """
    登录表单
    """
    email = StringField(_l('邮箱'),
                        validators=[DataRequired(), Length(1, 64), Email()])
    password = PasswordField(_l('密码'), validators=[DataRequired()])
    remember_me = BooleanField(_l('保持登录状态'))
    submit = SubmitField(_l('登录'))


class RegistrationForm(FlaskForm):
    """
    注册表单
    """
    email = StringField(_l('邮箱'),
                        validators=[DataRequired(), Length(1, 64), Email()])
    username = StringField(_l('用户名'),
                           validators=[DataRequired(), Length(1, 16)])
    password = PasswordField(_l('密码'),
                             validators=[DataRequired(), Length(4, 20),
                                         EqualTo('password_confirm',
                                                 message=_l('两次输入密码不一致'))])
    password_confirm = PasswordField(_l('密码确认'),
                                     validators=[DataRequired(), Length(4, 20)])
    submit = SubmitField(_l('注册'))

    def validate_email(self, field):
        """ 验证邮箱是否已被注册。实际上是一个魔法方法。源码中是这样描述的：
            Validates the form by calling `validate` on each field, passing any
        extra `Form.validate_<fieldname>` validators to the field validator.

        :param field: 表单邮箱数据
        """
        if User.query.filter_by(email=field.data).first():
            raise ValidationError(_l('该邮箱已被注册'))

    def validate_username(self, field):
        """ 验证用户名是否已被使用。如上，同为魔法方法。

        :param field: 表单用户名数据
        """
        if User.query.filter_by(username=field.data).first():
            raise ValidationError(_l('该用户名已被使用'))


class ChangePasswordForm(FlaskForm):
    """
    修改密码表单
    """
    old_password = PasswordField(_l('原密码'),
                                 validators=[DataRequired()])
    new_password = PasswordField(_l('新密码'),
                                 validators=[DataRequired(), Length(4, 20)])
    submit = SubmitField(_l('提交'))
