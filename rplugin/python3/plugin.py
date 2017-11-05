import neovim
import os

@neovim.plugin
class Main(object):
    def __init__(self, nvim):
        self.nvim = nvim

    # Moves notes from mobile inbox to inbox.
    @neovim.function('MoveMobileInbox')
    def moveMobileInbox(self, args):
        mobile_inbox = os.environ["MOBILE_INBOX_FILE"]
        self.nvim.command('echo "Moving mobile inbox {}"'.format(mobile_inbox))

        def process_line(line):
            return '*' + line.strip()

        with open(mobile_inbox, 'r+') as f:
            lines = f.readlines()
            if len(lines):
                self.nvim.current.buffer.append([process_line(line) for line in lines])
                f.seek(0)
                f.truncate()
