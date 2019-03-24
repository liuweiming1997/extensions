#!/usr/bin/env python3
# -*- coding: utf-8 -*-

SEED = 131
MOD = 1000000007

class HashUtil:

    @classmethod
    def get_hash_by_string(cls, s):
        hash_val = 0
        for ch in s:
            hash_val = hash_val * SEED + ord(ch)
            hash_val %= MOD
        return hash_val
