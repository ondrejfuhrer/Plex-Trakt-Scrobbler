import sys

# submodules for Plex plugins "hack"

import model
sys.modules['data.model'] = model

import sync_status
sys.modules['data.sync_status'] = sync_status

import watch_session
sys.modules['data.watch_session'] = watch_session
