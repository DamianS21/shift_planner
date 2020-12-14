# Shift planner
## Init
This project was used to as a useful tool for scheduling of work in 24h shifts.
## Description
Day shift (from 07:00 to 19:00) and night shift (from 19:00 to 07:00 next day) are assigned to the most rested user (having the longest _time of break_).
After each iteration to dict _time of break_ is reseted for user that had scheduled duty, and added 12h rest period to others.


The script allows to assign request free from day and night shift in variables _request_day_ and _request_night_.

**The script is still under contruction and was used as a single time solution.**

## To do:
- remove global variables
- make variables more understable to reader
- make better representations of result
- make it user friendly
