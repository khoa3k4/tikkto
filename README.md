# TikTok Downloader Android APK

Dự án Kivy chuyển chức năng tải TikTok trong `tik.py` thành ứng dụng Android có ô nhập link, nút tải và thanh tiến trình.

## Cách build chỉ bằng điện thoại Android

Cách dễ nhất là dùng GitHub Actions trên trình duyệt điện thoại. Bạn cần tài khoản GitHub.

1. Tải và giải nén `tik_apk_project.zip`.
2. Trên trình duyệt, vào https://github.com/new để tạo repository mới, ví dụ `tikdownloader`. Đặt repository là **Public** nếu muốn dùng GitHub Actions miễn phí và dễ thao tác; không tải lên thông tin bí mật.
3. Trong repository, chọn **Add file → Upload files**. Tải lên các file/thư mục trong dự án đã giải nén, bao gồm `main.py`, `buildozer.spec`, `README.md` và thư mục `.github/workflows/build-apk.yml`. Nếu giao diện điện thoại không cho tải thư mục `.github`, tạo các thư mục đó trong giao diện GitHub hoặc dùng GitHub web editor.
4. Commit các file lên nhánh `main`.
5. Mở tab **Actions** của repository. Nếu GitHub hỏi, chọn **I understand my workflows, go ahead and enable them**.
6. Chọn workflow **Build Android APK**, nhấn **Run workflow → Run workflow**. Nếu workflow tự chạy khi push thì chờ lần đó hoàn tất.
7. Mở lần chạy mới nhất. Khi trạng thái có dấu tick xanh, kéo xuống **Artifacts** và tải `tikdownloader-debug-apk`.
8. Giải nén artifact ZIP để lấy file `.apk`. Mở APK trên điện thoại và cho phép trình duyệt/công cụ quản lý tệp cài ứng dụng không rõ nguồn gốc nếu Android hỏi.

## Lưu ý

- Build lần đầu có thể mất 10–30 phút hoặc lâu hơn. Nếu build lỗi, mở log của bước bị lỗi và gửi ảnh/log để sửa cấu hình.
- Đây là **debug APK**, phù hợp cài thử trực tiếp, chưa phải bản phát hành ký số để đưa lên cửa hàng.
- Vì Android hạn chế quyền ghi vào thư mục Download công khai, bản này lưu trong thư mục dữ liệu riêng của ứng dụng (`user_data_dir/Download/123`). Gỡ ứng dụng có thể xóa các tệp trong thư mục riêng đó; hãy sao chép tệp ra nơi khác nếu cần giữ lại.
- `yt-dlp` không bảo đảm mọi link TikTok đều tải được; nền tảng có thể thay đổi hoặc yêu cầu xác thực. Chỉ tải nội dung bạn có quyền lưu và tuân thủ điều khoản dịch vụ.
