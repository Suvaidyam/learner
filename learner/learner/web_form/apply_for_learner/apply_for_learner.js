async function filterDistrict(state) {
    var myurl = '/api/method/frappe.desk.search.search_link';
    return new Promise(function (resolve, reject) {
        $.ajax({
            type: 'GET',
            url: myurl,
            data: {
                doctype: 'District',
                filters: JSON.stringify({
                    'state': state
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
		let ops = await filterDistrict(value);
		console.log('asdadad',ops)
        console.log(frappe.web_form)
		frappe.web_form.set_df_property("district", "is_web_form", ops);
        // frappe.web_form.fields
	});
});


document.querySelector("div.page_content").style.maxWidth = "100%";
