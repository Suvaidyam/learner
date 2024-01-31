async function filterDistrict(key,value) {
    var myurl = '/api/method/frappe.desk.search.search_link';
    return new Promise(function (resolve, reject) {
        $.ajax({
            type: 'GET',
            url: myurl,
            data: {
                doctype: 'District',
                filters: JSON.stringify({
                    key: value
                }),
                txt: ''
            },
            success:async function (result) {
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

frappe.ready(function () {
	frappe.web_form.on('state', async (field, value) => {
		let ops = await filterDistrict('state',value);
		frappe.web_form.set_df_property("district", "options", ops);
        var field = frappe.web_form.fields_dict['district']
        field._data = ops;
        field.refresh()
        console.log('fields_disct', field)
	});
});


document.querySelector("div.page_content").style.maxWidth = "100%";
