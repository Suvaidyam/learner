import smtplib
import frappe
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class MSG:
    def send_email(name,user_eamil,subjects,data=None):
        sender_email = 'noreply.suvaidyam@gmail.com'
        sender_password = 'gfiw axwi tswb rvgy'
        receiver_email = user_eamil
        subject = subjects
        accepted = f"""
        <html>
          <body class="bg-light">
           <div class="p-2" style="background:white;padding:5px;">
           <img src="https://res.cloudinary.com/dkb3hvxhf/image/upload/v1709007859/SecondaryLogoColor_1_qnpkoy.png" alt="Suvaidyam" width="200" style="display:block;width:100%;margin:auto;padding-bottom:15px">
              <div style="border-radius:10px;border:1px solid grey;padding:10px;font-size:15px;">
                <p style="font-size:15px;font-weight:600;">Hello {name} 👋,</p>
                <p style="font-size:15px">I hope you are doing well. 
                    We are excited to inform you that after a thorough review of the 
                    applications, you have been selected for the Suvaidyam Learner Program.</p>
                  Congratulations 😍 on this achievement! Your enthusiasm for learning and your 
                  commitment to personal and professional development stood out among the applicants,
                    and we believe that you will contribute significantly to the program.
              </div>
              <div style="display:flex;padding-top:8px;">
                  <a href="https://www.instagram.com/suvaidyam" style="width:35px;height:35px;cursor: pointer;border-radius:10px;background:gray;margin: 0px 7px;">
                    <img src="https://res.cloudinary.com/dkb3hvxhf/image/upload/v1709008582/insta_a9nghw.png" style="border-radius:10px;" width="100%"/>
                  </a>
                  <a href="https://www.whatsapp.com/channel/0029VaAg20iG3R3rCSYYjL30" style="width:35px;height:35px;cursor: pointer;border-radius:10px;background:gray;margin: 0px 7px;">
                    <img src="https://res.cloudinary.com/dkb3hvxhf/image/upload/v1709008589/whats_rzokoe.png" style="border-radius:10px;" width="100%"/>
                  
                  
                  </a>
                  <a href="https://www.youtube.com/@suvaidyam" style="width:35px;height:35px;cursor: pointer;border-radius:10px;background:gray;margin: 0px 7px;">
                    <img src="https://res.cloudinary.com/dkb3hvxhf/image/upload/v1709008596/youtube_ukjh7i.png" style="border-radius:10px;" width="100%"/>
                    
                  </a>
                  <a href="https://www.linkedin.com/company/suvaidyam/?originalSubdomain=in" style="width:35px;height:35px;cursor: pointer;border-radius:10px;background:gray;margin: 0px 7px;">
                    <img src="https://res.cloudinary.com/dkb3hvxhf/image/upload/v1709009320/link_tova1z.png" style="border-radius:10px;" width="100%"/>
                    
                  </a>
              </div>
            </div>
          </body>
        </html>
        """
        rejected = f"""
        <html>
          <body class="bg-light">
           <div class="p-2" style="background:white;padding:5px;">
            <img src="https://res.cloudinary.com/dkb3hvxhf/image/upload/v1709007859/SecondaryLogoColor_1_qnpkoy.png" alt="Suvaidyam" width="200" style="display:block;width:100%;margin:auto;padding-bottom:15px">
               <div style="border-radius:10px;border:1px solid grey;padding:10px;font-size:15px;">
                <p style="font-size:15px;font-weight:600;">Hello {name} 👋,</p>
                <p style="font-size:15px">I trust this message finds you well.
                  We appreciate the time and effort you invested in applying for the Suvaidyam Learner Program.</p>
                  <p>After careful consideration and review of all applications, we regret to inform you that your application was not selected 😔 for the program. While we received numerous impressive applications, the selection process was highly competitive.</p>
                  <p>We commend your interest in the program and encourage you to continue pursuing your passion for learning and professional development. The decision-making process was challenging, and unfortunately, we were unable to accommodate all qualified candidates.</p>
                  <p>We genuinely appreciate your interest in our program and wish you the best in your future endeavors. Thank you for your understanding.</p>
              </div>
              <div style="display:flex;padding-top:8px;">
                  <a href="https://www.instagram.com/suvaidyam" style="width:35px;height:35px;cursor: pointer;border-radius:10px;background:gray;margin: 0px 7px;">
                    <img src="https://res.cloudinary.com/dkb3hvxhf/image/upload/v1709008582/insta_a9nghw.png" style="border-radius:10px;" width="100%"/>
                  </a>
                  <a href="https://www.whatsapp.com/channel/0029VaAg20iG3R3rCSYYjL30" style="width:35px;height:35px;cursor: pointer;border-radius:10px;background:gray;margin: 0px 7px;">
                    <img src="https://res.cloudinary.com/dkb3hvxhf/image/upload/v1709008589/whats_rzokoe.png" style="border-radius:10px;" width="100%"/>
                  
                  
                  </a>
                  <a href="https://www.youtube.com/@suvaidyam" style="width:35px;height:35px;cursor: pointer;border-radius:10px;background:gray;margin: 0px 7px;">
                    <img src="https://res.cloudinary.com/dkb3hvxhf/image/upload/v1709008596/youtube_ukjh7i.png" style="border-radius:10px;" width="100%"/>
                    
                  </a>
                  <a href="https://www.linkedin.com/company/suvaidyam/?originalSubdomain=in" style="width:35px;height:35px;cursor: pointer;border-radius:10px;background:gray;margin: 0px 7px;">
                    <img src="https://res.cloudinary.com/dkb3hvxhf/image/upload/v1709009320/link_tova1z.png" style="border-radius:10px;" width="100%"/>
                    
                  </a>
              </div>
            </div>
          </body>
        </html>
        """
        admin = f"""
        <html>
          <body class="bg-light">
            <div style="background:#F8F9FA" class="p-2">
              <img src="https://res.cloudinary.com/dkb3hvxhf/image/upload/v1709007859/SecondaryLogoColor_1_qnpkoy.png" alt="Suvaidyam" width="200" style="display:block;width:100%;margin:auto;padding-bottom:15px">
                <div style="border-radius:10px;background:white;padding:10px;">
                    <p style="font-size:15px">Heyy Samar Singh 👋,<br>There is a new application on <a href="https://learn.suvaidyam.com">https://learn.suvaidyam.com</a></p>
                    <div style="border-radius:8px;background:#efefef;padding:10px;font-size:15px;">
                    <pre>
                     {data}
                    </pre>
                </div>
             </div>
            </div>
          </body>
        </html>
        """
        applied = f"""
        <html>
          <body class="bg-light">
           <div class="p-2" style="background:white;padding:5px;">
           <img src="https://res.cloudinary.com/dkb3hvxhf/image/upload/v1709007859/SecondaryLogoColor_1_qnpkoy.png" alt="Suvaidyam" width="200" style="display:block;margin:auto;padding-bottom:15px">
              <div style="border-radius:10px;border:1px solid grey;padding:10px;font-size:15px;">
                <p style="font-size:15px;font-weight:600;">Dear {name} 👋,</p>
                <p style="font-size:15px">
                I trust this message finds you well.
                Thank you for taking the time and effort to apply for the Suvaidyam Learner Program. We appreciate your interest and enthusiasm for joining our program dedicated to personal and professional development.
                After a thorough review of the applications, we are pleased to inform you that you have been selected for the Suvaidyam Learner Program. 
                <br>
                <strong>Congratulations</strong> on this well-deserved achievement! Your commitment to learning and your passion for personal growth truly stood out among the applicants.
                We believe that your unique skills and dedication will contribute significantly to the success of the program. We are excited to have you on board and look forward to the learning journey ahead.
                Once again, congratulations on this accomplishment, and thank you for choosing Suvaidyam for your learning endeavors.
                Best regards,
                Suvaidyam Learning Team
                </p>
              </div>
              <div style="display:flex;padding-top:8px;">
                  <a href="https://www.instagram.com/suvaidyam" style="width:35px;height:35px;cursor: pointer;border-radius:10px;background:gray;margin: 0px 7px;">
                    <img src="https://res.cloudinary.com/dkb3hvxhf/image/upload/v1709008582/insta_a9nghw.png" style="border-radius:10px;" width="100%"/>
                  </a>
                  <a href="https://www.whatsapp.com/channel/0029VaAg20iG3R3rCSYYjL30" style="width:35px;height:35px;cursor: pointer;border-radius:10px;background:gray;margin: 0px 7px;">
                    <img src="https://res.cloudinary.com/dkb3hvxhf/image/upload/v1709008589/whats_rzokoe.png" style="border-radius:10px;" width="100%"/>
                  
                  
                  </a>
                  <a href="https://www.youtube.com/@suvaidyam" style="width:35px;height:35px;cursor: pointer;border-radius:10px;background:gray;margin: 0px 7px;">
                    <img src="https://res.cloudinary.com/dkb3hvxhf/image/upload/v1709008596/youtube_ukjh7i.png" style="border-radius:10px;" width="100%"/>
                    
                  </a>
                  <a href="https://www.linkedin.com/company/suvaidyam/?originalSubdomain=in" style="width:35px;height:35px;cursor: pointer;border-radius:10px;background:gray;margin: 0px 7px;">
                    <img src="https://res.cloudinary.com/dkb3hvxhf/image/upload/v1709009320/link_tova1z.png" style="border-radius:10px;" width="100%"/>
                    
                  </a>
              </div>
            </div>
          </body>
        </html>
        """
        
        body = accepted if subject == 'Accepted' else (rejected if subject == 'Rejected' else (applied if subject == 'Applied' else admin))  
        message = MIMEMultipart()
        message['From'] = 'Suvaidyam <{}>'.format(sender_email)
        message['To'] = receiver_email
        message['Subject'] = subject
        message.attach(MIMEText(body, 'html'))

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(sender_email, sender_password)
            server.send_message(message)
