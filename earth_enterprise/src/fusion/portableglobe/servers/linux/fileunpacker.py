#!/usr/bin/python
#
# Copyright 2017 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# This file was automatically generated by SWIG (http://www.swig.org).
# Version 1.3.33
#
# Don't modify this file, modify the SWIG interface instead.
# This file is compatible with both classic and new-style classes.

import _fileunpacker
import new
new_instancemethod = new.instancemethod
try:
    _swig_property = property
except NameError:
    pass # Python < 2.2 doesn't have 'property'.
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'PySwigObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static) or hasattr(self,name):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError,name

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

import types
try:
    _object = types.ObjectType
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0
del types


class FileUnpacker(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, FileUnpacker, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, FileUnpacker, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _fileunpacker.new_FileUnpacker(*args)
        try: self.this.append(this)
        except: self.this = this
    def FindDataPacket(*args): return _fileunpacker.FileUnpacker_FindDataPacket(*args)
    def FindQtpPacket(*args): return _fileunpacker.FileUnpacker_FindQtpPacket(*args)
    def FindFile(*args): return _fileunpacker.FileUnpacker_FindFile(*args)
    def LowOffset(*args): return _fileunpacker.FileUnpacker_LowOffset(*args)
    def HighOffset(*args): return _fileunpacker.FileUnpacker_HighOffset(*args)
    def Size(*args): return _fileunpacker.FileUnpacker_Size(*args)
    def IndexFile(*args): return _fileunpacker.FileUnpacker_IndexFile(*args)
    def IndexSize(*args): return _fileunpacker.FileUnpacker_IndexSize(*args)
    def Index(*args): return _fileunpacker.FileUnpacker_Index(*args)
    __swig_destroy__ = _fileunpacker.delete_FileUnpacker
    __del__ = lambda self : None;
FileUnpacker_swigregister = _fileunpacker.FileUnpacker_swigregister
FileUnpacker_swigregister(FileUnpacker)

class PackageFileLoc(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, PackageFileLoc, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, PackageFileLoc, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _fileunpacker.new_PackageFileLoc(*args)
        try: self.this.append(this)
        except: self.this = this
    def Offset(*args): return _fileunpacker.PackageFileLoc_Offset(*args)
    def Size(*args): return _fileunpacker.PackageFileLoc_Size(*args)
    __swig_destroy__ = _fileunpacker.delete_PackageFileLoc
    __del__ = lambda self : None;
PackageFileLoc_swigregister = _fileunpacker.PackageFileLoc_swigregister
PackageFileLoc_swigregister(PackageFileLoc)

class PackageIndexEntry(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, PackageIndexEntry, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, PackageIndexEntry, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _fileunpacker.new_PackageIndexEntry(*args)
        try: self.this.append(this)
        except: self.this = this
    def Path(*args): return _fileunpacker.PackageIndexEntry_Path(*args)
    def FileLoc(*args): return _fileunpacker.PackageIndexEntry_FileLoc(*args)
    __swig_destroy__ = _fileunpacker.delete_PackageIndexEntry
    __del__ = lambda self : None;
PackageIndexEntry_swigregister = _fileunpacker.PackageIndexEntry_swigregister
PackageIndexEntry_swigregister(PackageIndexEntry)

class Package(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Package, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Package, name)
    __repr__ = _swig_repr
    __swig_getmethods__["CalculateCrc"] = lambda x: _fileunpacker.Package_CalculateCrc
    if _newclass:CalculateCrc = staticmethod(_fileunpacker.Package_CalculateCrc)
    __swig_getmethods__["ReadCrc"] = lambda x: _fileunpacker.Package_ReadCrc
    if _newclass:ReadCrc = staticmethod(_fileunpacker.Package_ReadCrc)
    __swig_getmethods__["ReadVersion"] = lambda x: _fileunpacker.Package_ReadVersion
    if _newclass:ReadVersion = staticmethod(_fileunpacker.Package_ReadVersion)
    __swig_getmethods__["FileSize"] = lambda x: _fileunpacker.Package_FileSize
    if _newclass:FileSize = staticmethod(_fileunpacker.Package_FileSize)
    def __init__(self, *args): 
        this = _fileunpacker.new_Package(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _fileunpacker.delete_Package
    __del__ = lambda self : None;
Package_swigregister = _fileunpacker.Package_swigregister
Package_swigregister(Package)
cvar = _fileunpacker.cvar
Package.kCrcSize = _fileunpacker.cvar.Package_kCrcSize
Package.kCrcOffset = _fileunpacker.cvar.Package_kCrcOffset
Package.kVersionSize = _fileunpacker.cvar.Package_kVersionSize
Package.kVersionOffset = _fileunpacker.cvar.Package_kVersionOffset
Package.kIndexOffsetSize = _fileunpacker.cvar.Package_kIndexOffsetSize
Package.kIndexOffsetOffset = _fileunpacker.cvar.Package_kIndexOffsetOffset
Package_CalculateCrc = _fileunpacker.Package_CalculateCrc
Package_ReadCrc = _fileunpacker.Package_ReadCrc
Package_ReadVersion = _fileunpacker.Package_ReadVersion
Package_FileSize = _fileunpacker.Package_FileSize

kDbRootPacket = _fileunpacker.kDbRootPacket
kDbRoot2Packet = _fileunpacker.kDbRoot2Packet
kQtpPacket = _fileunpacker.kQtpPacket
kQtp2Packet = _fileunpacker.kQtp2Packet
kImagePacket = _fileunpacker.kImagePacket
kTerrainPacket = _fileunpacker.kTerrainPacket
kVectorPacket = _fileunpacker.kVectorPacket
class IndexItem(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, IndexItem, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, IndexItem, name)
    __repr__ = _swig_repr
    __swig_setmethods__["btree_high"] = _fileunpacker.IndexItem_btree_high_set
    __swig_getmethods__["btree_high"] = _fileunpacker.IndexItem_btree_high_get
    if _newclass:btree_high = _swig_property(_fileunpacker.IndexItem_btree_high_get, _fileunpacker.IndexItem_btree_high_set)
    __swig_setmethods__["btree_low"] = _fileunpacker.IndexItem_btree_low_set
    __swig_getmethods__["btree_low"] = _fileunpacker.IndexItem_btree_low_get
    if _newclass:btree_low = _swig_property(_fileunpacker.IndexItem_btree_low_get, _fileunpacker.IndexItem_btree_low_set)
    __swig_setmethods__["level"] = _fileunpacker.IndexItem_level_set
    __swig_getmethods__["level"] = _fileunpacker.IndexItem_level_get
    if _newclass:level = _swig_property(_fileunpacker.IndexItem_level_get, _fileunpacker.IndexItem_level_set)
    __swig_setmethods__["packet_type"] = _fileunpacker.IndexItem_packet_type_set
    __swig_getmethods__["packet_type"] = _fileunpacker.IndexItem_packet_type_get
    if _newclass:packet_type = _swig_property(_fileunpacker.IndexItem_packet_type_get, _fileunpacker.IndexItem_packet_type_set)
    __swig_setmethods__["channel"] = _fileunpacker.IndexItem_channel_set
    __swig_getmethods__["channel"] = _fileunpacker.IndexItem_channel_get
    if _newclass:channel = _swig_property(_fileunpacker.IndexItem_channel_get, _fileunpacker.IndexItem_channel_set)
    __swig_setmethods__["file_id"] = _fileunpacker.IndexItem_file_id_set
    __swig_getmethods__["file_id"] = _fileunpacker.IndexItem_file_id_get
    if _newclass:file_id = _swig_property(_fileunpacker.IndexItem_file_id_get, _fileunpacker.IndexItem_file_id_set)
    __swig_setmethods__["packet_size"] = _fileunpacker.IndexItem_packet_size_set
    __swig_getmethods__["packet_size"] = _fileunpacker.IndexItem_packet_size_get
    if _newclass:packet_size = _swig_property(_fileunpacker.IndexItem_packet_size_get, _fileunpacker.IndexItem_packet_size_set)
    __swig_setmethods__["offset"] = _fileunpacker.IndexItem_offset_set
    __swig_getmethods__["offset"] = _fileunpacker.IndexItem_offset_get
    if _newclass:offset = _swig_property(_fileunpacker.IndexItem_offset_get, _fileunpacker.IndexItem_offset_set)
    def __eq__(*args): return _fileunpacker.IndexItem___eq__(*args)
    def __lt__(*args): return _fileunpacker.IndexItem___lt__(*args)
    def Fill(*args): return _fileunpacker.IndexItem_Fill(*args)
    def __init__(self, *args): 
        this = _fileunpacker.new_IndexItem(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _fileunpacker.delete_IndexItem
    __del__ = lambda self : None;
IndexItem_swigregister = _fileunpacker.IndexItem_swigregister
IndexItem_swigregister(IndexItem)

class PacketBundle(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, PacketBundle, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, PacketBundle, name)
    def __init__(self): raise AttributeError, "No constructor defined"
    __repr__ = _swig_repr
    __swig_destroy__ = _fileunpacker.delete_PacketBundle
    __del__ = lambda self : None;
PacketBundle_swigregister = _fileunpacker.PacketBundle_swigregister
PacketBundle_swigregister(PacketBundle)
