from django import template

register = template.Library()


@register.filter
def admin_page(obj):
    app = obj._meta.app_label
    model = obj._meta.model_name
    return "admin:{}_{}_change".format(app, model)
