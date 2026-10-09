[app]
title = TikTok Downloader
package.name = tiktokdownloader
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1

# Khai báo các thư viện Python ứng dụng yêu cầu
requirements = python3,kivy,yt_dlp

orientation = portrait
osx.kivy_version = 2.3.0
fullscreen = 0
android.permissions = INTERNET

[buildozer]
log_level = 2
warn_on_root = 1
