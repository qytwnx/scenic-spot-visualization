class ScenicSpotsAddDto:
    """景点添加实体"""

    def __init__(self, name, level, province, city, address, introduction, heat, price, sales, image, info, comment):
        self.name = name
        self.level = level
        self.province = province
        self.city = city
        self.address = address
        self.introduction = introduction
        self.heat = heat
        self.price = price
        self.sales = sales
        self.image = image
        self.info = info
        self.comment = comment


class ScenicSpotsUpdateDto:
    """用户更新实体"""

    def __init__(self, id, name, level, province, city, address, introduction, heat, price, sales, image, info,
                 comment):
        self.id = id
        self.name = name
        self.level = level
        self.province = province
        self.city = city
        self.address = address
        self.introduction = introduction
        self.heat = heat
        self.price = price
        self.sales = sales
        self.image = image
        self.info = info
        self.comment = comment


class ScenicSpots:
    """用户实体"""

    def __init__(self, id, name, level, province, city, address, introduction, heat, price, sales, image, info, comment,
                 create_time=None, update_time=None):
        self.id = id
        self.name = name
        self.level = level
        self.province = province
        self.city = city
        self.address = address
        self.introduction = introduction
        self.heat = heat
        self.price = price
        self.sales = sales
        self.image = image
        self.info = info
        self.comment = comment
        self.create_time = create_time
        self.update_time = update_time

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "level": self.level,
            "province": self.province,
            "city": self.city,
            "address": self.address,
            "introduction": self.introduction,
            "heat": self.heat,
            "price": self.price,
            "sales": self.sales,
            "image": self.image,
            "info": self.info,
            "comment": self.comment,
            "createTime": self.create_time,
            "updateTime": self.update_time
        }


class ScenicSpotsVo:
    """用户返回模型"""

    def __init__(self, id, name, level, province, city, address, introduction, heat, price, sales, image, info, comment,
                 create_time, update_time):
        self.id = id
        self.name = name
        self.level = level
        self.province = province
        self.city = city
        self.address = address
        self.introduction = introduction
        self.heat = heat
        self.price = price
        self.sales = sales
        self.image = image
        self.info = info
        self.comment = comment
        self.create_time = create_time
        self.update_time = update_time

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "level": self.level,
            "province": self.province,
            "city": self.city,
            "address": self.address,
            "introduction": self.introduction,
            "heat": self.heat,
            "price": self.price,
            "sales": self.sales,
            "image": self.image,
            "info": self.info,
            "comment": self.comment,
            "createTime": self.create_time.strftime("%Y-%m-%d %H:%M:%S"),
            "updateTime": self.update_time.strftime("%Y-%m-%d %H:%M:%S")
        }
