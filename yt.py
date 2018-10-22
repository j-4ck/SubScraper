import requests
import sys

try:
	data=requests.get(sys.argv[1]).content
except IndexError:
	print 'Usage:\n\tpython %s <channel-url>\nExample:\n\tpython %s https://www.youtube.com/user/PewDiePie'%(sys.argv[0], sys.argv[0])
	sys.exit()
num1 = int(data.split('subscriber-count')[1].split('<span class="yt-subscription-button-disabled-mask"')[0].split('aria-label="')[1].split('">')[0].strip('subscribers').replace(',',''))
count = 1
while True:
	try:
		data=requests.get(sys.argv[1]).content
		num = int(data.split('subscriber-count')[1].split('<span class="yt-subscription-button-disabled-mask"')[0].split('aria-label="')[1].split('">')[0].strip('subscribers').replace(',',''))
		if num-num1>-1:sgn='+'
		else:sgn=''
		sys.stdout.write('\r'+'['+str(count)+'] '+data.split('og:title')[1].split('">')[0][11:]+': ')
		sys.stdout.write(data.split('subscriber-count')[1].split('<span class="yt-subscription-button-disabled-mask"')[0].split('aria-label="')[1].split('">')[0]+' ('+sgn+str(num-num1)+')')
		sys.stdout.flush()
		num1 = num
		count+=1
	except:
		sys.exit('')

