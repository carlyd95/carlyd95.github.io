#!/usr/bin/python

import urllib2
from datetime import datetime, timedelta

hoy = datetime.now().strftime("%Y/%m/%d:%A/%B/%d")
day = hoy.split(':')
lastmonth = datetime.strftime(datetime.now() - timedelta(1), '%B')

resp = urllib2.urlopen("https://wol.jw.org/en/wol/dt/r1/lp-e/" + day[0]).read()

rmdr = ''
rmdrday = day[1].split('/')
if int(rmdrday[2]) == 1:
	rmdr = '\n<b>Have you turned your time in for the month of ' + lastmonth + '?</b>'

html = "<center>\n" + resp.split('Examining the Scriptures Daily\xe2\x80\x94' + day[0].split('/')[0] + '\n                </div>\n            </div>\n    \n            <div class="cardTitleDetail"></div>\n    \n            <div class="cardChevron">\n                <div class="icon"></div>\n            </div>\n    \n            </a>\n    \n                        </div>\n                                    </div>\n                                    ')[1].split('</div>\n                            </div>\n                    <div class="todayItem today')[0].replace('<a href=', '<a style="color:#808080" href=') + rmdr + "\n</center>"

html = html.replace('/en/wol/', 'https://wol.jw.org/en/wol/')

"""
sday = day[1].split('/')
sday = sday[0] + ', ' + sday[1] + "\xc2\xa0" + str(int(sday[2]))
html = html.split(sday + "</h2>\r\n</header>\r\n")[1]
subj = sday.replace('\xc2\xa0', ' ')
"""

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


from_addr = 'Daily Text <dcarltondunlap@gmail.com>'
recipients = ['courtneywdunlap@hotmail.com','foxy56127@gmail.com', 'summitmkt@gmail.com', 'debbie.u.watson@hotmail.com', 'dcarltondunlap@hotmail.com', 'edcook1@crimson.ua.edu']

msg = MIMEMultipart()
msg['From'] = from_addr
msg['To'] = from_addr
msg['Subject'] = 'Daily Text'


# Record the MIME types of both parts - text/plain and text/html.
htmlmime = MIMEText(html, 'html')

# Attach parts into message container.
# According to RFC 2046, the last part of a multipart message, in this case
# the HTML message, is best and preferred.
msg.attach(htmlmime)

s = smtplib.SMTP('localhost')
s.sendmail(from_addr, [from_addr] + recipients, msg.as_string())
s.quit()
