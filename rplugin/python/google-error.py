import urllib
import webbrowser
import neovim

@neovim.plugin
class Main(object):
    def __init__(self, vim):
        self.vim = vim

    @neovim.function('GoogleError')
    def google_error(self, args):
        error = self.vim.command_output('1 messages')
        query =  { 'q': error}
        webbrowser.open('https://www.google.com/search?{}'.format(urllib.urlencode(query)), new=2)

