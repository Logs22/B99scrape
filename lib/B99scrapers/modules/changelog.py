# -*- coding: utf-8 -*-
"""
	B99scrapers Module
"""

from B99scrapers.modules.control import addonPath, addonVersion, joinPath
from B99scrapers.windows.textviewer import TextViewerXML


def get():
	B99scrapers_path = addonPath()
	B99scrapers_version = addonVersion()
	changelogfile = joinPath(B99scrapers_path, 'changelog.txt')
	r = open(changelogfile, 'r', encoding='utf-8', errors='ignore')
	text = r.read()
	r.close()
	heading = '[B]B99Scrapers -  v%s - ChangeLog[/B]' % B99scrapers_version
	windows = TextViewerXML('textviewer.xml', B99scrapers_path, heading=heading, text=text)
	windows.run()
	del windows