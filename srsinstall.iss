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
Source: "C:\Users\Alex Edwards\Desktop\VBox Shared Folder\python-3.13.2-amd64.exe"; DestDir: "{localappdata}\SRSBot\bot_files"; Flags: ignoreversion
Source: "C:\Users\Alex Edwards\Documents\GitHub\SRSBot\install_requirements.bat"; DestDir: "{localappdata}\SRSBot\bot_files"; Flags: ignoreversion

[Dirs]
Name: "{localappdata}\SRSBot\Updater"

[Icons]
Name: "{group}\SRSBot Launcher"; Filename: "{localappdata}\SRSBot\bot_files\Launcher.exe"
Name: "{commondesktop}\SRSBot Launcher"; Filename: "{localappdata}\SRSBot\bot_files\Launcher.exe"; IconFilename: "{localappdata}\SRSBot\bot_files\Imagery\boticon.ico"

[Run]
Filename: "{localappdata}\SRSBot\bot_files\Launcher.exe"; Description: "Launch SRSBot"; Flags: nowait postinstall skipifsilent

[Code]
const
  SMTO_ABORTIFHUNG = 2;
  WM_SETTINGCHANGE = $1A;

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

procedure DeinitializeSetup;
var
  ResultCode: Integer;
begin
  if FileExists(ExpandConstant('{localappdata}\SRSBot\bot_files\python-3.13.2-amd64.exe')) then
  begin
    ShellExec('', ExpandConstant('{localappdata}\SRSBot\bot_files\python-3.13.2-amd64.exe'), '', '', SW_SHOWNORMAL, ewWaitUntilTerminated, ResultCode);
    MsgBox('Please follow the instructions in the Python installer. Make sure to check the "Add Python to PATH" option. If you already have Python installed, you can cancel the installation.', mbInformation, MB_OK);
    ShellExec('', 'cmd.exe', '/C {localappdata}\SRSBot\bot_files\install_requirements.bat', '', SW_SHOWNORMAL, ewWaitUntilTerminated, ResultCode);
  end;
end;