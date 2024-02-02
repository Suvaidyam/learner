import frappe

@frappe.whitelist(allow_guest=True)
def get_context(doctype=None, filter=None , fields=['*']):
    
    results = frappe.get_all(doctype, fields, filters=filter)

    return results
