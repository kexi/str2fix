"""
str2fix.

An example python library.
"""

__version__ = "0.1.0"
__author__ = 'kexi'
__credits__ = 'kexi'

import mojimoji as moji
import unicodedata


def convert_with_x(val: str, field_length: int) -> str:
    """半角にして左詰(残りは半角スペース)

    :param val: 文字列
    :type val: str
    :param field_length: フィールド長
    :type field_length: int
    :return: 固定長文字列(UTF-8)
    :rtype: str
    """

    val = moji.zen_to_han(val)
    byte = 0
    r = ""
    for ch in val:
        r += ch
        byte += len(ch.encode('cp932'))
        if byte >= field_length:
            break

    while byte < field_length:
        r += " "
        byte += 1

    return r


def convert_with_n(val: str, field_length: int) -> str:
    """全角にして左詰(残りは全角スペース)

    :param val: 文字列
    :type val: str
    :param field_length: フィールド長
    :type field_length: int
    :return: 固定長文字列(UTF-8)
    :rtype: str
    """
    val = moji.han_to_zen(val)
    byte = 0
    r = ""
    for ch in val:
        r += ch
        byte += len(ch.encode('cp932'))
        if byte >= field_length:
            break

    while byte < field_length:
        r += "　"
        byte += 2

    return r


def convert_with_m(val: str, field_length: int) -> str:
    """左詰して残りは半角スペース(半角・全角混在可)

    :param val: 文字列
    :type val: str
    :param field_length: フィールド長
    :type field_length: int
    :return: 固定長文字列(UTF-8)
    :rtype: str
    """

    byte = 0
    r = ""
    for ch in val:
        ch_len = len(ch.encode('cp932'))
        if ch_len + byte <= field_length:
            r += ch
            byte += ch_len
        else:
            r += ' '
            byte += 1

        if byte >= field_length:
            break

    while byte < field_length:
        r += " "
        byte += 1

    return r


def convert_with_9(val: str, field_length: int) -> str:
    """前ゼロ(半角)をつけて右詰

    :param val: 文字列
    :type val: str
    :param field_length: フィールド長
    :type field_length: int
    :return: 固定長文字列(UTF-8)
    :rtype: str
    """
    val = moji.zen_to_han(val)
    r = field_length * '0' + val
    r = r[-field_length:]

    return r


def convert_with_z(val: str, field_length: int) -> str:
    """前スペース(半角)をつけて右詰

    :param val: 文字列
    :type val: str
    :param field_length: フィールド長
    :type field_length: int
    :return: 固定長文字列(UTF-8)
    :rtype: str
    """
    val = moji.zen_to_han(val)
    r = field_length * ' ' + val
    r = r[-field_length:]

    return r


def _get_byte_length(text: str) -> int:
    length = 0
    for c in text:
        if unicodedata.east_asian_width(c) in 'FWA':
            length += 2
        else:
            length += 1
    return length
