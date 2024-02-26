# Copyright (c) 2024, Rahul Kumar and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document
from learner.services.send_mail import MSG

class LearnerForm(Document):
	def on_update(self):
		if self.application_status =='Accepted':
		
			MSG.send_email(self.full_name,self.email,self.application_status)
		elif self.application_status == 'Rejected': 
			MSG.send_email(self.full_name,self.email,self.application_status)
		elif self.application_status == 'Open': 
			data = {
				"full_name":self.full_name,
				"email":self.email,
				"phone_zwil":self.phone_zwil,
				"block":self.block,
				"panchayat":self.panchayat,
				"village":self.village,
				"passing_year_10th":self.passing_year_10th,
				"total_obtain_marks":self.total_obtain_marks,
				"obtain_marks_in_science":self.obtain_marks_in_science,
				"obtain_marks_in_maths":self.obtain_marks_in_maths,
				"result_not_yet_declared":self.result_not_yet_declared,
				"passing_year_12th":self.passing_year_12th,
				"stream":self.stream,
				"main_subject":self.main_subject,
				"obtain_marks_in_maths12":self.obtain_marks_in_maths12,
				"total_obtain_marks12":self.total_obtain_marks12,
				"career_option":self.career_option,
			}
			MSG.send_email(self.full_name,'abhishek.suvaidyam@gmail.com',self.application_status,data)

	
