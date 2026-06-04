# # PHẦN 1 — PHÂN TÍCH VÀ THIẾT KẾ GIẢI PHÁP

# ## 1. Phân tích Input/Output

# ### Input

# Người dùng nhập dữ liệu từ bàn phím:

# * Lựa chọn menu: int (1-7)
# * account_id: string
# * customer_name: string
# * balance: int
# * term_months: int
# * interest_rate: float
# * actual_months: int

# ### Output

# * Hiển thị menu CLI
# * Danh sách sổ tiết kiệm
# * Thông báo lỗi hợp lệ/không hợp lệ
# * Kết quả tính lãi
# * Kết quả kiểm tra rút trước hạn
# * Thông báo cập nhật/tất toán thành công

# ---

# ## 2. Đề xuất giải pháp

# * Dùng list chứa các dictionary để lưu danh sách sổ tiết kiệm.
# * Dùng vòng lặp while True để chạy menu.
# * Dùng:

#   * strip() để xoá khoảng trắng
#   * upper() để chuẩn hoá mã sổ
#   * try-except để kiểm tra nhập số
# * Tạo hàm tìm sổ tiết kiệm theo mã để tái sử dụng.
# * Kiểm tra:

#   * Mã không trùng
#   * Không bỏ trống tên
#   * Số tiền, kỳ hạn > 0
#   * Lãi suất > 0
#   * Chỉ thao tác với sổ active

# ---

# ## 3. Thiết kế thuật toán

# ### Luồng chương trình

# B1. Khởi tạo danh sách saving_accounts
# B2. Hiển thị menu
# B3. Người dùng chọn chức năng
# B4. Kiểm tra lựa chọn hợp lệ
# B5. Thực hiện chức năng tương ứng:

# * Xem danh sách
# * Thêm sổ
# * Cập nhật
# * Tất toán
# * Tính lãi
# * Kiểm tra rút trước hạn
#   B6. Quay lại menu
#   B7. Nếu chọn 7 → kết thúc chương trình


saving_accounts = [
    {
        "account_id": "STK001",
        "customer_name": "Nguyễn Văn An",
        "balance": 50000000,
        "term_months": 6,
        "interest_rate": 6.5,
        "status": "active"
    },
    {
        "account_id": "STK002",
        "customer_name": "Trần Thị Bình",
        "balance": 120000000,
        "term_months": 12,
        "interest_rate": 7.2,
        "status": "active"
    }
]


def find_account(account_id):
    for account in saving_accounts:
        if account["account_id"] == account_id:
            return account
    return None


while True:
    print("\n===== HỆ THỐNG QUẢN LÝ TÀI KHOẢN TIẾT KIỆM TECHBANK =====")
    print("1. Xem danh sách sổ tiết kiệm")
    print("2. Mở sổ tiết kiệm mới")
    print("3. Cập nhật thông tin sổ tiết kiệm")
    print("4. Tất toán hoặc xóa sổ tiết kiệm")
    print("5. Tính lãi dự kiến khi đến hạn")
    print("6. Kiểm tra điều kiện rút trước hạn")
    print("7. Thoát chương trình")

    choice = input("Nhập lựa chọn của bạn: ").strip()

    if not choice.isdigit():
        print("Lựa chọn không hợp lệ, vui lòng nhập lại")
        continue

    choice = int(choice)

    if choice < 1 or choice > 7:
        print("Lựa chọn không hợp lệ, vui lòng nhập lại")
        continue

    match choice:

        case 1:
            if len(saving_accounts) == 0:
                print("Danh sách sổ tiết kiệm hiện đang trống")

            else:
                print("\nDanh sách sổ tiết kiệm:")

                for index in range(len(saving_accounts)):
                    account = saving_accounts[index]

                    print(
                        f"{index + 1}. "
                        f"Mã sổ: {account['account_id']} | "
                        f"Khách hàng: {account['customer_name']} | "
                        f"Số tiền gửi: {account['balance']} | "
                        f"Kỳ hạn: {account['term_months']} tháng | "
                        f"Lãi suất: {account['interest_rate']}%/năm | "
                        f"Trạng thái: {account['status']}"
                    )

        case 2:
            account_id = input(
                "Nhập mã sổ tiết kiệm: "
            ).strip().upper()

            customer_name = input(
                "Nhập tên khách hàng: "
            ).strip()

            try:
                balance = int(
                    input("Nhập số tiền gửi: ").strip()
                )

                term_months = int(
                    input("Nhập kỳ hạn gửi theo tháng: ").strip()
                )

            except:
                print("Số tiền gửi hoặc kỳ hạn không hợp lệ")
                continue

            try:
                interest_rate = float(
                    input("Nhập lãi suất năm: ").strip()
                )

            except:
                print("Lãi suất không hợp lệ!")
                continue

            if find_account(account_id):
                print("Mã sổ tiết kiệm đã tồn tại!")
                continue

            if customer_name == "":
                print("Tên khách hàng không được để trống")
                continue

            if balance <= 0 or term_months <= 0:
                print("Số tiền gửi hoặc kỳ hạn không hợp lệ")
                continue

            if interest_rate <= 0:
                print("Lãi suất không hợp lệ!")
                continue

            saving_accounts.append({
                "account_id": account_id,
                "customer_name": customer_name,
                "balance": balance,
                "term_months": term_months,
                "interest_rate": interest_rate,
                "status": "active"
            })

            print("Mở sổ tiết kiệm thành công!")

        case 3:
            account_id = input(
                "Nhập mã sổ tiết kiệm cần cập nhật: "
            ).strip().upper()

            account = find_account(account_id)

            if not account:
                print("Không tìm thấy mã sổ tiết kiệm")
                continue

            if account["status"] == "closed":
                print("Không thể cập nhật sổ tiết kiệm đã tất toán!")
                continue

            customer_name = input(
                "Nhập tên khách hàng mới: "
            ).strip()

            try:
                balance = int(
                    input("Nhập số tiền gửi mới: ").strip()
                )

                term_months = int(
                    input("Nhập kỳ hạn mới theo tháng: ").strip()
                )

            except:
                print("Số tiền gửi hoặc kỳ hạn không hợp lệ")
                continue

            try:
                interest_rate = float(
                    input("Nhập lãi suất năm mới: ").strip()
                )

            except:
                print("Lãi suất không hợp lệ!")
                continue

            if customer_name == "":
                print("Tên khách hàng không được để trống")
                continue

            if balance <= 0 or term_months <= 0:
                print("Số tiền gửi hoặc kỳ hạn không hợp lệ")
                continue

            if interest_rate <= 0:
                print("Lãi suất không hợp lệ!")
                continue

            account["customer_name"] = customer_name
            account["balance"] = balance
            account["term_months"] = term_months
            account["interest_rate"] = interest_rate

            print("Cập nhật sổ tiết kiệm thành công!")

        case 4:
            account_id = input(
                "Nhập mã sổ tiết kiệm cần tất toán/xóa: "
            ).strip().upper()

            account = find_account(account_id)

            if not account:
                print("Không tìm thấy mã sổ tiết kiệm")
                continue

            account["status"] = "closed"

            print("Tất toán sổ tiết kiệm thành công!")

        case 5:
            account_id = input(
                "Nhập mã sổ tiết kiệm cần tính lãi: "
            ).strip().upper()

            account = find_account(account_id)

            if not account:
                print("Không tìm thấy mã sổ tiết kiệm")
                continue

            if account["status"] == "closed":
                print("Không thể thao tác với sổ tiết kiệm đã tất toán")
                continue

            interest = (
                account["balance"]
                * account["interest_rate"]
                / 100
                * account["term_months"]
                / 12
            )

            total = account["balance"] + interest

            print(f"Tiền lãi dự kiến: {interest}")
            print(f"Tổng tiền nhận khi đến hạn: {total}")

        case 6:
            account_id = input(
                "Nhập mã sổ tiết kiệm cần kiểm tra: "
            ).strip().upper()

            account = find_account(account_id)

            if not account:
                print("Không tìm thấy mã sổ tiết kiệm")
                continue

            if account["status"] == "closed":
                print("Không thể thao tác với sổ tiết kiệm đã tất toán")
                continue

            try:
                actual_months = int(
                    input("Nhập số tháng thực gửi: ").strip()
                )

            except:
                print("Số tháng thực gửi không hợp lệ!")
                continue

            if actual_months <= 0:
                print("Số tháng thực gửi không hợp lệ!")
                continue

            if actual_months < account["term_months"]:
                applied_rate = 0.5
                print("Khách hàng rút trước hạn")

            else:
                applied_rate = account["interest_rate"]
                print("Khách hàng đủ điều kiện hưởng lãi đúng hạn")

            interest = (
                account["balance"]
                * applied_rate
                / 100
                * actual_months
                / 12
            )

            total = account["balance"] + interest

            print(f"Lãi suất áp dụng: {applied_rate}%/năm")
            print(f"Tiền lãi thực nhận: {interest}")
            print(f"Tổng tiền thực nhận: {total}")

        case 7:
            print("Thoát chương trình!")
            break


