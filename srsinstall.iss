[Setup]
AppName=SRSBot
AppVersion=1.0
DefaultDirName={localappdata}\SRSBot
DefaultGroupName=SRSBot
OutputDir=C:\Users\Alex Edwards\Desktop\VBox Shared Folder
OutputBaseFilename=SRSBotInstaller
Compression=lzma
SolidCompression=yes

[Files]
Source: "C:\Users\Alex Edwards\Documents\GitHub\SRSBot\dist\Launcher.exe"; DestDir: "{localappdata}\SRSBot\bot_files"; Flags: ignoreversion
Source: "C:\Users\Alex Edwards\Documents\GitHub\SRSBot\Launcher.spec"; DestDir: "{localappdata}\SRSBot\bot_files"; Flags: ignoreversion
Source: "C:\Users\Alex Edwards\Documents\GitHub\SRSBot\Launcher.py"; DestDir: "{localappdata}\SRSBot\bot_files"; Flags: ignoreversion
Source: "C:\Users\Alex Edwards\Documents\GitHub\SRSBot\Verifier.py"; DestDir: "{localappdata}\SRSBot\bot_files"; Flags: ignoreversion
Source: "C:\Users\Alex Edwards\Documents\GitHub\SRSBot\srsenv\*"; DestDir: "{localappdata}\SRSBot\bot_files\srsenv"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "C:\Users\Alex Edwards\Documents\GitHub\SRSBot\imagery\boticon.ico"; DestDir: "{localappdata}\SRSBot\bot_files\Imagery"; Flags: ignoreversion
Source: "C:\Users\Alex Edwards\Documents\GitHub\SRSBot\imagery\SRSLogo.ico"; DestDir: "{localappdata}\SRSBot\bot_files\Imagery"; Flags: ignoreversion
Source: "C:\Users\Alex Edwards\Documents\GitHub\SRSBot\imagery\SRS Discord Logo.png"; DestDir: "{localappdata}\SRSBot\bot_files\Imagery"; Flags: ignoreversion
Source: "C:\Users\Alex Edwards\Documents\GitHub\SRSBot\imagery\SRS Logo Official.jpg"; DestDir: "{localappdata}\SRSBot\bot_files\Imagery"; Flags: ignoreversion
Source: "C:\Users\Alex Edwards\Documents\GitHub\SRSBot\python\*"; DestDir: "{localappdata}\SRSBot\python"; Flags: ignoreversion recursesubdirs createallsubdirs

[Dirs]
Name: "{localappdata}\SRSBot\Updater"

[Icons]
Name: "{group}\SRSBot Launcher"; Filename: "{localappdata}\SRSBot\bot_files\Launcher.exe"
Name: "{commondesktop}\SRSBot Launcher"; Filename: "{localappdata}\SRSBot\bot_files\Launcher.exe"; IconFilename: "{localappdata}\SRSBot\bot_files\Imagery\boticon.ico"

[Run]
Filename: "{localappdata}\SRSBot\bot_files\Launcher.exe"; Description: "Launch SRSBot"; Flags: nowait postinstall skipifsilent