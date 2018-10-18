# -*- coding: cp1254 -*-
# please visit http://www.iptvxtra.net

import xbmc,xbmcgui,xbmcplugin,sys
icondir = xbmc.translatePath("special://home/addons/plugin.audio.radiofsn/icons/")
plugin_handle = int(sys.argv[1])

def add_video_item(url, infolabels, img=''):
    listitem = xbmcgui.ListItem(infolabels['title'], iconImage=img, thumbnailImage=img)
    listitem.setInfo('video', infolabels)
    listitem.setProperty('IsPlayable', 'true')
    xbmcplugin.addDirectoryItem(plugin_handle, url, listitem, isFolder=False)

add_video_item('http://stream.radio-fsn.de:8000/rock',{ 'title': ''},img=icondir + 'rock.png')
add_video_item('http://stream.radio-fsn.de:8000/balladen',{ 'title': ''},img=icondir + 'balladen.png')
add_video_item('http://stream.radio-fsn.de:8000/hardcore',{ 'title': ''},img=icondir + 'hardcore.png')
add_video_item('http://stream.radio-fsn.de:8000/blackmetal',{ 'title': ''},img=icondir + 'nsbm.png')

xbmcplugin.endOfDirectory(plugin_handle)
xbmc.executebuiltin("Container.SetViewMode(500)")