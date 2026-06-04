# Phân tích Input / Output
## Input
# * Danh sách giỏ hàng (`list`) chứa nhiều sản phẩm (`dict`)
# * Dữ liệu người dùng nhập:

#   * Mã sản phẩm (`string`)
#   * Tên sản phẩm (`string`)
#   * Số lượng (`int`)
#   * Đơn giá (`int`)
#   * Lựa chọn menu (`int`)

# ## Output

# * Hiển thị danh sách sản phẩm dạng bảng
# * Tổng số lượng và tổng tiền
# * Thông báo thêm / sửa / xóa thành công hoặc lỗi dữ liệu

# # Đề xuất giải pháp

# * Dùng `list` để lưu nhiều sản phẩm
# * Mỗi sản phẩm dùng `dictionary`
# * Dùng vòng lặp `while True` để chạy menu
# * Dùng `for` để tìm sản phẩm theo ID
# * Kiểm tra:

#   * `number > 0`
#   * `price >= 0`
#   * menu từ `1-5`
# * Sử dụng:

#   * `append()` để thêm sản phẩm
#   * `remove()` để xóa
#   * cập nhật trực tiếp dictionary để sửa số lượng

# # Thuật toán (Pseudocode)

# 1. Hiển thị menu
# 2. Người dùng nhập lựa chọn
# 3. Nếu:

#    * `1` → In giỏ hàng + tổng tiền
#    * `2` → Thêm sản phẩm / cộng dồn số lượng
#    * `3` → Cập nhật số lượng
#    * `4` → Xóa sản phẩm
#    * `5` → Thoát chương trình
# 4. Kiểm tra dữ liệu hợp lệ
# 5. Nếu sai → báo lỗi
# 6. Lặp lại menu

cart_items = [
         {
         	"id": "P001", 
         	"name": "Dien thoai iPhone 15",
         	"number": 1,
         	"price": 25000000
         },
         {
         	"id": "P002",
         	"name": "Op lung Silicon", 
         	"number": 2, 
         	"price": 150000
         }
]

while True:
    print("=" * 55)
    print(f"{'SHOPEE CART MANAGEMENT SYSTEM':^55}")
    print("=" * 55)

    print("1. Xem chi tiết giỏ hàng & Tính tổng tiền")
    print("2. Thêm sản phẩm mới / Cộng dồn số lượng")
    print("3. Cập nhật số lượng của một sản phẩm")
    print("4. Xóa sản phẩm khỏi giỏ hàng")
    print("5. Thoát chương trình")

    print("=" * 55)
    choice = int(input("Mời bạn chọn chức năng (1-5): "))
    match choice:
        case 1:
            count = 1
            total_prds = 0
            total_bills = 0
            print("--- CHI TIẾT GIỎ HÀNG ---")
            print(f"{'STT':<4} | {'Mã SP':<6} | {'Tên sản phẩm':<24} | {'SL':<3} | {'Đơn giá':<12} | {'Thành tiền':<12}")
            print("-" * 85)
            for cart in cart_items:
                price_format = f'{cart["price"]:,}đ'
                price_total_format = f'{cart["price"] * cart["number"]:,}đ'
                print(f"{count:<4} | {cart['id']:<6} | {cart['name']:<24} | {cart['number']:<3} | {price_format:<12} | {price_total_format:<12}")                
                count += 1
                total_prds += cart['number']
                total_bills += cart['price'] * cart['number']
            print("-" * 85)
            print(f"=> Tổng số lượng sản phẩm trong giỏ: {total_prds}")
            print(f"=> Tổng tiền thanh toán: {f'{total_bills:,}'}đ")

        case 2:
            addPrd_Id = input("Mã sản phẩm: ")
            addPrd_Name = input("Tên sản phẩm: ")
            addPrd_Number = int(input("Nhập số lượng: "))
            addPrd_Price = input("Đơn giá: ")

            if addPrd_Price.isdigit():
                addPrd_Price = int(addPrd_Price)
                for cart in cart_items:
                    if addPrd_Id == cart["id"]:
                        print("Sản phẩm này đã bị trùng không thể thêm!!")
                        break
                else:
                    new_prd = {
                        "id": addPrd_Id,
                        "name": addPrd_Name,
                        "number": addPrd_Number,
                        "price": addPrd_Price
                    }
                    cart_items.append(new_prd)
                    print("Đã thêm thành công!!!")
            else:
                print("Vui lòng hãy nhập số!!!")
        case 3:
            addPrd_Id = input("Mã sản phẩm: ")
            addPrd_Number = input("Nhập số lượng mới cần thay đổi: ")

            if addPrd_Number.isdigit():
                addPrd_Number = int(addPrd_Number)
                for index, cart in enumerate(cart_items):
                    if addPrd_Id == cart["id"]:
                        cart_items[index]["number"] = addPrd_Number
                        print("Đã cập nhật số lượng thành công!!!")
                        break
                else:
                    print("Sản phẩm này không tồn tại trong danh sách!!!")
            else:
                price_format("Vui lòng hãy nhập số!!!")
        case 4:
            addPrd_Id = input("Mã sản phẩm: ")

            for index, cart in enumerate(cart_items):
                if addPrd_Id == cart["id"]:
                    cart_items.pop(index)
                    print("Đã xóa sản phẩm thành công!!!")
                    break
            else:
                print("Sản phẩm này không tồn tại trong danh sách!!!")
        case 5:
            print("Đã thoát chương trình!!!")
            break
        case _:
            print("Vui lòng nhập từ 1-5 !!!")