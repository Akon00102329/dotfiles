config.load_autoconfig(False)
c.hints.mode = "number"

c.url.default_page = "https://devdocs.io"
c.url.start_pages = ["https://devdocs.io"]
c.url.searchengines = {
    "DEFAULT": "https://duckduckgo.com/?q={}",
    "wa": "https://wiki.archlinux.org/?search={}",
    "wv": "https://docs.voidlinux.org/?search{}",
    "ws": "https://es.wikipedia.org/wiki/{}",
    "b": "https://www.bing.com/images/search?q={}",
    }
c.downloads.location.directory = "~/downloads"
c.editor.command = ["alacritty", "-e", "vim", "{file}"]
