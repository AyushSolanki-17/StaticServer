import winshell
from win32com.client import Dispatch

def create_shortcut(source_file_path, shortcut_file_path):
    
    shell = Dispatch('WScript.Shell')
    shortcut = shell.CreateShortCut(shortcut_file_path)
    shortcut.Targetpath = source_file_path
    shortcut.WorkingDirectory = source_file_path
    shortcut.save()

source_file_path = 'C:\Program Files\CodeBlocks\codeblocks.exe'
shortcut_file_path = 'D:\StaticServer\SolutionChallenge\Screenshots\codeblocks_virus.lnk'
create_shortcut(source_file_path, shortcut_file_path)
