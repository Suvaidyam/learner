async function filter(key, value, fields, doctype) {
 let list= await frappe.call({
        method: "learner.api.get_context",
        args: {
            doctype: doctype,
            filter: {
                [key]: value
            },
            fields:fields
        },
        callback: function (response) {
            // handle the response from the server
            if (response.message) {
                console.log(response.message);
                return response
            } else {
                console.log("Error:", response.exc);
            }
        }
    });
    return list.message;
}
async function truncateDepChild(children = []) {
    for (let child of children) {
        frappe.web_form.set_value(child, '')
    }
}

function filterFields(parent, child, fields, doc) {
    frappe.web_form.on(parent, async (field, value) => {
        let ops = await filter(parent, value,fields, doc);
        let new_opps = ops.map((e)=>{return{
            "label":e[child],
            "value":e.name
        }})
        console.log("new_opps", new_opps)
        var field = frappe.web_form.fields_dict[child]
        if (value) {
            field._data = new_opps;
        } else {
            field._data = [];
            await truncateDepChild(['district', 'block', 'panchayat'])
        }
        field.refresh()
    });
}
async function truncateOptions(fields = []) {
    for (let field of fields) {
        frappe.web_form.fields_dict[field]._data = [];
    }
}

frappe.ready(async function () {
    await truncateOptions(['district', 'block', 'panchayat']);
    filterFields('state', 'district', ["name", "district"],  'District')
    filterFields('district', 'block', ["name", "block"], 'Block')
    filterFields('block', 'panchayat', ["name", 'panchayat'], 'Panchyat')
});


document.querySelector("div.page_content").style.maxWidth = "100%";
