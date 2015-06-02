---
layout: wiki
title: jekyll
create: 2014-06-19
update: 2014-06-19
---
## install
sudo apt-get install ruby1.9.1-dev
sudo gem install jekyll
sudo gem install rdiscount
sudo gem install therubyracer

## usage
jekyll build -s source -d \_sites
jekyll serve --host 0.0.0.0 --port 4000


jekyll 2.5.3 -- Jekyll is a blog-aware, static site generator in Ruby

Usage:

  jekyll <subcommand> [options]

Options:
        -s, --source [DIR]  Source directory (defaults to ./)
        -d, --destination [DIR]  Destination directory (defaults to ./_site)
            --safe         Safe mode (defaults to false)
        -p, --plugins PLUGINS_DIR1[,PLUGINS_DIR2[,...]]  Plugins directory (defaults to ./_plugins)
            --layouts DIR  Layouts directory (defaults to ./_layouts)
        -h, --help         Show this message
        -v, --version      Print the name and version
        -t, --trace        Show the full backtrace when an error occurs

Subcommands:
  docs                  Launch local server with docs for Jekyll v2.5.3
  doctor, hyde          Search site and print specific deprecation warnings
  build, b              Build your site
  serve, server, s      Serve your site locally
  new                   Creates a new Jekyll site scaffold in PATH
  help                  Show the help message, optionally for a given subcommand.
