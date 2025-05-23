"""LCM type definitions
This file automatically generated by lcm.
DO NOT MODIFY BY HAND!!!!
"""

from io import BytesIO
import struct

class pd_tau_targets_lcmt(object):

    __slots__ = ["q_des", "tau_ff", "timestamp_us"]

    __typenames__ = ["double", "double", "int64_t"]

    __dimensions__ = [[29], [29], None]

    def __init__(self):
        self.q_des = [ 0.0 for dim0 in range(29) ]
        """ LCM Type: double[29] """
        self.tau_ff = [ 0.0 for dim0 in range(29) ]
        """ LCM Type: double[29] """
        self.timestamp_us = 0
        """ LCM Type: int64_t """

    def encode(self):
        buf = BytesIO()
        buf.write(pd_tau_targets_lcmt._get_packed_fingerprint())
        self._encode_one(buf)
        return buf.getvalue()

    def _encode_one(self, buf):
        buf.write(struct.pack('>29d', *self.q_des[:29]))
        buf.write(struct.pack('>29d', *self.tau_ff[:29]))
        buf.write(struct.pack(">q", self.timestamp_us))

    @staticmethod
    def decode(data):
        if hasattr(data, 'read'):
            buf = data
        else:
            buf = BytesIO(data)
        if buf.read(8) != pd_tau_targets_lcmt._get_packed_fingerprint():
            raise ValueError("Decode error")
        return pd_tau_targets_lcmt._decode_one(buf)

    @staticmethod
    def _decode_one(buf):
        self = pd_tau_targets_lcmt()
        self.q_des = struct.unpack('>29d', buf.read(232))
        self.tau_ff = struct.unpack('>29d', buf.read(232))
        self.timestamp_us = struct.unpack(">q", buf.read(8))[0]
        return self

    @staticmethod
    def _get_hash_recursive(parents):
        if pd_tau_targets_lcmt in parents: return 0
        tmphash = (0xc36d9a4a18ca6110) & 0xffffffffffffffff
        tmphash  = (((tmphash<<1)&0xffffffffffffffff) + (tmphash>>63)) & 0xffffffffffffffff
        return tmphash
    _packed_fingerprint = None

    @staticmethod
    def _get_packed_fingerprint():
        if pd_tau_targets_lcmt._packed_fingerprint is None:
            pd_tau_targets_lcmt._packed_fingerprint = struct.pack(">Q", pd_tau_targets_lcmt._get_hash_recursive([]))
        return pd_tau_targets_lcmt._packed_fingerprint

    def get_hash(self):
        """Get the LCM hash of the struct"""
        return struct.unpack(">Q", pd_tau_targets_lcmt._get_packed_fingerprint())[0]

