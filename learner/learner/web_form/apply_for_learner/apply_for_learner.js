frappe.ready(function () {
	// bind events here
	frappe.web_form.on("state", () => {
		let state = frappe.web_form.get_value('state');
		console.log(state);

		if (state) {
			return {
				filters: {
					"district": ["=", state]
				}
			};
		} else {
			return {
				filters: {
					"district": ["=", "Please select a state"]
				}
			};
		}
	});

})

document.querySelector("div.page_content").style.maxWidth = "100%";
