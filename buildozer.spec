[app]
title = TikTok Downloader
package.name = tikdownloader
package.domain = com.example
source.dir = .
source.include_exts = py,kv,txt
version = 1.0.0
requirements = python3,kivy,yt-dlp,certifi,requests,urllib3,mutagen,pycryptodomex,websockets
orientation = portrait
fullscreen = 0

# Android build settings
android.permissions = INTERNET
android.api = 33
android.minapi = 23
android.archs = arm64-v8a
android.accept_sdk_license = True
android.allow_backup = False

# Avoid bundling development files
source.exclude_dirs = .git,.github,__pycache__,bin,.buildozer

[buildozer]
log_level = 2
warn_on_root = 1
