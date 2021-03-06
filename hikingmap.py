#!/usr/bin/env python

# hikingmap -- render maps on paper using data from OpenStreetMap
# Copyright (C) 2015  Roel Derickx <roel.derickx AT gmail>

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import sys, mapnik

from hikingmap_parameters import Parameters
from hikingmap_tracks import Tracks
from hikingmap_trackfinder import TrackFinder

# MAIN

if not hasattr(mapnik, 'mapnik_version') or mapnik.mapnik_version() < 600:
    raise SystemExit('This script requires Mapnik >= 0.6.0)')

# enable to search other paths for fonts
mapnik.FontEngine.register_fonts("/usr/share/fonts/noto", True)
mapnik.FontEngine.register_fonts("/usr/share/fonts/noto-cjk", True)
mapnik.FontEngine.register_fonts("/usr/share/fonts/TTF", True)

params = Parameters()
if not params.parse_commandline():
    sys.exit()

tracks = Tracks(params)

trackfinder = TrackFinder(params, tracks)
trackfinder.render()

