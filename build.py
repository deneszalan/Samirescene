#!/usr/bin/env python3
"""Builds index.html (the GitHub Pages page) from ludd-in-der-fabrik.html (the page source)."""
src = open('ludd-in-der-fabrik.html', encoding='utf-8').read()
head, body = src.split('</style>', 1)
open('index.html', 'w', encoding='utf-8').write(
    '<!doctype html>\n<html lang="de">\n<head>\n<meta charset="utf-8">\n'
    '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
    '<style>body{margin:0}img{max-width:100%}[hidden]{display:none!important}</style>\n'
    + head + '</style>\n</head>\n<body>' + body.rstrip() + '\n</body>\n</html>\n')
