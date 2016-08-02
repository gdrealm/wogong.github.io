---
layout: wiki
title: pandoc
date: 2014-05-18
---

* markdown -> html
pandoc markdown 支持很多元素，脚注，数学公式，等等

`pandoc -o ch1.html ch1.md -s --template=default.html`

-s standalone


## default template:
        
    <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
    <html xmlns="http://www.w3.org/1999/xhtml"$if(lang)$ lang="$lang$" xml:lang="$lang$"$endif$>
    <head>
      <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
      <meta http-equiv="Content-Style-Type" content="text/css" />
      <meta name="generator" content="pandoc" />
    $for(author-meta)$
      <meta name="author" content="$author-meta$" />
    $endfor$
    $if(date-meta)$
      <meta name="date" content="$date-meta$" />
    $endif$
      <title>$if(title-prefix)$$title-prefix$ - $endif$$pagetitle$</title>
      <style type="text/css">code{white-space: pre;}</style>
    $if(quotes)$
      <style type="text/css">q { quotes: "“" "”" "‘" "’"; }</style>
    $endif$
    $if(highlighting-css)$
      <style type="text/css">
    $highlighting-css$
      </style>
    $endif$
      <link rel="stylesheet" href="./markdown.css" type="text/css"/>
    $for(css)$
      <link rel="stylesheet" href="$css$" $if(html5)$$else$type="text/css" $endif$/>
    $endfor$
    $if(math)$
      $math$
    $endif$
    $for(header-includes)$
      $header-includes$
    $endfor$
    </head>
    <body>
    $for(include-before)$
    $include-before$
    $endfor$
    $if(title)$
    <div id="$idprefix$header">
    <h1 class="title">$title$</h1>
    $for(author)$
    <h2 class="author">$author$</h2>
    $endfor$
    $if(date)$
    <h3 class="date">$date$</h3>
    $endif$
    </div>
    $endif$
    $if(toc)$
    <div id="$idprefix$TOC">
    $toc$
    </div>
    $endif$
    $body$
    $for(include-after)$
    $include-after$
    $endfor$
    </body>
    </html>
    