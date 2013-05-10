import os
import sublime_plugin
import webbrowser
import urllib2
import re

class QuickOpenRailsViewsCommand(sublime_plugin.WindowCommand):

  def localhost_url(self, current_file):
    VIEW_DIR = os.path.join('app', 'views')
    start = current_file.find(VIEW_DIR)
    end = current_file.find('erb')
    if (start == -1 or end == -1):
      return None

    localhost_url = "http://localhost:3000/" + current_file[start + 10 : end - 6]
    if localhost_url.endswith("index"):
      localhost_url = localhost_url[:-5]

    if localhost_url.endswith("show"):
      localhost_url = localhost_url[:-4] + "1"

    if localhost_url.endswith("mobile"):
      localhost_url = localhost_url[:-7]

    return localhost_url

  def run(self):
    # find current file's path
    view = self.window.active_view()
    if view:
      current_file = view.file_name()
      url = self.localhost_url(current_file)
      if url:
        webbrowser.get('open -a /Applications/Firefox.app %s').open_new_tab(url)
