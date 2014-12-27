# comandos propios para Ranger:

class xh(Command):
    """'Extract here' para archivos comprimidos."""
    def execute(self):
        self.fm.run('file-roller -h "' + self.fm.thisfile.path + '"', flags='f')

class compress(Command):
    """Comprime los archivos seleccionados."""
    def execute(self):
        self.fm.run("file-roller -d " + files(self), flags='f')

class trash(Command):
    """Elimina los archivos seleccionados a la papelera."""
    def execute(self):
        self.fm.run("trash " + files(self), flags='f')
        self.fm.reload_cwd()

def files(command):
    return '"' + '" "'.join(
        [f.basename for f in command.fm.thistab.get_selection()]) + '"'
