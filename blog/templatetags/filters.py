from django.template.defaulttags import register

@register.filter
def get_value_of(dictionary, key):
    return dictionary.get(key)

@register.filter
def get_value_at(dictionary, idx):
    return list(dictionary)[idx][1]

@register.filter
def get_key_at(dictionary, idx):
    return list(dictionary)[idx][0]