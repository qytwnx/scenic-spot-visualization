class CountVo:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def to_dict(self):
        return {
            "name": self.name,
            "value": self.value
        }


class CountProvinceVo:
    def __init__(self, name, value, example):
        self.name = name
        self.value = value
        self.example = example

    def to_dict(self):
        return {
            "name": self.name,
            "value": self.value,
            "example": self.example
        }


class SalesVo:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def to_dict(self):
        return {
            "x": self.x,
            "y": self.y
        }
