# -*- coding: UTF-8 -*-


class DynamicTable(Document):
    rows = ListField(DictField())