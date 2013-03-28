# coding=utf8
import sublime, sublime_plugin

class EncodingPlugin(sublime_plugin.EventListener):
    def __init__(self):
        return
    def on_load(self, view):
        self.update_encoding(view)
    def on_post_save(self, view):
    	self.update_encoding(view)

    def update_encoding(self, view):
    	view.set_status('ShowEncodingPluginStatus', view.encoding() if view.encoding() != u'Undefined' else sublime.load_settings('Preferences.sublime-settings').get('default_encoding', 'Unknown Encoding'))
