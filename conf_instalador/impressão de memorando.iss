
#define MyAppName "Impressão de memorandos"
#define MyAppVersion "1.1"
#define MyAppPublisher "Ogliari"
#define MyAppURL "https://github.com/casa-inteligente"
#define MyAppSupport "https://github.com/casa-inteligente/pdf_to_print/issues/17"
#define MyAppExeName "print_memorando.exe"
#define MyAppAssocName MyAppName + " File"
#define MyAppAssocExt ".myp"
#define MyAppAssocKey StringChange(MyAppAssocName, " ", "") + MyAppAssocExt

#define PathApp "C:\Users\AULA-1\Documents\GitHub\pdf_to_print"

[Setup]
; NOTE: The value of AppId uniquely identifies this application. Do not use the same AppId value in installers for other applications.
; (To generate a new GUID, click Tools | Generate GUID inside the IDE.)
AppId={{9DF56F94-71E4-47F8-A99F-BA3659EBD296}
AppName={#MyAppName}
AppVersion={#MyAppVersion}
;AppVerName={#MyAppName} {#MyAppVersion}
AppPublisher={#MyAppPublisher}
AppPublisherURL={#MyAppURL}
AppSupportURL={#MyAppSupport}
AppUpdatesURL={#MyAppURL}
;DefaultDirName={autopf}\{#MyAppName}
DefaultDirName={autopf}\{#MyAppPublisher}\{#MyAppName}
ChangesAssociations=yes
DisableProgramGroupPage=yes
LicenseFile={#PathApp}\LICENSE
InfoBeforeFile={#PathApp}\conf_instalador\Antes.txt
InfoAfterFile={#PathApp}\conf_instalador\Depois.txt
; Remove the following line to run in administrative install mode (install for all users.)
PrivilegesRequired=lowest
OutputDir={#PathApp}\conf_instalador\instalador
OutputBaseFilename=Impressão de memorandos
SetupIconFile={#PathApp}\figure\este.ico
Compression=lzma
SolidCompression=yes
WizardStyle=modern

[Languages]
;Name: "english"; MessagesFile: "compiler:Default.isl"
Name: "brazilianportuguese"; MessagesFile: "compiler:Languages\BrazilianPortuguese.isl"

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: checkedonce

[Files]
Source: "C:\Users\AULA-1\Documents\GitHub\pdf_to_print\dist\print_memorando\{#MyAppExeName}"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\AULA-1\Documents\GitHub\pdf_to_print\dist\print_memorando\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs
; NOTE: Don't use "Flags: ignoreversion" on any shared system files

[Registry]
Root: HKA; Subkey: "Software\Classes\{#MyAppAssocExt}\OpenWithProgids"; ValueType: string; ValueName: "{#MyAppAssocKey}"; ValueData: ""; Flags: uninsdeletevalue
Root: HKA; Subkey: "Software\Classes\{#MyAppAssocKey}"; ValueType: string; ValueName: ""; ValueData: "{#MyAppAssocName}"; Flags: uninsdeletekey
Root: HKA; Subkey: "Software\Classes\{#MyAppAssocKey}\DefaultIcon"; ValueType: string; ValueName: ""; ValueData: "{app}\{#MyAppExeName},0"
Root: HKA; Subkey: "Software\Classes\{#MyAppAssocKey}\shell\open\command"; ValueType: string; ValueName: ""; ValueData: """{app}\{#MyAppExeName}"" ""%1"""
Root: HKA; Subkey: "Software\Classes\Applications\{#MyAppExeName}\SupportedTypes"; ValueType: string; ValueName: ".myp"; ValueData: ""

[Icons]
Name: "{autoprograms}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"
Name: "{autodesktop}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"; Tasks: desktopicon

[Run]
Filename: "{app}\{#MyAppExeName}"; Description: "{cm:LaunchProgram,{#StringChange(MyAppName, '&', '&&')}}"; Flags: nowait postinstall skipifsilent

