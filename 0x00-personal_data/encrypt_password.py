#!/usr/bin/env python3
"""encrypt password using bcrypt"""
import bcrypt


def hash_password(password: str) -> bytes:
    """returns a salted, hashed password, which is a byte string"""
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
