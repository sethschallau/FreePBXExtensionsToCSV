import re
import csv
#python 2 compatible, most FreePBX servers run python 2
file = open('/etc/asterisk/sip_additional.conf','r')
rawLine = []
signSpot = 0
extension = ""
arrExtension = []
secret = []
nat = []
callerid = []
for line in file:
	rawLine.append(line)
for line in range(len(rawLine)):
	if(rawLine[line] =="\n"):
		pass
	elif('[' in rawLine[line][0]):
			extension = rawLine[line]
			extension = re.sub(r '\[|\]','',extension)
			if(extension.strip().isdigit()):
				arrExtension.append(extension.rstrip())
	else:
		if("secret=" in rawLine[line]):
			secret.append(rawLine[line][rawLine[line].find('=')+1:].rstrip())
		if("nat=" in rawLine[line]):
			nat.append(rawLine[line][rawLine[line].find('=')+1:].rstrip())
		if("callerid=" in rawLine[line]):
			callerid.append(rawLine[line][rawLine[line].find('=')+1:].rstrip())

def writeCSV(arrExtension,secret,nat,callerid):
	with open('/extenQuBe.csv','w',) as file:
		writer = csv.writer(file)
		writer.writerow(['Extension number','Extension Password','Display Name','Outbound Caller ID','NAT','No Answer','Destination','Busy','Destination','Unavailable','Destination',
			'Voicemail:Enable','Voicemail:Password','Voicemail:Allow access without password from same extension','Voicemail:Allow remote access by pressing "*"','Voicemail:Email',
			'Voicemail:Email attach','Voicemail:Play CID','Voicemail:Play envelope','Voicemail:Delete listened','Voicemail:VM Options','Voicemail:VM Context','Follow Me:Enabled',
			'Follow Me:Initial ring time','Follow Me:FollowMe List','Follow Me:Ring Time','Follow Me:Ring Strategy','Follow Me:Play Music On Hold',
			'Follow Me:Music On Hold Class','Follow Me:CID Prefix','Follow Me:CID Forward Mode','Follow Me:Fixed CID','Follow Me:No Answer','Follow Me:Destination',
			'Extensions Settings:Queue state detection','Extensions Settings:Emergency CallerID','Extensions Settings:Ring Time','Extensions Settings:Call Waiting',
			'Extensions Settings:Allow spying','Extensions Settings:Call Screening','Extensions Settings:Incoming Call Presentation',
			'Extensions Settings:Answer the Channel When Call Forwarding is Enabled','Recording Settings:Incoming Internal Calls',
			'Recording Settings:Outgoing Internal Calls','Recording Settings:Incoming External Calls','Recording Settings:Outgoing External Calls',
			'Recording Settings:Ondemand Recording','Device SIP Settings:Context','Device SIP Settings:Host','Device SIP Settings:Type',
			'Device SIP Settings:DTMF Mode','Device SIP Settings:Direct Media','Device SIP Settings:Qualify','Device SIP Settings:Qualify Frequency',
			'Device SIP Settings:Port','Device SIP Settings:Session Timers','Device SIP Settings:Call Groups',	'Device SIP Settings:Pickup Groups',
			'Device SIP Settings:Account Code','Device SIP Settings:Call Counter','Device SIP Settings:Call Limit','Device SIP Settings:Outgoing Calls MOH Class',
			'Device SIP Settings:Incoming Calls MOH Class','Deny Address:deny','Permit address:Permit','Advanced Settings:Option'])
		for x in range(len(secret)):
			writer.writerow([arrExtension[x],secret[x],callerid[x],'',nat[x]])
		print("Done.")

writeCSV(arrExtension,secret,nat,callerid)

