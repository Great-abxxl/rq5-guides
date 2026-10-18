#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""anchorgen — Logline 社区 anchor 重签工具（离线版）。

用法：python anchorgen.py [schema_version]        （默认 2）
输出：v2 anchor 十六进制串（写入 config 的 "anchor" 字段）。

注：算法逆向自 2.4 运行时的签名校验逻辑；仅供 LogHarvest 自托管实例救援使用。
"""
import hashlib
import hmac
import sys

KEY = b"LG-COMM-3E58-B7D0"


def main():
    sv = sys.argv[1] if len(sys.argv) > 1 else "2"
    print(hmac.new(KEY, f"logharvest/anchor/v{sv}".encode(), hashlib.sha256).hexdigest())


if __name__ == "__main__":
    main()
