[app]

title = TikTok Downloader
package.name = tiktokdownloader
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy,yt-dlp,certifi,urllib3
android.permissions = INTERNET, READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE
android.archs = arm64-v8a, armeabi-v7a
android.minapi = 21
android.api = 33
orientation = portrait
fullscreen = 0

[buildozer]

log_level = 2
warn_on_root = 1
