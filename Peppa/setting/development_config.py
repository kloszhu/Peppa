#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/9 14:47
# @Author  : CoderCharm
# @File    : development_config.py
# @Software: PyCharm
# @Desc    :
"""

开发环境配置

"""
from typing import Union, Optional
from pydantic import AnyHttpUrl, BaseSettings, IPvAnyAddress


class Config(BaseSettings):
    # 文档地址
    DOCS_URL: str = "/api/docs"
    # # 文档关联请求数据接口
    OPENAPI_URL: str = "/api/openapi.json"
    # 禁用 redoc 文档
    REDOC_URL: Optional[str] = None

    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8
    SECRET_KEY: str = 'aeq)s(*&dWEQasd8**&^9asda_asdasd*&*&^+_sda'

    # 配置你的Mysql环境
    MYSQL_USERNAME: str = 'admin'
    MYSQL_PASSWORD: str = "admin1234"
    MYSQL_HOST: Union[AnyHttpUrl, IPvAnyAddress] = "121.4.203.2"
    MYSQL_DATABASE: str = 'Peppa'

    # Mysql地址
    SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{MYSQL_USERNAME}:{MYSQL_PASSWORD}@" \
                              f"{MYSQL_HOST}/{MYSQL_DATABASE}?charset=utf8mb4"


config = Config()
