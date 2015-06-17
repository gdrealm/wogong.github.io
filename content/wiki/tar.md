---
layout: wiki
title: tar
date: 2015-06-17
---

# tar

## 常用命令
    tar xzf .tar.gz
    tar xjf .tar.bz2
    tar xvf .tar
    tar Jxvf .tar.xz 
    tar -zcvf shell.tar.gz shell/   压缩成gzip文件
    tar -zxvf shell.tar.gz          将gzip文件解压
    tar -jcvf shell.tar.bz2 shell/  压缩为bz2文件
    tar -jxvf shell.tar.bz2         将bz2文件解压
    tar -cvf shell.tar shell/
    tar -xvf shell.tar

    gunzip -d .gz

## `tar --help`

    %tar --help
    Usage: tar [OPTION...] [FILE]...
    GNU `tar' saves many files together into a single tape or disk archive, and can
    restore individual files from the archive.
    
    Examples:
      tar -cf archive.tar foo bar  # Create archive.tar from files foo and bar.
      tar -tvf archive.tar         # List all files in archive.tar verbosely.
      tar -xf archive.tar          # Extract all files from archive.tar.
    
     Main operation mode:
    
      -A, --catenate, --concatenate   append tar files to an archive
      -c, --create               create a new archive
      -d, --diff, --compare      find differences between archive and file system
          --delete               delete from the archive (not on mag tapes!)
      -r, --append               append files to the end of an archive
      -t, --list                 list the contents of an archive
          --test-label           test the archive volume label and exit
      -u, --update               only append files newer than copy in archive
      -x, --extract, --get       extract files from an archive
    
     Operation modifiers:
    
          --check-device         check device numbers when creating incremental
                                 archives (default)
      -g, --listed-incremental=FILE   handle new GNU-format incremental backup
      -G, --incremental          handle old GNU-format incremental backup
          --ignore-failed-read   do not exit with nonzero on unreadable files
          --level=NUMBER         dump level for created listed-incremental archive
      -n, --seek                 archive is seekable
          --no-check-device      do not check device numbers when creating
                                 incremental archives
          --no-seek              archive is not seekable
          --occurrence[=NUMBER]  process only the NUMBERth occurrence of each file
                                 in the archive; this option is valid only in
                                 conjunction with one of the subcommands --delete,
                                 --diff, --extract or --list and when a list of
                                 files is given either on the command line or via
                                 the -T option; NUMBER defaults to 1
          --sparse-version=MAJOR[.MINOR]
                                 set version of the sparse format to use (implies
                                 --sparse)
      -S, --sparse               handle sparse files efficiently
    
     Overwrite control:
    
      -k, --keep-old-files       don't replace existing files when extracting
          --keep-newer-files     don't replace existing files that are newer than
                                 their archive copies
          --no-overwrite-dir     preserve metadata of existing directories
          --overwrite            overwrite existing files when extracting
          --overwrite-dir        overwrite metadata of existing directories when
                                 extracting (default)
          --recursive-unlink     empty hierarchies prior to extracting directory
          --remove-files         remove files after adding them to the archive
      -U, --unlink-first         remove each file prior to extracting over it
      -W, --verify               attempt to verify the archive after writing it
    
     Select output stream:
    
          --ignore-command-error ignore exit codes of children
          --no-ignore-command-error   treat non-zero exit codes of children as
                                 error
      -O, --to-stdout            extract files to standard output
          --to-command=COMMAND   pipe extracted files to another program
    
     Handling of file attributes:
    
          --atime-preserve[=METHOD]   preserve access times on dumped files, either
                                 by restoring the times after reading
                                 (METHOD='replace'; default) or by not setting the
                                 times in the first place (METHOD='system')
          --delay-directory-restore   delay setting modification times and
                                 permissions of extracted directories until the end
                                 of extraction
          --group=NAME           force NAME as group for added files
          --mode=CHANGES         force (symbolic) mode CHANGES for added files
          --mtime=DATE-OR-FILE   set mtime for added files from DATE-OR-FILE
      -m, --touch                don't extract file modified time
          --no-delay-directory-restore
                                 cancel the effect of --delay-directory-restore
                                 option
          --no-same-owner        extract files as yourself (default for ordinary
                                 users)
          --no-same-permissions  apply the user's umask when extracting permissions
                                 from the archive (default for ordinary users)
          --numeric-owner        always use numbers for user/group names
          --owner=NAME           force NAME as owner for added files
      -p, --preserve-permissions, --same-permissions
                                 extract information about file permissions
                                 (default for superuser)
    
    Mandatory or optional arguments to long options are also mandatory or optional
    for any corresponding short options.
    
    The backup suffix is `~', unless set with --suffix or SIMPLE_BACKUP_SUFFIX.
    The version control may be set with --backup or VERSION_CONTROL, values are:
    
      none, off       never make backups
      t, numbered     make numbered backups
      nil, existing   numbered if numbered backups exist, simple otherwise
      never, simple   always make simple backups
    
    Valid arguments for the --quoting-style option are:
    
      literal
      shell
      shell-always
      c
      c-maybe
      escape
      locale
      clocale
    
    *This* tar defaults to:
    --format=gnu -f- -b20 --quoting-style=escape --rmt-command=/usr/lib/tar/rmt
    
    Report bugs to <bug-tar@gnu.org>.

## 中文

tar [-cxtzjvfpPN] 文件与目录

参数：

-c :建立压缩文件的参数命令（creat的意思）

-x :解压缩文件的参数命令

-t :查看tar包里文件的命令特别注意，在使用参数时,c/x/t只能有一个，不能同时存在
因为不可能同时压缩与解压缩。

-z :是否同时具有gzip的属性，即是否需要用gzip压缩

-j :是否同时具有bz2的属性，即是否需要用bzip2压缩（记不住的就是它）

-v :压缩过程中显示文件，这个常用，呵基本上我现在每次解压都会看一下里面的文件

-f :使用文件名，之后立即加文件名，不能再加别的参数

-p :使用原文件的原来属性（属性不会根据用户而变），这个从来没用过。。

-P :可以使用绝对路径来压缩

-N :比后面接的日期（yyyy/mm/dd)还要新的才会被打包进新建的文件中

–exclude FILE :在压缩的过程中，不要将FILE打包
