# -*- coding: utf-8 -*-
"""
	B99scrapers Module
"""

from sys import argv
from urllib.parse import parse_qsl
from B99scrapers import sources_B99scrapers
from B99scrapers.modules import control

params = dict(parse_qsl(argv[2].replace('?', '')))
action = params.get('action')
mode = params.get('mode')
query = params.get('query')
name = params.get('name')

if action is None:
	control.openSettings('0.0', 'script.module.B99scrapers')

if action == "B99ScrapersSettings":
	control.openSettings('0.0', 'script.module.B99scrapers')

elif mode == "B99ScrapersSettings":
	control.openSettings('0.0', 'script.module.B99scrapers')

elif action == 'ShowChangelog':
	from B99scrapers.modules import changelog
	changelog.get()

elif action == 'ShowHelp':
	from B99scrapers.help import help
	help.get(name)

elif action == "Defaults":
	sourceList = []
	sourceList = sources_B99scrapers.all_providers
	for i in sourceList:
		source_setting = 'provider.' + i
		value = control.getSettingDefault(source_setting)
		control.setSetting(source_setting, value)

elif action == "toggleAll":
	sourceList = []
	sourceList = sources_B99scrapers.all_providers
	for i in sourceList:
		source_setting = 'provider.' + i
		control.setSetting(source_setting, params['setting'])

elif action == "toggleAllHosters":
	sourceList = []
	sourceList = sources_B99scrapers.hoster_providers
	for i in sourceList:
		source_setting = 'provider.' + i
		control.setSetting(source_setting, params['setting'])

elif action == "toggleAllTorrent":
	sourceList = []
	sourceList = sources_B99scrapers.torrent_providers
	for i in sourceList:
		source_setting = 'provider.' + i
		control.setSetting(source_setting, params['setting'])

elif action == "toggleAllPackTorrent":
	control.execute('RunPlugin(plugin://script.module.B99scrapers/?action=toggleAllTorrent&amp;setting=false)')
	control.sleep(500)
	sourceList = []
	from B99scrapers import pack_sources
	sourceList = pack_sources()
	for i in sourceList:
		source_setting = 'provider.' + i
		control.setSetting(source_setting, params['setting'])

elif action == 'openMyAccount':
	from myaccounts import openMASettings
	openMASettings('0.0')
	control.sleep(500)
	while control.condVisibility('Window.IsVisible(addonsettings)') or control.homeWindow.getProperty('myaccounts.active') == 'true':
		control.sleep(500)
	control.sleep(100)
	control.syncMyAccounts()
	control.sleep(100)
	if params.get('opensettings') == 'true':
		control.openSettings(query, 'script.module.B99scrapers')

elif action == 'syncMyAccount':
	control.syncMyAccounts()
	if params.get('opensettings') == 'true':
		control.openSettings(query, 'script.module.B99scrapers')

elif action == 'cleanSettings':
	control.clean_settings()

elif action == 'undesirablesSelect':
	from B99scrapers.modules.undesirables import undesirablesSelect
	undesirablesSelect()

elif action == 'undesirablesInput':
	from B99scrapers.modules.undesirables import undesirablesInput
	undesirablesInput()

elif action == 'undesirablesUserRemove':
	from B99scrapers.modules.undesirables import undesirablesUserRemove
	undesirablesUserRemove()

elif action == 'undesirablesUserRemoveAll':
	from B99scrapers.modules.undesirables import undesirablesUserRemoveAll
	undesirablesUserRemoveAll()

elif action == 'tools_clearLogFile':
	from B99scrapers.modules import log_utils
	cleared = log_utils.clear_logFile()
	if cleared == 'canceled': pass
	elif cleared: control.notification(message='B99Scrapers Log File Successfully Cleared')
	else: control.notification(message='Error clearing B99Scrapers Log File, see kodi.log for more info')

elif action == 'tools_viewLogFile':
	from B99scrapers.modules import log_utils
	log_utils.view_LogFile(name)

elif action == 'tools_uploadLogFile':
	from B99scrapers.modules import log_utils
	log_utils.upload_LogFile()
