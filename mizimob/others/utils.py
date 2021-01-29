import re
import smtplib, ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import secrets


def validate_email(email):
    regex = re.compile(r'^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,'
                       r'3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$')
    return re.match(regex, email)


def validate_phone(number):
    regex = re.compile("^[0-9]{10,12}$", re.IGNORECASE)
    final = re.match(regex, number)
    return bool(final)


def send_email(_to, subject, body) -> bool:
    _from = "admin@fuprox.com"
    message = MIMEMultipart("alternative")
    message["Subject"] = subject
    message["From"] = _from
    message["To"] = _to

    # Turn these into plain/html MIMEText objects
    part = MIMEText(body, "html")
    # Add HTML/plain-text parts to MIMEMultipart message
    message.attach(part)
    # Create secure connection with server and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("mail.fuprox.com", 465, context=context) as server:
        server.login(_from, "Japanitoes")
        if server.sendmail(_from, _to, message.as_string()):
            return True
        else:
            return False


def reset_body():
    return f"""<div style="width:100%;font-family:helvetica,&#39;helvetica neue&#39;,arial,verdana,
    sans-serif;margin:0;padding:0">
  <div style="background-color:#f6f6f6"> 

   <table width="100%" cellspacing="0" cellpadding="0" style="border-collapse:collapse;border-spacing:0px;width:100%;height:100%;background:repeat center top;margin:0;padding:0"> 
     <tbody><tr style="border-collapse:collapse"> 
      <td valign="top" style="margin:0;padding:0"> 
       <table cellpadding="0" cellspacing="0" class="m_7060812267205857880es-header" align="center" style="border-collapse:collapse;border-spacing:0px;table-layout:fixed!important;width:100%;background:repeat center top" bgcolor="transparent"> 
         <tbody><tr style="border-collapse:collapse"> 
          <td class="m_7060812267205857880es-adaptive" align="center" bgcolor="#f0f3f4" style="margin:0;padding:0"> 
           <table class="m_7060812267205857880es-header-body" width="600" cellspacing="0" cellpadding="0" align="center" bgcolor="#2b3648" style="border-collapse:collapse;border-spacing:0px"> 
             <tbody><tr style="border-collapse:collapse"> 
             </tr>
           </tbody></table>
</td> 
         </tr> 
       </tbody></table> 
       <table cellpadding="0" cellspacing="0" class="m_7060812267205857880es-content" align="center" style="border-collapse:collapse;border-spacing:0px;table-layout:fixed!important;width:100%"> 
         <tbody><tr style="border-collapse:collapse"> 
          <td align="center" bgcolor="#f0f3f4" style="margin:0;padding:0"> 
           <table width="600" cellspacing="0" cellpadding="0" bgcolor="transparent" align="center" style="border-collapse:collapse;border-spacing:0px"> 
             <tbody><tr style="border-collapse:collapse"> 
              <td align="left" style="margin:0;padding:0"> 
               <table width="100%" cellspacing="0" cellpadding="0" style="border-collapse:collapse;border-spacing:0px"> 
                 <tbody><tr style="border-collapse:collapse"> 
                  <td width="600" valign="top" align="center" style="margin:0;padding:0"> 
                   <table width="100%" cellspacing="0" cellpadding="0" style="border-collapse:collapse;border-spacing:0px"> 
                     <tbody><tr style="border-collapse:collapse"> 
</tr>
                   </tbody></table>
</td> 
                 </tr> 
               </tbody></table>
</td> 
             </tr> 

             <tr style="border-collapse:collapse"> 
              </tr>
<tr style="border-collapse:collapse"> 
              <td align="left" style="margin:0;padding:0 30px" bgcolor="#fcfaf2"> 
               <table width="100%" cellspacing="0" cellpadding="0" style="border-collapse:collapse;border-spacing:0px"> 
                 <tbody><tr style="border-collapse:collapse"> 
                  <td width="540" valign="top" align="center" style="margin:0;padding:0"> 
                   <table width="100%" cellspacing="0" cellpadding="0" style="border-collapse:collapse;border-spacing:0px"> 
                     <tbody><tr style="border-collapse:collapse"> 
<!--                      <td align="center" bgcolor="transparent" dir="ltr" class="m_7060812267205857880es-m-txt-c" style="margin:0;padding:30px 0 10px"><h1 style="line-height:43px;font-family:roboto,&#39;helvetica neue&#39;,helvetica,arial,sans-serif;font-size:36px;font-style:normal;font-weight:normal;color:#2b3648;margin:0" align="center"><b>The Extra Day Sale ends today!</b></h1></td>-->
                     </tr>
                     <tr style="border-collapse:collapse"> 
<!--                      <td align="center" style="margin:0;padding:10px 20px 20px" bgcolor="transparent" dir="ltr" class="m_7060812267205857880es-m-txt-c"><p style="font-size:18px;font-family:roboto,&#39;helvetica neue&#39;,helvetica,arial,sans-serif;line-height:22px;color:#2b3648;margin:0" align="center"><strong>Grab your chance to unlock unlimited learning with 12 months of Premium for the price of 6.</strong></p></td> -->
                     </tr> 
                     <tr style="border-collapse:collapse"> 
                     </tr>
                     <tr style="border-collapse:collapse"> 
                      <td align="left" style="margin:0;padding:20px 20px 30px" bgcolor="transparent" dir="ltr"
                          class="m_7060812267205857880es-m-txt-l"><p
                              style="font-size:14px;font-family:roboto,&#39;helvetica neue&#39;,helvetica,arial,sans-serif;line-height:17px;color:#2b3648;margin:0">
                          Dear ,
<br><br>
                          Below please fine the key to recover you password from Billie Account. Please Not That this
                          key is only valid for Six hour then you will need to generate another one.
                          <br><br>

                          <div style="font-family:monospace"><b></b></div>
                          <br><br>
                          If This  requests was not made by you, please consider changing you password.
                          <br><br>
                          For more information please <b>Open the Billie App On Your phone</b> or click the link
                          below for more infomation
                          <br><br>
                          <a style="text-decoration:none!important;font-family:roboto,&#39;helvetica neue&#39;,helvetica,arial,sans-serif;font-size:24px;color:#2b3648;display:inline-block;background-color:#ffc000;border-radius:20px;font-weight:bold;font-style:normal;line-height:29px;width:auto;text-align:center;border-color:#ffc000;border-style:solid;border-width:10px 30px" href="http://drive.overflow.monster/app/help/password">Password Help</a>

                      </p></td>
                     </tr> 

                     <tr style="border-collapse:collapse"> 
                     </tr>
                   </tbody></table>
</td> 
                 </tr> 
               </tbody></table>
</td> 
             </tr> 
             <tr style="border-collapse:collapse"> 
              <td align="left" style="margin:0;padding:0"> 
               <table cellpadding="0" cellspacing="0" width="100%" style="border-collapse:collapse;border-spacing:0px"> 
                 <tbody><tr style="border-collapse:collapse"> 
                  <td width="600" align="center" valign="top" style="margin:0;padding:0"> 
                   <table cellpadding="0" cellspacing="0" width="100%" style="border-collapse:collapse;border-spacing:0px"> 
                     <tbody><tr style="border-collapse:collapse"> 
                      <td align="center" style="margin:0;padding:0"><img class="m_7060812267205857880adapt-img" src="https://cdn.braze.eu/appboy/communication/assets/image_assets/images/5d6e53729ae1685b2ab3949d/original.png?1567511410" alt="" style="display:block;outline:none;text-decoration:none;border:0" width="600" height="34"></td> 
                     </tr> 
                   </tbody></table>
</td> 
                 </tr> 
               </tbody></table>
</td> 
             </tr> 
           </tbody></table>
</td> 
         </tr> 
       </tbody></table> 
       <table cellpadding="0" cellspacing="0" class="m_7060812267205857880es-footer" align="center" style="border-collapse:collapse;border-spacing:0px;table-layout:fixed!important;width:100%;background:repeat center top" bgcolor="transparent"> 
         <tbody><tr style="border-collapse:collapse"> 
          <td align="center" bgcolor="#f0f3f4" style="margin:0;padding:0"> 
           <table class="m_7060812267205857880es-footer-body" style="border-collapse:collapse;border-spacing:0px" width="600" cellspacing="0" cellpadding="0" bgcolor="#f0f3f4" align="center"> 
             <tbody><tr style="border-collapse:collapse"> 
              <td align="left" style="margin:0;padding:0"> 
               <table width="100%" cellspacing="0" cellpadding="0" style="border-collapse:collapse;border-spacing:0px"> 
                 <tbody><tr style="border-collapse:collapse"> 
                  <td width="600" valign="top" align="center" style="margin:0;padding:0"> 
                   <table width="100%" cellspacing="0" cellpadding="0" style="border-collapse:collapse;border-spacing:0px"> 
                     <tbody><tr style="border-collapse:collapse"> 
                      <td align="center" style="margin:0;padding:10px 20px"> 
                       <table border="0" width="100%" height="100%" cellpadding="0" cellspacing="0" style="border-collapse:collapse;border-spacing:0px"> 
                         <tbody><tr style="border-collapse:collapse"> 
                          <td style="border-bottom-width:0px;border-bottom-color:#cccccc;border-bottom-style:solid;background-image:none;height:1px;width:100%;margin:0px;padding:0"></td> 
                         </tr> 
                       </tbody></table>
</td>
                     </tr> 
                   </tbody></table>
</td> 
                 </tr> 
               </tbody></table>
</td> 
             </tr> 
           </tbody></table>
</td> 
         </tr> 
       </tbody></table> 
       <table class="m_7060812267205857880es-content" cellspacing="0" cellpadding="0" align="center" style="border-collapse:collapse;border-spacing:0px;table-layout:fixed!important;width:100%">
         <tbody><tr style="border-collapse:collapse"></tr>
         <tr style="border-collapse:collapse">
          <td align="center" bgcolor="#f0f3f4" style="margin:0;padding:0">
           <table class="m_7060812267205857880es-footer-body" style="border-collapse:collapse;border-spacing:0px" width="600" cellspacing="0" cellpadding="0" bgcolor="#f0f3f4" align="center">
             <tbody><tr style="border-collapse:collapse">
              <td align="left" style="margin:0;padding:20px 20px 0">
               <table width="100%" cellspacing="0" cellpadding="0" style="border-collapse:collapse;border-spacing:0px">
                 <tbody><tr style="border-collapse:collapse">
                  <td width="560" valign="top" align="center" style="margin:0;padding:0">
                   <table width="100%" cellspacing="0" cellpadding="0" style="border-collapse:collapse;border-spacing:0px">
                     <tbody><tr style="border-collapse:collapse">
                      <td class="m_7060812267205857880es-m-txt-c" align="center" style="margin:0;padding:5px 0 20px">
                       <table class="m_7060812267205857880es-table-not-adapt m_7060812267205857880es-social" cellspacing="0" cellpadding="0" style="border-collapse:collapse;border-spacing:0px">
                         <tbody><tr style="border-collapse:collapse">
                       </tbody></table></td>
                     </tr>
                   </tbody></table></td>
                 </tr>
               </tbody></table></td>
             </tr>
<!--             <tr style="border-collapse:collapse">-->
<!--              <td align="left" style="margin:0;padding:20px">-->
<!--               <table width="100%" cellspacing="0" cellpadding="0" style="border-collapse:collapse;border-spacing:0px">-->
<!--                 <tbody><tr style="border-collapse:collapse">-->
<!--                  <td width="560" valign="top" align="center" style="margin:0;padding:0">-->
<!--                   <table width="100%" cellspacing="0" cellpadding="0" style="border-collapse:collapse;border-spacing:0px">-->
<!--                     <tbody><tr style="border-collapse:collapse">-->
<!--                      <td align="left" style="margin:0;padding:0">-->
<!--                        <p style="font-size:14px;font-family:arial,&#39;helvetica neue&#39;,helvetica,sans-serif;line-height:21px;color:#2b3648;margin:0"><span style="font-size:10px"> No longer need our help? <a href="https://ablink.promos.memrise.com/ls/click?upn=1qLrt1TrXn9A-2F1ZCJ096DlvUrNBuiTJPEHRkj25QFHYnc4coirnkxFR8k4h8GfkP7-2FPgLGsitvl-2B6PkXevPbjKwC5wQeYHUTwNJRP1qHdLA9soIjh7tXoyqIwTHo5n4LdptjkP1UNbbR4uYyOAUUWlCIp2y8WEFBmpmeBMM0rFpqhUc7sUG1cXIxtuPIbpZQIM1hC3lKwt0chJUXXC8Vbh-2BkopUkyTNkBhvFXhW9WW6Ou-2B2zDKvR1OYqK5WtlN-2F2msXMhTesvdEZMg43EhaEJuO2CDfJ0eN8PQYMo4RskMGKjd1JBXJzUzkDHADHadFtmNjEsr94CWbblu-2Bi1yEkX6yx-2F3H7Ie2eTPnrbYyL5RxUA5Di4N9XMkrBI4mveyydeXCpTeZWompO-2FG-2BLxpPtV0Og7ifQ9ym2yhIDOr5rWMqSWNxjA-2BZGE2A6ZrkNqiFSzNz7HUofhszgyO7BSQlCOu7OzqYw7evMpfCFeV0vlxGeLyUsG-2F2fmS24GKSNIU0bPF-2FDQxf4q9h0wLhQr-2Fmn03URrcumWtzwFVXgqYuXKEH0d441BlqTuAe8gW3H3Mvw-2BnQCkvj99uKetRfVsa32DA-3D-3DyCE__I-2BXlUsPfrnJydjcnE-2BgVz8acyqWcoafrAIs2L-2BYnK5oMR-2FypsC6mqzYUAmnAH-2B-2FN1de7pD52F-2Fz6A6yzE2WzkPOECWHFHP0pAFntPK22p0jL3PbKlcknO88XZqup0aS8r8n0KeuTyqIMUzbMtNCva3pQjkyAW2uBIQtH5Pbtzb-2BlRkbUeZ-2FoAr25sCWS2PrhsXU1Bh0I5mi5ugWZETAXQ1swYO6X-2BoV9HWoLQLvcgvPct1Vk9ydYG9UqGava9-2BtvPk10Mx5i4J5RsfiTejSojX2c54hwvoVvBAh-2FHYMNhjfVQv80d7IRrdHAY8XaRN9mllCkJZhruiy3LPhg6HYgMoToTw34kFdLRwBw-2BxgLpUWPvUA2Yq5peKvSnJvfAvv5i3tLzBnsZRbEnwC-2BkxlWNAwK9F0ozyYRoOJt1bwF3IjeD7HBZZ6cNaCO7WrttokuF8beQiQLgrm8ds0vY4ZFo6DqCe-2BuuATX9VDpnVzUXO5MihD9zol-2BZQAbk-2Bp4VPr45ZuvU1Tasfhkr7mOm13IZv-2BLKQr4GLDrU4tCiuhPzmY5vUYEJx-2B3h1lmQhFyClvb1XVja3aQwKMKUbcB2mYLuO3bxkRKeaDyPPlvopjG-2FwH-2FZIt77XOJXb2ZA2GNxoxSb8qz0gh9Y9zRPQIzgUrPjg-3D-3D" target="_blank">Unsubscribe here</a> <br>-->
<!--                        2020 Memrise<br>-->
<!--                        3-5 Fashion Street, E1 6PX, London<br>-->
<!--                        <br>-->
<!--                        This email was sent to <a href="mailto:" 
target="_blank"></a><br>-->
<!--                        You received this email because you are registered with Memrise.</span><br>-->
<!--                        <br>-->
<!--                        <br><br></p>-->
<!--                        <p style="font-size:14px;font-family:arial,&#39;helvetica neue&#39;,helvetica,sans-serif;line-height:21px;color:#2b3648;margin:0"><br></p>-->
<!--                        </td>-->
<!--                     </tr>-->

<!--                   </tbody></table>-->
<!--</td>-->
<!--                 </tr>-->
<!--               </tbody></table>-->
<!--                </td>-->
<!--             </tr>-->
<!--           </tbody>-->
<!--           </table>-->
</td>
         </tr>
       </tbody></table>
    </td>
     </tr>
   </tbody></table> 
  </div> 
<!--<img src="https://ablink.prmos.memrise.com/wf/open?upn=8CZIdLciSFC-2BO5jF-2FiP8qKv6DW1FyR-2FIuCUZYo0Ni4kVI-2BZOcymYMMfMCud9nlIH6b2aN4nqrPocu1Qmw4Za9738XXyv063HbORKWapJfZx9o5JOrKJuJrT9kffDkuTY70n6rh0-2F-2ByhcjUshU-2FWj3Bzlfp9jN9VNOs5wJVIMrZiUPvKV9oQpFrWLOPEXMQT4gaRvO7vuLCEVgMgjRuWZacALSneRquySn5CRBP9iBCl9ty1lXMi9lzSxjc9CgbQbcIqqgmC5kkyj5mPm3ZGwTi1OxYoOOhK-2FvD9y1LCaJOppDOzMOxOLgAIjXhKM0mo1TwmoSvn72k-2FU3xK02x4MLEJbJm-2B671ei2qFpPojojuywNExtxpoI16AO6QFUX24Ig1Xq52LHuWhfoKEeh27DQdiBkVYqLhVwFMUzPWS0rwdCECqACmPd10X72ZrfPKy67FZFIUZuqCtSPARF6kV-2BZgWx-2FsdqFny7Bp447w8GCM5KXshePnDgdro8Fe69GkFW-2B-2F64JktIXJnnspsVQjmbgZDiksop2bspskCmV-2F3bGEiYFuub7yurnZ3zgnV-2Fl38uW2KSXhnwuG4QRfzgMcRPqn9EINsx34W-2FYJDsNnSTAucLjQuyeH3rqMo-2F8YabGRYkXdt9yXiOc-2BIPGvC9mwZwRA-3D-3D" alt="" width="1" height="1" border="0" style="height:1px!important;width:1px!important;border-width:0!important;margin-top:0!important;margin-bottom:0!important;margin-right:0!important;margin-left:0!important;padding-top:0!important;padding-bottom:0!important;padding-right:0!important;padding-left:0!important">-->
</div>
"""


def crop_center(pil_img, crop_width, crop_height):
    img_width, img_height = pil_img.size
    return pil_img.crop(((img_width - crop_width) // 2,
                         (img_height - crop_height) // 2,
                         (img_width + crop_width) // 2,
                         (img_height + crop_height) // 2))


def crop_max_square(pil_img):
    return crop_center(pil_img, min(pil_img.size), min(pil_img.size))


def is_admin(user):
    return user.is_admin


def unique_code(prepend):
    return f"{prepend.upper()}-{secrets.token_hex(8)}"



