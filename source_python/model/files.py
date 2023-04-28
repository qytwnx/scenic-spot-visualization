from model.user import UserSimpleVo


class FilesAddDto:
    """文件记录添加实体"""

    def __init__(self, name, file_type, size, url, uploader):
        self.name = name
        self.type = file_type
        self.size = size
        self.url = url
        self.uploader = uploader


class Files:
    """文件实体"""

    def __init__(self, id, name, file_type, size, url, uploader, create_time=None, update_time=None):
        self.id = id
        self.name = name
        self.type = file_type
        self.size = size
        self.url = url
        self.uploader = uploader
        self.create_time = create_time
        self.update_time = update_time

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "type": self.type,
            "size": self.size,
            "url": self.url,
            "uploader": self.uploader,
            "createTime": self.create_time,
            "updateTime": self.update_time
        }


class FilesVo:
    """文件返回模型"""

    def __init__(self, id, name, file_type, size, url, uploader: UserSimpleVo, create_time=None,
                 update_time=None):
        self.id = id
        self.name = name
        self.type = file_type
        self.size = size
        self.url = url
        self.uploader = uploader
        self.create_time = create_time
        self.update_time = update_time

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "type": self.type,
            "size": self.size,
            "url": self.url,
            "uploader": self.uploader,
            "createTime": self.create_time.strftime("%Y-%m-%d %H:%M:%S"),
            "updateTime": self.update_time.strftime("%Y-%m-%d %H:%M:%S")
        }
