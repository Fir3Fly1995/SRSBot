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
Source: "C:\Users\Alex Edwards\Documents\GitHub\SRSBot\build\exe.win-amd64-3.8\Launcher.exe"; DestDir: "{localappdata}\SRSBot\dist"; Flags: ignoreversion
Source: "C:\Users\Alex Edwards\Documents\GitHub\SRSBot\build\exe.win-amd64-3.8\Package_manager.exe"; DestDir: "{localappdata}\SRSBot\dist"; Flags: ignoreversion
Source: "C:\Users\Alex Edwards\Documents\GitHub\SRSBot\build\exe.win-amd64-3.8\SRS_Recover.exe"; DestDir: "{localappdata}\SRSRecovery"; Flags: ignoreversion
Source: "C:\Users\Alex Edwards\Documents\GitHub\SRSBot\Verifier.py"; DestDir: "{localappdata}\SRSBot"; Flags: ignoreversion
Source: "C:\Users\Alex Edwards\Documents\GitHub\SRSBot\srs_env\*"; DestDir: "{localappdata}\SRSBot\srs_env"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "C:\Users\Alex Edwards\Documents\GitHub\SRSBot\Imagery\BotIcon.ico"; DestDir: "{localappdata}\SRSBot\Imagery"; Flags: ignoreversion
Source: "C:\Users\Alex Edwards\Documents\GitHub\SRSBot\Imagery\SRS Discord Logo.png"; DestDir: "{localappdata}\SRSBot\Imagery"; Flags: ignoreversion
Source: "C:\Users\Alex Edwards\Documents\GitHub\SRSBot\Imagery\SRS Logo Official.jpg"; DestDir: "{localappdata}\SRSBot\Imagery"; Flags: ignoreversion
Source: "C:\Users\Alex Edwards\Documents\GitHub\SRSBot\Imagery\SRSLogo.ico"; DestDir: "{localappdata}\SRSBot\Imagery"; Flags: ignoreversion

[Dirs]
Name: "{localappdata}\SRSBot\Updater"
Name: "{localappdata}\SRSBot\Log_Files"

[Icons]
Name: "{group}\SRSBot Launcher"; Filename: "{localappdata}\SRSBot\dist\Launcher.exe"
Name: "{commondesktop}\SRSBot Launcher"; Filename: "{localappdata}\SRSBot\dist\Launcher.exe"; IconFilename: "{localappdata}\SRSBot\Imagery\BotIcon.ico"

[Run]
Filename: "{localappdata}\SRSBot\dist\Launcher.exe"; Description: "Launch SRSBot"; Flags: nowait postinstall skipifsilent

[UninstallDelete]
Type: files; Name: "{localappdata}\SRSBot\dist\Launcher.exe"
Type: files; Name: "{localappdata}\SRSBot\dist\Package_manager.exe"
Type: files; Name: "{localappdata}\SRSRecovery\SRS_Recover.exe"
Type: files; Name: "{localappdata}\SRSBot\Verifier.py"
Type: files; Name: "{localappdata}\SRSBot\srs_env\*"
Type: files; Name: "{localappdata}\SRSBot\Imagery\BotIcon.ico"
Type: files; Name: "{localappdata}\SRSBot\Imagery\SRS Discord Logo.png"
Type: files; Name: "{localappdata}\SRSBot\Imagery\SRS Logo Official.jpg"
Type: files; Name: "{localappdata}\SRSBot\Imagery\SRSLogo.ico"
Type: files; Name: "{localappdata}\SRSBot\Log_Files\*"
Type: dirifempty; Name: "{localappdata}\SRSBot\Updater"
Type: dirifempty; Name: "{localappdata}\SRSBot\Log_Files"
Type: dirifempty; Name: "{localappdata}\SRSBot\dist"
Type: dirifempty; Name: "{localappdata}\SRSBot\Imagery"
Type: dirifempty; Name: "{localappdata}\SRSBot\srs_env"
Type: dirifempty; Name: "{localappdata}\SRSBot"
Type: dirifempty; Name: "{localappdata}\SRSRecovery"

[Code]
const
  SMTO_ABORTIFHUNG = 2;
  WM_SETTINGCHANGE = $1A;

procedure CurStepChanged(CurStep: TSetupStep);
begin
  if CurStep = ssPostInstall then
  begin
    // Check for the presence of %localappdata%\Temp\SRSLog\rcvr.log
    if FileExists(ExpandConstant('{localappdata}\Temp\SRSLog\rcvr.log')) then
    begin
      // Ensure the destination directory exists
      if not DirExists(ExpandConstant('{localappdata}\SRSBot\Log_Files')) then
      begin
        CreateDir(ExpandConstant('{localappdata}\SRSBot\Log_Files'));
      end;

      // Move the rcvr.log file to %localappdata%\SRSBot\Log_Files\rcvr.log
      if not RenameFile(ExpandConstant('{localappdata}\Temp\SRSLog\rcvr.log'), ExpandConstant('{localappdata}\SRSBot\Log_Files\rcvr.log')) then
      begin
        MsgBox('Failed to move rcvr.log file.', mbError, MB_OK);
      end;

      // Delete the %localappdata%\Temp\SRSLog directory
      if not DelTree(ExpandConstant('{localappdata}\Temp\SRSLog'), True, True, True) then
      begin
        MsgBox('Failed to delete Temp\SRSLog directory.', mbError, MB_OK);
      end;
    end;
  end;
end;