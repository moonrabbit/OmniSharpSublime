import os
import sublime
import sublime_plugin

from ..lib import helpers
from ..lib import omnisharp

class SwapServerClosure():
    def __init__(self, list):
        self.list = list

    def cb(self, index):
        settings = sublime.load_settings('OmniSharpSublime.sublime-settings')
        settings.set("omnisharp_server_active", self.list[index])
        print(settings)
        sublime.save_settings('OmniSharpSublime.sublime-settings')


class OmniSharpSelectVersion(sublime_plugin.TextCommand):
    def run(self, edit):
        view = helpers.active_view()
        active = helpers.get_settings(view, "omnisharp_server_active")
        servers = helpers.get_settings(view, "omnisharp_servers")

        popup_list = []
        for server in servers:
            popup_list.append(server.get("name"))

        view.show_popup_menu(popup_list, SwapServerClosure(popup_list).cb)