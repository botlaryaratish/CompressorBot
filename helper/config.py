#    This file is part of the Compressor distribution.
#    Copyright (c) Binary Tech
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, version 3.
#
#    This program is distributed in the hope that it will be useful, but
#    WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
#    General Public License for more details.



from . import *

try:
    APP_ID = config("10663626", cast=int)
    API_HASH = config("5685a6aabd0f5ab31a75ab2b096bfd43")
    BOT_TOKEN = config("5367344283:AAGWSfBqa269dZih3GyPzv0bcmvZ65TQ4_E")
    OWNER = config("5175012041", cast=int)
    LOG = config("-1001170224733", cast=int)
except Exception as e:
    LOGS.info("Environment vars Missing")
    LOGS.info("something went wrong")
    LOGS.info(str(e))
    exit(1)
