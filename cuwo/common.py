# Copyright (c) Mathias Kaerlev 2013.
#
# This file is part of cuwo.
# 
# cuwo is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# cuwo is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with cuwo.  If not, see <http://www.gnu.org/licenses/>.

from cuwo import constants

def get_hex_string(value):
    v = '0x'
    for c in value:
        new_hex = hex(ord(c))[2:].upper()
        if len(new_hex) < 2:
            new_hex = '0' + new_hex
        v += new_hex
    return v

def is_bit_set(value, index):
    return value & (1 << index)

def get_time_string(value):
    hour = (value * 24) / constants.MAX_TIME
    minute = ((value * 24 * 60) / constants.MAX_TIME) % 60
    return '%02d:%02d' % (hour, minute)

def get_chunk(vec):
    return (int(vec.x / constants.CHUNK_SCALE), 
            int(vec.y / constants.CHUNK_SCALE))

def get_sector(vec):
    return (int(vec.x / constants.SECTOR_SCALE), 
            int(vec.y / constants.SECTOR_SCALE))