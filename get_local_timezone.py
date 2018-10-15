import time
import pytz
import datetime

local_names = []
if time.daylight:
    local_offset = time.altzone
    localtz = time.tzname[1]
else:
    local_offset = time.timezone
    localtz = time.tzname[0]

local_offset = datetime.timedelta(seconds=-local_offset)

for name in pytz.all_timezones:
    timezone = pytz.timezone(name)
    if not hasattr(timezone, '_tzinfos'):
        continue#skip, if some timezone doesn't have info
    # go thru tzinfo and see if short name like EDT and offset matches
    for (utcoffset, daylight, tzname), _ in timezone._tzinfos.iteritems():
        if utcoffset == local_offset and tzname == localtz:
            local_names.append(name)

print local_names
