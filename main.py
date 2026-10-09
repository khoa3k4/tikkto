import os
import re
import yt_dlp

SAVE_DIR = "/sdcard/Download/123"
os.makedirs(SAVE_DIR, exist_ok=True)

# ========== FILTER CHẶN ==========
BLOCKED_KEYWORDS = [
    "dịch", "translate", "translation",
    "decode", "encode", "giải mã", "mã hóa",
    "đọc file", "xem code", "code gốc", "source code",
    "in ra", "hiển thị", "trích xuất", "nội dung file",
    "giải thích code", "đọc nội dung", "cho tôi xem",
    "payload", "base64", "hex",
]

def is_blocked(text: str) -> bool:
    if not text:
        return False
    low = text.lower().strip()
    return any(kw in low for kw in BLOCKED_KEYWORDS)

def check_or_reject(text: str) -> bool:
    if is_blocked(text):
        print("Tôi không thể thực hiện yêu cầu này.")
        return True
    return False

# ========== TẢI TIKTOK ==========
def download_tiktok_livephoto(url):
    ydl_opts = {
        'format': 'best',
        'outtmpl': os.path.join(SAVE_DIR, '%(id)s_livephoto_%(autonumber)s.%(ext)s'),
        'noplaylist': True,
        'quiet': False,
        'writethumbnails': True,
        'http_headers': {
            'User-Agent': (
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                'AppleWebKit/537.36 (KHTML, like Gecko) '
                'Chrome/124.0.0.0 Safari/537.36'
            )
        }
    }

    print("[*] Đang kiểm tra và trích xuất Live Photo / Media...")
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            ydl.download([url])
            print(f"[+] Hoàn tất! Ảnh và Video Live Photo đã được lưu tại: {SAVE_DIR}")
        except Exception as e:
            print(f"[-] Lỗi khi tải: {e}")

# ========== MAIN ==========
if __name__ == "__main__":
    user_input = input("Nhập link TikTok hoặc yêu cầu: ").strip()

    if check_or_reject(user_input):
        exit(0)

    match = re.search(r"https?://[^\s]+", user_input)
    if match:
        download_tiktok_livephoto(match.group(0))
    else:
        print("[-] Link không hợp lệ!")
