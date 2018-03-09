---
title: pelican
date: 2015-06-17
update: 2015-07-12 19:35:16
---

修改配置文件后一定要在 ia 上测试。

## commands 
	pelican content --output output --relative-urls --ignore-cache
	make html
	make serve
	make s3_upload
	
	
	$ pelican --help
	usage: pelican [-h] [-t THEME] [-o OUTPUT] [-s SETTINGS] [-d] [-v] [-q] [-D]
	               [--version] [-r] [--relative-urls] [--cache-path CACHE_PATH]
	               [--ignore-cache] [-w SELECTED_PATHS]
	               [path]
	
	A tool to generate a static blog, with restructured text input files.
	
	positional arguments:
	  path                  Path where to find the content files. (default: None)
	
	optional arguments:
	  -h, --help            show this help message and exit
	  -t THEME, --theme-path THEME
	                        Path where to find the theme templates. If not
	                        specified, it will use the default one included with
	                        pelican. (default: None)
	  -o OUTPUT, --output OUTPUT
	                        Where to output the generated files. If not specified,
	                        a directory will be created, named "output" in the
	                        current path. (default: None)
	  -s SETTINGS, --settings SETTINGS
	                        The settings of the application, this is automatically
	                        set to pelicanconf.py if a file exists with this name.
	                        (default: None)
	  -d, --delete-output-directory
	                        Delete the output directory. (default: None)
	  -v, --verbose         Show all messages. (default: None)
	  -q, --quiet           Show only critical errors. (default: None)
	  -D, --debug           Show all messages, including debug messages. (default:
	                        None)
	  --version             Print the pelican version and exit.
	  -r, --autoreload      Relaunch pelican each time a modification occurs on
	                        the content files. (default: False)
	  --relative-urls       Use relative urls in output, useful for site
	                        development (default: False)
	  --cache-path CACHE_PATH
	                        Directory in which to store cache files. If not
	                        specified, defaults to "cache". (default: None)
	  --ignore-cache        Ignore content cache from previous runs by not loading
	                        cache files. (default: False)
	  -w SELECTED_PATHS, --write-selected SELECTED_PATHS
	                        Comma separated list of selected paths to write
	                        (default: None)


