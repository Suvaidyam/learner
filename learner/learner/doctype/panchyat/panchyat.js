// Copyright (c) 2024, Rahul Kumar and contributors
// For license information, please see license.txt


frappe.ui.form.on("Panchyat", {
    refresh(frm) {
        frm.fields_dict["district"].get_query = function (doc) {
            return {
                filters: {
                    "state": "Please select a state",
                }
            }
        }
        frm.fields_dict["block"].get_query = function (doc) {
            return {
                filters: {
                    "district": "Please select a district",
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
        frm.fields_dict["block"].get_query = function (doc) {
            if (doc.district) {
                return {
                    filters: {
                        "district": doc.district
                    }
                }
            } else {
                return {
                    filters: {
                        "district": "Please select a district",
                    }
                }
            }
        }
        frm.set_value("district", "")
        frm.set_value("block", "")

    },
    district: function (frm) {
        frm.set_value("block", "")
    }

});


