# 1. I/O:
#    - I: Menu (str), Mã sổ/Tên KH (str), Tiền gốc/Kỳ hạn/Tháng thực gửi (int), Lãi suất (float).
#    - O: Danh sách sổ, tiền lãi/tổng tiền (làm tròn 2 số), báo lỗi Edge Cases.

# 2. giải pháp:
#    - Menu: Dùng 'match-case' điều hướng.
#    - Bắt lỗi: Dùng 'try-except' ép kiểu số để chống sập app khi nhập chữ.
#    - Check rỗng: Dùng 'if not' kiểm tra chuỗi và danh sách rỗng.
#    - Chuẩn hóa: Dùng .strip() xóa dấu cách, .upper() viết hoa mã sổ.

# 3. luồng:
#    - 1 (Xem): List rỗng -> báo trống. Có sổ -> vòng lặp in ra.
#    - 2 (Mở): Nhập ID, Tên (check rỗng/trùng). Nhập số (try-except check > 0) -> Thêm vào list.
#    - 3 (Sửa): Nhập ID (check tồn tại/chặn sổ đã đóng) -> Nhập data mới (try-except check) -> Ghi đè.
#    - 4 (Tất toán): Nhập ID -> Đổi status thành 'closed' để lưu lịch sử.
#    - 5 (Tính lãi): Nhập ID (active) -> Áp công thức tính lãi đúng hạn -> In kết quả.
#    - 6 (Rút trước hạn): Nhập ID, Số tháng gửi (check > 0). Tháng gửi < Kỳ hạn -> Lãi 0.5%, ngược lại -> Lãi gốc. Tính tiền -> In kết quả.
#    - 7 (Thoát): Break dừng vòng lặp. Sai menu -> Vào 'case _' báo nhập lại.
# ================================================================================

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

while True:
    print('''\n===== HỆ THỐNG QUẢN LÝ TÀI KHOẢN TIẾT KIỆM TECHBANK =====
1. Xem danh sách sổ tiết kiệm
2. Mở sổ tiết kiệm mới
3. Cập nhật thông tin sổ tiết kiệm
4. Tất toán hoặc xóa sổ tiết kiệm
5. Tính lãi dự kiến khi đến hạn
6. Kiểm tra điều kiện rút trước hạn
7. Thoát chương trình
========================================================''')
    
    choice = input("Nhập lựa chọn của bạn (1-7): ").strip()
    
    match choice:
        case "1":
            if not saving_accounts:
                print("Danh sách sổ tiết kiệm hiện đang trống")
            else:
                print("\nDanh sách sổ tiết kiệm:")
                for i, account in enumerate(saving_accounts, 1):
                    print(f"{i}. Mã sổ: {account['account_id']} | Khách hàng: {account['customer_name']} | Số tiền gửi: {account['balance']} | Kỳ hạn: {account['term_months']} tháng | Lãi suất: {account['interest_rate']}%/năm | Trạng thái: {account['status']}")

        case "2":
            print("\n--- MỞ SỔ TIẾT KIỆM MỚI ---")
            new_id = input("Nhập mã sổ tiết kiệm: ").strip().upper()
            if not new_id:
                print("Mã sổ tiết kiệm không được để trống!")
                continue
                
            is_duplicate = False
            for account in saving_accounts:
                if account["account_id"] == new_id:
                    is_duplicate = True
                    break
            if is_duplicate:
                print("Mã sổ tiết kiệm đã tồn tại!")
                continue 
            new_name = input("Nhập tên khách hàng: ").strip()
            if not new_name:
                print("Tên khách hàng không được để trống")
                continue
                
            try:
                new_balance = int(input("Nhập số tiền gửi: "))
                new_term = int(input("Nhập kỳ hạn gửi theo tháng: "))
                if new_balance <= 0 or new_term <= 0:
                    print("Số tiền gửi hoặc kỳ hạn không hợp lệ")
                    continue
            except ValueError:
                print("Số tiền gửi hoặc kỳ hạn không hợp lệ")
                continue
            try:
                new_rate = float(input("Nhập lãi suất năm: "))
                if new_rate <= 0:
                    print("Lãi suất không hợp lệ!")
                    continue
            except ValueError:
                print("Lãi suất không hợp lệ!")
                continue
                
            saving_accounts.append({
                "account_id": new_id,
                "customer_name": new_name,
                "balance": new_balance,
                "term_months": new_term,
                "interest_rate": new_rate,
                "status": "active"
            })
            print("Mở sổ tiết kiệm mới thành công!")

        case "3":
            print("\n--- CẬP NHẬT THÔNG TIN SỔ TIẾT KIỆM ---")
            search_id = input("Nhập mã sổ tiết kiệm cần cập nhật: ").strip().upper()
            
            is_exist = False
            for account in saving_accounts:
                if account["account_id"] == search_id:
                    is_exist = True
                    
                    if account["status"] == "closed":
                        print("Không thể cập nhật sổ tiết kiệm đã tất toán!")
                        break
                        
                    print(f"-> Đang sửa thông tin cho sổ của KH: {account['customer_name']}")
                    update_name = input("Nhập tên khách hàng mới: ").strip()
                    if update_name == "":
                        print("Tên khách hàng không được để trống")
                        break
                    
                    try:
                        up_balance = int(input("Nhập số tiền gửi mới: "))
                        up_term = int(input("Nhập kỳ hạn mới theo tháng: "))
                        up_rate = float(input("Nhập lãi suất năm mới: "))
                        
                        if up_balance <= 0 or up_term <= 0 or up_rate <= 0:
                            print("Dữ liệu nhập vào phải lớn hơn 0!")
                            break
                    except ValueError:
                        print("Dữ liệu nhập vào không hợp lệ (phải là số)!")
                        break
                        
                    account["customer_name"] = update_name
                    account["balance"] = up_balance
                    account["term_months"] = up_term
                    account["interest_rate"] = up_rate
                    print("Cập nhật thông tin sổ tiết kiệm thành công!")
                    break
                    
            if not is_exist:
                print("Không tìm thấy mã sổ tiết kiệm")

        case "4":
            print("\n--- TẤT TOÁN SỔ TIẾT KIỆM ---")
            search_id = input("Nhập mã sổ tiết kiệm cần tất toán/xóa: ").strip().upper()
            
            is_exist = False
            for account in saving_accounts:
                if account["account_id"] == search_id:
                    is_exist = True
                    account["status"] = "closed"
                    print(f"Đã tất toán thành công sổ {search_id}. Trạng thái chuyển thành 'closed'.")
                    break
                    
            if not is_exist:
                print("Không tìm thấy mã sổ tiết kiệm")

        case "5":
            print("\n--- TÌM LÃI DỰ KIẾN KHI ĐẾN HẠN ---")
            search_id = input("Nhập mã sổ tiết kiệm cần tính lãi: ").strip().upper()
            
            is_exist = False
            for account in saving_accounts:
                if account["account_id"] == search_id:
                    is_exist = True
                    
                    if account["status"] == "closed":
                        print("Không thể thao tác với sổ tiết kiệm đã tất toán")
                        break
                        
                    interest = account["balance"] * account["interest_rate"] / 100 * account["term_months"] / 12
                    total_receive = account["balance"] + interest
                    
                    print(f"Khách hàng: {account['customer_name']}")
                    print(f"- Tiền gốc: {account['balance']} VND")
                    print(f"- Tiền lãi dự kiến: {round(interest, 2)} VND")
                    print(f"- Tổng tiền nhận khi đến hạn: {round(total_receive, 2)} VND")
                    break
                    
            if not is_exist:
                print("Không tìm thấy mã sổ tiết kiệm")

        case "6":
            print("\n--- KIỂM TRA ĐIỀU KIỆN RÚT TRƯỚC HẠN ---")
            search_id = input("Nhập mã sổ tiết kiệm cần kiểm tra: ").strip().upper()
            
            is_exist = False
            for account in saving_accounts:
                if account["account_id"] == search_id:
                    is_exist = True
                    
                    if account["status"] == "closed":
                        print("Không thể thao tác với sổ tiết kiệm đã tất toán")
                        break
                    
                    try:
                        actual_months = int(input("Nhập số tháng thực gửi: "))
                        if actual_months <= 0:
                            print("Số tháng thực gửi không hợp lệ!")
                            break
                    except ValueError:
                        print("Số tháng thực gửi không hợp lệ!")
                        break
                        
                    if actual_months < account["term_months"]:
                        print("Rút trước hạn! Lãi suất áp dụng: 0.5%/năm")
                        applied_rate = 0.5
                    else:
                        print("Đúng hoặc quá hạn! Áp dụng lãi suất gốc.")
                        applied_rate = account["interest_rate"]
                        
                    actual_interest = account["balance"] * applied_rate / 100 * actual_months / 12
                    actual_total = account["balance"] + actual_interest
                    
                    print(f"--- KẾT QUẢ THỰC NHẬN ---")
                    print(f"- Tiền lãi thực nhận: {round(actual_interest, 2)} VND")
                    print(f"- Tổng số tiền thực nhận về: {round(actual_total, 2)} VND")
                    break
                    
            if not is_exist:
                print("Không tìm thấy mã sổ tiết kiệm")
        
        case "7":
            print("\nThoát chương trình.")
            break
            
        case _:
            print("Lựa chọn không hợp lệ, vui lòng nhập lại")