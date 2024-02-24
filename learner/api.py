import frappe

@frappe.whitelist(allow_guest=True)
def get_context(doctype=None, filter=None , fields=['*']):
    
    results = frappe.get_all(doctype, fields, filters=filter)

    return results

@frappe.whitelist(allow_guest=True)
def contact_us(full_name, email, message):
    new_doc = frappe.new_doc('Contact us')
    new_doc.full_name = full_name
    new_doc.email = email
    new_doc.message = message
    new_doc.save()
    return new_doc
    

@frappe.whitelist(allow_guest=True)
def subscribe(email):
    new_doc = frappe.new_doc('Subscribe')
    new_doc.email = email
    new_doc.save()
    return new_doc