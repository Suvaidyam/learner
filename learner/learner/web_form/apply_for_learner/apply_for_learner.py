# learner/learner/web_form/apply_for_learner.py

from __future__ import unicode_literals
import frappe

@frappe.whitelist(allow_guest=True)
def get_context(doctype=None, key=None, value=None, **kwargs):
    # Your custom logic goes here
    # Use doctype, key, and value as needed

    # For example:
    result = {
        'message': 'Hello from get_context',
        'key': key,
        'value': value
    }

    return result
