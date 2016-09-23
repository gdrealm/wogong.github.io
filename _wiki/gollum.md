---
layout: wiki
title: gollum
date: 2015-06-17
---

# Gollum

## install
1. rvm
   `curl -L https://get.rvm.io | bash -s`
2. `rvm requirements`
3. `gem install gollum`
4. `rvm install 1.9.3`
5. `gem install gollum`

## gollum --help

    %gollum --help
    Gollum is a multi-format Wiki Engine/API/Frontend.
    Basic Command Line Usage:
      gollum [OPTIONS] [PATH]
            PATH                         The path to the Gollum repository (default .).
    Options:
            --port [PORT]                Bind port (default 4567).
            --host [HOST]                Hostname or IP address to listen on (default 0.0.0.0).
            --version                    Display current version.
            --config [CONFIG]            Path to additional configuration file        
            --irb                        Start an irb process with gollum loaded for the current wiki.
            --css                        Inject custom css. Uses custom.css from root repository        
            --js                         Inject custom js. Uses custom.js from root repository
            --page-file-dir [PATH]       Specify the sub directory for all page files (default: repository root).        
            --base-path [PATH]           Specify the base path.
            --gollum-path [PATH]         Specify the gollum path.
            --ref [REF]                  Specify the repository ref to use (default: master).        
            --no-live-preview            Disables livepreview.
            --mathjax                    Enables mathjax.        
            --user-icons [SOURCE]        Set the history user icons. Valid values: gravatar, identicon, none. Default: none.
            --show-all                   Shows all files in file view. By default only valid pages are shown.
            --collapse-tree              Collapse file view tree. By default, expanded tree is shown.
            --h1-title                   Sets page title to value of first h1
