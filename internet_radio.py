#! /usr/bin/python3

#    internet_radio.py
#    Copyright (C) 2015  Patrick Graham
#
#   This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.

import sys
import subprocess
if len(sys.argv) < 2:
        print('Usage python: internet_radio.py [station] - listen to internet radio.')
        sys.exit()

stations = {'left_coast_70s': 'http://somafm.com/seventies.pls', 'celtic': 'http://somafm.com/thistle.pls', 'klol': 'http://rock101klol.com:8000/listen.pls'}

# First command line argument is the station name.
station = sys.argv[1]

if station in stations:
    return subprocess.call([vlc", stations[station]])
else:
        print('There is no station called ' + station)
