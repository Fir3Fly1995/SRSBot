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
Source: "C:\Users\Alex Edwards\Documents\GitHub\SRSBot\Verifier.py"; DestDir: "{localappdata}\SRSBot\bot_files"; Flags: ignoreversion
Source: "C:\Users\Alex Edwards\Documents\GitHub\SRSBot\srs_env\*"; DestDir: "{localappdata}\SRSBot\bot_files\srs_env"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "C:\Users\Alex Edwards\Documents\GitHub\SRSBot\Start_bot.bat"; DestDir: "{localappdata}\SRSBot\bot_files"; Flags: ignoreversion
Source: "C:\Users\Alex Edwards\Documents\GitHub\SRSBot\imagery\boticon.ico"; DestDir: "{localappdata}\SRSBot\bot_files\Imagery"; Flags: ignoreversion
Source: "C:\Users\Alex Edwards\Documents\GitHub\SRSBot\imagery\SRSLogo.ico"; DestDir: "{localappdata}\SRSBot\bot_files\Imagery"; Flags: ignoreversion
Source: "C:\Users\Alex Edwards\Documents\GitHub\SRSBot\imagery\SRS Discord Logo.png"; DestDir: "{localappdata}\SRSBot\bot_files\Imagery"; Flags: ignoreversion
Source: "C:\Users\Alex Edwards\Documents\GitHub\SRSBot\imagery\SRS Logo Official.jpg"; DestDir: "{localappdata}\SRSBot\bot_files\Imagery"; Flags: ignoreversion
Source: "C:\Users\Alex Edwards\Documents\Python313\*"; DestDir: "C:\Program Files\Python313"; Flags: ignoreversion recursesubdirs createallsubdirs

[Dirs]
Name: "{localappdata}\SRSBot\Updater"

[Icons]
Name: "{group}\SRSBot Launcher"; Filename: "{localappdata}\SRSBot\bot_files\Launcher.exe"
Name: "{commondesktop}\SRSBot Launcher"; Filename: "{localappdata}\SRSBot\bot_files\Launcher.exe"; IconFilename: "{localappdata}\SRSBot\bot_files\Imagery\boticon.ico"

[Run]
Filename: "{localappdata}\SRSBot\bot_files\Launcher.exe"; Description: "Launch SRSBot"; Flags: nowait postinstall skipifsilent

[Code]
procedure AddPythonToPath;
var
  Path: string;
  PythonPath: string;
begin
  PythonPath := 'C:\Program Files\Python313';
  if RegQueryStringValue(HKEY_LOCAL_MACHINE, 'SYSTEM\CurrentControlSet\Control\Session Manager\Environment', 'Path', Path) then
  begin
    if Pos(PythonPath, Path) = 0 then
    begin
      Path := Path + ';' + PythonPath;
      RegWriteStringValue(HKEY_LOCAL_MACHINE, 'SYSTEM\CurrentControlSet\Control\Session Manager\Environment', 'Path', Path);
      SendMessageTimeout(HWND_BROADCAST, WM_SETTINGCHANGE, 0, LPARAM(PChar('Environment')), SMTO_ABORTIFHUNG, 5000, PDWORD(nil)^);
    end;
  end;
end;

procedure CurStepChanged(CurStep: TSetupStep);
begin
  if CurStep = ssPostInstall then
  begin
    AddPythonToPath;
  end;
end;