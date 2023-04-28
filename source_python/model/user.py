class UserLoginDto:
    """用户登录实体"""

    def __init__(self, account, password):
        self.account = account
        self.password = password


class UserAddDto:
    """用户添加实体"""

    def __init__(self, name, account, password, role):
        self.name = name
        self.account = account
        self.password = password
        self.role = role


class UserUpdateDto:
    """用户更新实体"""

    def __init__(self, id, name, account):
        self.id = id
        self.name = name
        self.account = account


class UserChangePasswordDto:
    """用户修改密码实体"""

    def __init__(self, id, account, old_password, password, re_password):
        self.id = id
        self.account = account
        self.old_password = old_password
        self.password = password
        self.re_password = re_password


class User:
    """用户实体"""

    def __init__(self, id, name, account, password, role, create_time=None, update_time=None):
        self.id = id
        self.name = name
        self.account = account
        self.password = password
        self.role = role
        self.create_time = create_time
        self.update_time = update_time

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "account": self.account,
            "password": self.password,
            "role": self.role,
            "createTime": self.create_time,
            "updateTime": self.update_time
        }


class UserVo:
    """用户返回模型"""

    def __init__(self, id, name, account, role, create_time, update_time):
        self.id = id
        self.name = name
        self.account = account
        self.role = role
        self.create_time = create_time
        self.update_time = update_time

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "account": self.account,
            "role": self.role,
            "createTime": self.create_time.strftime("%Y-%m-%d %H:%M:%S"),
            "updateTime": self.update_time.strftime("%Y-%m-%d %H:%M:%S")
        }


class UserLoginVo:
    """用户登录返回模型"""

    def __init__(self, user, token: str):
        self.user = user
        self.token = token

    def to_dict(self):
        return {
            "user": self.user,
            "token": self.token
        }


class UserSimpleVo:
    """用户返回简单模型"""

    def __init__(self, id, name, account):
        self.id = id
        self.name = name
        self.account = account

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "account": self.account
        }
