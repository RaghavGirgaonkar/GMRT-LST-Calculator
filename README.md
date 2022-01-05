# GMRT-LST-Calculator
Script to find the Local Sidereal Time (LST) at the Giant Metrewave Radio Telescope (GMRT) Pune, India

# Usage

usage: python lst_calculator.py [-h] [-y YEAR] [-mo MONTH] [-d DATE] [-hh HOUR] [-mm MINUTE] [-t OBSERVING_DURATION]

Calculate GMRT Sidereal Time at specified Date and IST

optional arguments:

  -h, --help            show this help message and exit
  
  -y YEAR, --year YEAR  Year
  
  -mo MONTH, --month MONTH Month
                        
  -d DATE, --date DATE  Date
  
  -hh HOUR, --hour HOUR Hour
  
  -mm MINUTE, --minute MINUTE Minute
  
  -t OBSERVING_DURATION, --observing_duration OBSERVING_DURATION Observation Duration (in hours)
  
  # Python Requirements
  
  astropy
