# -*- coding: utf-8 -*-

# Widget que representa las tres columnas del Home en Turpial
#
# Author: Wil Alvarez (aka Satanas)
# Jun 03, 2010

from turpial.ui.gtk.columns import StandardColumn
from turpial.ui.gtk.wrapper import Wrapper, WrapperAlign

try:
    import webkit
    from turpial.ui.gtk.tweetslistwk import TweetListWebkit
except:
    pass
    
class Home(Wrapper):
    def __init__(self, mainwin, mode='single'):
        Wrapper.__init__(self)
        
        if mainwin.extend:
            self.timeline = TweetListWebkit(mainwin, 'Timeline')
            self.replies = TweetListWebkit(mainwin, _('Mentions'))
        else:
            self.timeline = StandardColumn(mainwin, _('Timeline'), 
                id='timeline', marknew=True)
            self.replies = StandardColumn(mainwin, _('Mentions'), id='replies')
        self.direct = StandardColumn(mainwin, _('Directs'), 'direct', 
            id='directs')
        
        self._append_widget(self.timeline, WrapperAlign.left)
        self._append_widget(self.replies, WrapperAlign.middle)
        self._append_widget(self.direct, WrapperAlign.right)
        
        self.change_mode(mode)
