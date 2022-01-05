import numpy as np
from datetime import datetime
import astropy
import argparse
from astropy.coordinates import EarthLocation, SkyCoord
from astropy.time import Time
from astropy import units as u
import sys

parser = argparse.ArgumentParser(description="Calculate GMRT Sidereal Time at specified Date and IST")
parser.add_argument('-y', '--year', type=int, help="Year")
parser.add_argument('-mo', '--month', type=int, help="Month")
parser.add_argument('-d', '--date', type=int, help="Date")
parser.add_argument('-hh', '--hour', type=int, help="Hour")
parser.add_argument('-mm', '--minute', type=int, help="Minute")
parser.add_argument('-t', '--observing_duration', type=int, help="Observation Duration (in hours)")
args = parser.parse_args()

#Time correction for GMRT, 4hrs 56 mins 12 secs
#To Calculate LST at GMRT: Find Sidereal Time at Greenwich and add the Longitude correction for GMRT
# GMRT Longitude: 74.049742 Deg East which amounts to a time delay from the GMT of 4hrs 56mins 12 seconds

def get_LST(year, month, date, hour, minute, observing_time):
	print("Starting time of observation is " + str(year)+'-'+str(month)+'-'+str(date)+' T'+str(hour)+':'+str(minute)+':00')
    
	#Calculating UTC
	local_time = hour + minute/60
	utc_time = local_time - 5.5
	if utc_time < 0:
		utc_time += 24
		date -= 1
		if date <=0:
			month -= 1
			if month == 0:
				month = 12
				year -= 1
			if month == 2 and year % 4 == 0:
				date = 29
			if month == 2 and year % 4 != 0:
				date = 28
			if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
				date = 31
			if month == 4 or month == 6 or month == 9 or month == 11:
				date = 30
	hour = int(str(utc_time).split('.')[0])

	minute = int(np.round(60*float('0.'+str(utc_time).split('.')[1])))

	print("UTC time is " + str(year)+'-'+str(month)+'-'+str(date)+' T'+str(hour)+':'+str(minute)+':00')
	
	#Creating Time Object for UTC Time,
	UTC = Time(datetime(year, month, date, hour, minute,0), scale = 'utc')

	GMST = UTC.sidereal_time('mean', 'greenwich')#Calculate GMT Sidereal Time

	gmrt_longitude = SkyCoord(ra = 74.05*u.deg, dec = 19.08333*u.deg)

	gmst = str(GMST)

	h = int(gmst.split('h')[0])
	m = int(gmst.split('h')[1].split('m')[0])

	s = float(gmst.split('h')[1].split('m')[1].split('s')[0])

	#Apply the 4hrs 56mins 12seconds delay
	lst_h = h + 4
	lst_m = m + 56
	lst_s = s + 12.0 

	if lst_s >= 60:
		lst_s -= 60
		lst_m += 1

	if lst_m >= 60:
		lst_m -= 60
		lst_h += 1

	if lst_h >= 24:
		lst_h -= 24

	end_lst_h = lst_h + observing_time
	if end_lst_h >=24:
		end_lst_h -= 24

	print("Starting LST  = ", str(lst_h)+'h'+str(lst_m)+'m'+str(lst_s)+'s')
	print("Ending LST  = ", str(end_lst_h)+'h'+str(lst_m)+'m'+str(lst_s)+'s')
	
	
while __name__ == '__main__':
    year = args.year
    date = args.date
    month = args.month
    hour = args.hour
    minute = args.minute
    observing_duration = args.observing_duration
    get_LST(year, month, date, hour, minute, observing_duration)
    sys.exit()








