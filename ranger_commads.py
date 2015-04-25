# comandos propios para Ranger:

class xh(Command):
    def execute(self):
        self.fm.run('file-roller -h "' + self.fm.thisfile.path + '"', flags='f')

class compress(Command):
    def execute(self):
        self.fm.run("file-roller -d " + files(self), flags='f')

class trash(Command):
    def execute(self):
        self.fm.run("trash " + files(self), flags='f')
        self.fm.reload_cwd()

class duplicate(Command):
    def execute(self):
        import datetime
        import shutil
        shutil.copyfile(self.fm.thisfile.path, self.fm.thisfile.path + \
            datetime.datetime.now().strftime("_%Y-%m-%d_%H%M%S"))

def files(command):
    return '"' + '" "'.join(
        [f.basename for f in command.fm.thistab.get_selection()]) + '"'
