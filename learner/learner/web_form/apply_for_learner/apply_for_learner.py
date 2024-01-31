import frappe


def get_context(context):
    # Your code to populate the context goes here
    context['custom_data'] = "Hello, this is custom data!"
    return context
