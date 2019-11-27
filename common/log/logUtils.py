import logging

import time
import os

ENDL = "\n" if os.name == "posix" else "\r\n"

def cm(message):
	"""
	CM logging (with logging)

	:param message: the message to log
	:return:
	"""

def warning(message):
	logging.warning(message)


def error(message):
	logging.error(message)


def info(message):
	logging.info(message)


def debug(message):
	logging.debug(message)


def rap(userID, message, through="FokaBot"):
	"""
	Log a message to Admin Logs.

	:param userID: admin user ID
	:param message: message content, without username
	:param through: through string. Default: FokaBot
	:return:
	"""
	import common.ripple
	import objects.glob
	objects.glob.db.execute("INSERT INTO rap_logs (id, userid, text, datetime, through) VALUES (NULL, %s, %s, %s, %s)", [userID, message, int(time.time()), through])
	username = common.ripple.userUtils.getUsername(userID)

LEVELS_MAPPING = {
	"warning": warning,
	"info": info,
	"error": error
}