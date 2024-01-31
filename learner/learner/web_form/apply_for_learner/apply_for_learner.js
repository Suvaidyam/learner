async function filter(key, value, doc) {
    var myurl = '/api/method/frappe.desk.search.search_link';
    return new Promise(function (resolve, reject) {
        $.ajax({
            type: 'GET',
            url: myurl,
            data: {
                doctype: doc,
                filters: JSON.stringify({
                    [key]: value
                }),
                txt: ''
            },
            success: async function (result) {
                var options = await result.message;
                resolve(options);
            },
            error: function (err) {
                console.error(err.responseText);
                reject(err);
            }
        });
    });
}
async function truncateDepChild(children=[]){
    for(let child of children){
        frappe.web_form.set_value(child, '')
    }
}

function filterFields(parent, child, doc) {
    frappe.web_form.on(parent, async (field, value) => {
        let ops = await filter(parent, value, doc);
        var field = frappe.web_form.fields_dict[child]
        if (value) {
            field._data = ops;
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
    filterFields('state', 'district', 'District')
    filterFields('district', 'block', 'Block')
    filterFields('block', 'panchayat', 'Panchyat')
});


document.querySelector("div.page_content").style.maxWidth = "100%";
