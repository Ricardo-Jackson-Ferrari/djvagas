class FormMixin:
    def add_attr(self, field, attr_name, attr_value):
        field = self.fields[field]
        existing_attr = field.widget.attrs.get(attr_name, '')
        field.widget.attrs[attr_name] = f'{existing_attr} {attr_value}'.strip()

    def add_attr_placeholder(self, field, attr_value):
        self.add_attr(field, 'placeholder', attr_value)
