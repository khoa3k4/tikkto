[app]
title = TikTok Downloader
package.name = tiktokdownloader
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1

requirements = python3,kivy,yt_dlp

orientation = portrait
fullscreen = 0
android.permissions = INTERNET
android.accept_sdk_license = True

[buildozer]
log_level = 2
warn_on_root = 1
