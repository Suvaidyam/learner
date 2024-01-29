// Copyright (c) 2024, Rahul Kumar and contributors
// For license information, please see license.txt

frappe.ui.form.on("Block", {
    refresh(frm) {
        frm.fields_dict["district"].get_query = function (doc) {
            return {
                filters: {
                    "state": "Please select a state",
                }
            }
        }

    },
    state: function (frm) {
        frm.fields_dict["district"].get_query = function (doc) {
            if (doc.state) {
                return {
                    filters: {
                        "state": doc.state
                    }
                }
            } else {
                return {
                    filters: {
                        "state": "Please select a state",
                    }
                }
            }
        }
        frm.set_value("district", "")

    },
});
``

