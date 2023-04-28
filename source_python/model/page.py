class Page:
    def __init__(self, total, records):
        self.total = total
        self.records = records

    def to_dict(self):
        return {
            'total': self.total,
            'records': self.records,
        }
