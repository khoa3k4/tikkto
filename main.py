import os
import re
import threading
from urllib.parse import urlparse

import yt_dlp
from kivy.app import App
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.properties import StringProperty, NumericProperty, BooleanProperty
from kivy.uix.boxlayout import BoxLayout

KV = """
<RootUI>:
    orientation: "vertical"
    padding: "20dp"
    spacing: "14dp"

    Label:
        text: "TikTok Downloader"
        font_size: "24sp"
        bold: True
        size_hint_y: None
        height: "48dp"

    Label:
        text: "Dán liên kết TikTok vào ô bên dưới"
        size_hint_y: None
        height: "28dp"
        color: 0.75, 0.78, 0.82, 1

    TextInput:
        id: url_input
        hint_text: "https://www.tiktok.com/..."
        multiline: False
        size_hint_y: None
        height: "48dp"
        write_tab: False

    Button:
        text: "Đang tải..." if root.busy else "Tải xuống"
        disabled: root.busy
        size_hint_y: None
        height: "50dp"
        on_release: root.start_download(url_input.text)

    ProgressBar:
        max: 100
        value: root.progress
        size_hint_y: None
        height: "8dp"

    Label:
        text: root.status
        text_size: self.width, None
        halign: "left"
        valign: "top"
        size_hint_y: None
        height: self.texture_size[1] + dp(12)

    Label:
        text: "Tệp được lưu trong thư mục riêng của ứng dụng. Bạn có thể xem đường dẫn bên dưới."
        text_size: self.width, None
        halign: "left"
        valign: "top"
        size_hint_y: None
        height: self.texture_size[1] + dp(12)
        color: 0.75, 0.78, 0.82, 1

    Label:
        text: root.save_dir
        text_size: self.width, None
        halign: "left"
        valign: "top"
        size_hint_y: None
        height: self.texture_size[1] + dp(12)
        font_size: "12sp"
"""

class RootUI(BoxLayout):
    status = StringProperty("Sẵn sàng.")
    progress = NumericProperty(0)
    busy = BooleanProperty(False)
    save_dir = StringProperty("")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.save_dir = os.path.join(App.get_running_app().user_data_dir, "Download", "123")
        os.makedirs(self.save_dir, exist_ok=True)

    def set_ui(self, **kwargs):
        def update(_dt):
            for key, value in kwargs.items():
                setattr(self, key, value)
        Clock.schedule_once(update, 0)

    def start_download(self, raw_url):
        url = (raw_url or "").strip()
        parsed = urlparse(url)
        if parsed.scheme not in ("http", "https") or not parsed.netloc:
            self.status = "Vui lòng nhập một liên kết URL hợp lệ."
            return
        if "tiktok.com" not in parsed.netloc.lower():
            self.status = "Vui lòng nhập liên kết thuộc TikTok."
            return

        self.busy = True
        self.progress = 0
        self.status = "Đang kết nối TikTok..."
        threading.Thread(target=self._download, args=(url,), daemon=True).start()

    def _download(self, url):
        def progress_hook(data):
            state = data.get("status")
            if state == "downloading":
                total = data.get("total_bytes") or data.get("total_bytes_estimate")
                downloaded = data.get("downloaded_bytes", 0)
                if total:
                    pct = max(0, min(100, downloaded * 100 / total))
                    self.set_ui(progress=pct, status=f"Đang tải... {pct:.0f}%")
                else:
                    self.set_ui(status="Đang tải video...")
            elif state == "finished":
                self.set_ui(progress=100, status="Đã tải xong dữ liệu, đang hoàn tất...")

        opts = {
            "format": "best",
            "outtmpl": os.path.join(self.save_dir, "%(id)s.%(ext)s"),
            "noplaylist": True,
            "quiet": True,
            "no_warnings": True,
            "writethumbnail": False,
            "progress_hooks": [progress_hook],
            "http_headers": {
                "User-Agent": (
                    "Mozilla/5.0 (Linux; Android 14) AppleWebKit/537.36 "
                    "(KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36"
                )
            },
        }
        try:
            with yt_dlp.YoutubeDL(opts) as ydl:
                ydl.download([url])
            self.set_ui(busy=False, progress=100, status=f"Tải hoàn tất!\nĐã lưu tại: {self.save_dir}")
        except Exception as exc:
            message = str(exc).strip().replace("\n", " ")
            if len(message) > 220:
                message = message[:220] + "…"
            self.set_ui(busy=False, status=f"Không tải được: {message or 'Lỗi không xác định.'}")

class TikDownloaderApp(App):
    title = "TikTok Downloader"

    def build(self):
        Builder.load_string(KV)
        return RootUI()

if __name__ == "__main__":
    TikDownloaderApp().run()
