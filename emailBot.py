import smtplib
from os.path import basename
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.utils import COMMASPACE, formatdate

def send(wmsg, images, sender, recievers):
    username = sender
    password = pwd
    
    sender = sender
    recievers = recievers
    
    weatherMsg = MIMEText(wmsg, 'plain')

    imgmsg = """\
<html>
    <head></head>
    <body>
	<h3>Today, you should be wearing</h3>
    <body>
</html>
""" 

    imageMsg = MIMEText(imgmsg, 'html')
    
    imgkeys = [key for key in images if images[key]]
    fps = [open(images[key], 'rb') for key in imgkeys]
    imgs = [MIMEImage(fps[i].read())for i in range(len(fps))]
    [fps[i].close() for i in range(len(fps))] 


    for i in range(len(imgkeys)):
	 imgs[i].add_header('Content-ID', '<{}>'.format(images[imgkeys[i]]))

    msg = MIMEMultipart()
    msg["To"] = COMMASPACE.join(recievers)
    msg["From"] = sender
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = "Weather and Clothing Reminder"

    msg.attach(weatherMsg)
    msg.attach(imageMsg)

    [msg.attach(x) for x in imgs]
    
   
    try: 
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(username,password)
        server.sendmail(sender, recievers, msg.as_string())
        server.close()
        print("sent")
    except:
        print("something went wrong")
