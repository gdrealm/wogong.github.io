title: everything
date: 2015-06-17
modified: 2015-07-13 22:48:14


open_folder_command2=$exec("%1")
open_file_command2=$exec("%1")
open_path_command2=$exec("%SystemRoot%\explorer.exe" /select,"%1")

open_path_command2=$exec(“c:\Program Files\totalcmd\TOTALCMD.EXE” “$parent(%1)”)
open_folder_command2=$exec(“c:\Program Files\totalcmd\TOTALCMD.EXE” “%1″)

http://xbeta.info/everything-tc.htm

调用第三方资源管理器


