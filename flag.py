from hashlib import md5
from zlib import crc32

salt = b'salt'

FLAG = "FLAG{this_is_an_example_flag" + str(crc32(salt)) + "}"

