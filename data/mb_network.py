mb_network_address = """
Cần đưa ra câu trả lời chính xác, không trả lời chung kiểu "rất nhiều", nếu câu trả lời không tồn tại trong tài liệu, trả ra không có
Danh sách chi nhánh và phòng giao dịch của MB trên cả nước
Khu vực Hà Nội,Hà Nội 1,CN. Bà Triệu,Trụ sở,Hà Nội,Quận Hoàn Kiếm,Số 18 Đường Ngô Quyền - Phường Tràng Tiền - Quận Hoàn Kiếm - Hà Nội
Khu vực Hà Nội,Hà Nội 1,CN. Bạch Mai,Trụ sở,Hà Nội,Quận Hai Bà Trưng,"Một phần Tầng 1 Trung tâm thương mại Chợ Mơ, số 459C phố Bạch Mai - Phường Trương Định - Quận Hai Bà Trưng - Hà Nội"
Khu vực Hà Nội,Hà Nội 1,CN. Điện Biên Phủ,Trụ sở,Hà Nội,Quận Ba Đình,Số 28A đường Điện Biên Phủ - Phường Điện Biên - Quận Ba Đình - Hà Nội
Khu vực Hà Nội,Hà Nội 1,CN. Đông Anh,Trụ sở,Hà Nội,Huyện Đông Anh,"Tầng 1,2,3 Tòa nhà Trung tâm Du lịch và Thương mại Tổng hợp Cổ Loa, Tổ 3, Thị trấn Đông Anh, Huyện Đông Anh, Hà Nội"
Khu vực Hà Nội,Hà Nội 1,CN. Đông Anh,Phòng giao dịch Sóc Sơn,Hà Nội,Huyện Sóc Sơn,"Một phần thửa đất Khu 1, Khu 2 - Thị Trấn Sóc Sơn - Huyện Sóc Sơn - Hà Nội"
Khu vực Hà Nội,Hà Nội 1,CN. Đống Đa,Trụ sở,Hà Nội,Quận Đống Đa,"Một phần tầng 1, tầng 2 tòa nhà Trụ sở làm việc Trung tâm Phát thanh truyền hình Quân đội, số 165 Xã Đàn - Phường Nam Đồng - Quận Đống Đa - Hà Nội"
Khu vực Hà Nội,Hà Nội 1,CN. Đống Đa,Phòng giao dịch Thái Thịnh,Hà Nội,Quận Đống Đa,Số 71 - 73 Thái Thịnh - Phường Thịnh Quang - Quận Đống Đa - Hà Nội
Khu vực Hà Nội,Hà Nội 1,CN. Đống Đa,Phòng giao dịch Hoàng Cầu,Hà Nội,Quận Đống Đa,Tầng 2 - Phường Ô Chợ Dừa - Quận Đống Đa - Hà Nội
Khu vực Hà Nội,Hà Nội 1,CN. Đông Hà Nội,Trụ sở,Hà Nội,Quận Long Biên,63 đường Cổ Linh - Phường Thạch Bàn - Quận Long Biên - Hà Nội
Khu vực Hà Nội,Hà Nội 1,CN. Gia Lâm,Trụ sở,Hà Nội,Huyện Gia Lâm,Số 132 - 134 đường Ngô Xuân Quảng - Thị Trấn Trâu Quỳ - Huyện Gia Lâm - Hà Nội
Khu vực Hà Nội,Hà Nội 1,CN. Hà Thành,Trụ sở,Hà Nội,Quận Ba Đình,47 Phan Đình Phùng - Phường Quán Thánh - Quận Ba Đình - Hà Nội
Khu vực Hà Nội,Hà Nội 1,CN. Hai Bà Trưng,Trụ sở,Hà Nội,Quận Hai Bà Trưng,"Tầng 1 tòa Tower 1, Times city, số 458 Minh Khai - Phường Vĩnh Tuy - Quận Hai Bà Trưng - Hà Nội"
Khu vực Hà Nội,Hà Nội 1,CN. Hai Bà Trưng,Phòng giao dịch Vân Hồ,Hà Nội,Quận Hai Bà Trưng,Số 29 Lê Đại Hành - Phường Lê Đại Hành - Quận Hai Bà Trưng - Hà Nội
Khu vực Hà Nội,Hà Nội 1,CN. Hoàn Kiếm,Trụ sở,Hà Nội,Quận Hoàn Kiếm,"Một phần tầng 1, tầng 2 và tầng 3, Tòa nhà thông tấn xã, Số 77 -79 đường Lý Thường Kiệt - Phường Trần Hưng Đạo - Quận Hoàn Kiếm - Hà Nội"
Khu vực Hà Nội,Hà Nội 1,CN. Hồng Hà,Trụ sở,Hà Nội,Quận Hà Đông,Tầng 1 số 160 đường Phùng Hưng - Phường Phúc La - Quận Hà Đông - Hà Nội
Khu vực Hà Nội,Hà Nội 1,CN. Linh Đàm,Trụ sở,Hà Nội,Quận Hoàng Mai,BT1 Ô 4 Bắc Linh Đàm - Phường Đại Kim - Quận Hoàng Mai - Hà Nội
Khu vực Hà Nội,Hà Nội 1,CN. Long Biên,Trụ sở,Hà Nội,Quận Long Biên,"Tầng 1, 3, 4, 5 số 137C đường Nguyễn Văn Cừ - Phường Ngọc Lâm - Quận Long Biên - Hà Nội"
Khu vực Hà Nội,Hà Nội 1,CN. Long Biên,Phòng giao dịch Yên Viên,Hà Nội,Huyện Gia Lâm,"Tầng 1, số 467 đường Hà Huy Tập - Thị Trấn Yên Viên - Huyện Gia Lâm - Hà Nội"
Khu vực Hà Nội,Hà Nội 1,CN. Lý Nam Đế,Trụ sở,Hà Nội,Quận Hoàn Kiếm,Số 14C đường Lý Nam Đế - Phường Hàng Mã - Quận Hoàn Kiếm - Hà Nội
Khu vực Hà Nội,Hà Nội 1,CN. Lý Thái Tổ,Trụ sở,Hà Nội,Quận Hoàn Kiếm,Số 17 Tông Đản - Phường Tràng Tiền - Quận Hoàn Kiếm - Hà Nội
Khu vực Hà Nội,Hà Nội 1,CN. Mê Linh,Trụ sở,Hà Nội,Huyện Mê Linh,"Thửa đất số 715, tờ bản đồ số 46, tổ dân phố số 7 - Thị trấn Quang Minh - Huyện Mê Linh - Hà Nội"
Khu vực Hà Nội,Hà Nội 1,CN. Minh Khai,Trụ sở,Hà Nội,Quận Hai Bà Trưng,"Tầng 1, 2, 3, 4 số 409, tổ 52, phố Kim Ngưu - Phường Vĩnh Tuy - Quận Hai Bà Trưng - Hà Nội"
Khu vực Hà Nội,Hà Nội 1,CN. Nam Hà Nội,Trụ sở,Hà Nội,Quận Đống Đa,"Một phần tầng 1, tầng 2 tòa nhà số 8 Phạm Ngọc Thạch - Phường Kim Liên - Quận Đống Đa - Hà Nội"
Khu vực Hà Nội,Hà Nội 1,CN. Ngô Gia Tự,Trụ sở,Hà Nội,Quận Long Biên,Số 32 đường Ngô Gia Tự - Phường Đức Giang - Quận Long Biên - Hà Nội
Khu vực Hà Nội,Hà Nội 1,CN. Tây Sơn,Trụ sở,Hà Nội,Quận Thanh Xuân,"Tầng 1, 3 tòa nhà số 539 - 539A, phố Vũ Tông Phan - Phường Khương Đình - Quận Thanh Xuân - Hà Nội"
Khu vực Hà Nội,Hà Nội 1,CN. Thanh Trì,Trụ sở,Hà Nội,Huyện Thanh Trì,Tầng 1 tòa nhà An & Huy khu công nghiệp Ngọc Hồi - Xã Ngọc Hồi - Huyện Thanh Trì - Hà Nội
Khu vực Hà Nội,Hà Nội 1,CN. Thanh Xuân,Trụ sở,Hà Nội,Quận Thanh Xuân,"Một phần Tầng 1, tầng 2 tòa nhà Gold Tower, số 275 Nguyễn Trãi - Phường Thanh Xuân Trung - Quận Thanh Xuân - Hà Nội"
Khu vực Hà Nội,Hà Nội 1,CN. Thủ Đô,Trụ sở,Hà Nội,Quận Hai Bà Trưng,Tòa nhà Vinafor số 127 Lò Đúc - Phường Đống Mác - Quận Hai Bà Trưng - Hà Nội
Khu vực Hà Nội,Hà Nội 1,CN. Thường Tín,Trụ sở,Hà Nội,Huyện Thường Tín,"Một phần tầng 1, tầng 2 tòa nhà tại lô số 2, cụm công nghiệp Hà Bình Phương - Xã Hà Hồi - Huyện Thường Tín - Hà Nội"
Khu vực Hà Nội,Hà Nội 1,CN. Thụy Khuê,Trụ sở,Hà Nội,Quận Tây Hồ,Tầng 1 vị trí L1 - A - B tổ hợp dự án số 69B phố Thụy Khuê - Phường Thụy Khuê - Quận Tây Hồ - Hà Nội
Khu vực Hà Nội,Hà Nội 1,CN. Vạn Phúc,Trụ sở,Hà Nội,Quận Hà Đông,"B-TT01-55B-TT01-57, Khu nhà ở Ngân Hà Vạn Phúc - Phường Vạn Phúc - Quận Hà Đông - Hà Nội"
Khu vực Hà Nội,Hà Nội 2,CN. Ba Đình,Trụ sở,Hà Nội,Quận Ba Đình,Số 3 Liễu Giai - Phường Liễu Giai - Quận Ba Đình - Hà Nội
Khu vực Hà Nội,Hà Nội 2,CN. Ba Đình,Phòng giao dịch Vĩnh Phúc 1,Hà Nội,Quận Ba Đình,"Tầng 1 và tầng 2 số 102, 103, 203 nhà K2, khu 7.2 HA Vĩnh Phúc - Phường Vĩnh Phúc - Quận Ba Đình - Hà Nội"
Khu vực Hà Nội,Hà Nội 2,CN. Đan Phượng,Trụ sở,Hà Nội,Huyện Đan Phượng,Km 21 Quốc Lộ 32 - Thị trấn Phùng - Huyện Đan Phượng - Hà Nội
Khu vực Hà Nội,Hà Nội 2,CN. Đông Đô,Trụ sở,Hà Nội,Quận Nam Từ Liêm,109 Phố Nhổn - Phường Phương Canh - Quận Nam Từ Liêm - Hà Nội
Khu vực Hà Nội,Hà Nội 2,CN. Giải Phóng,Trụ sở,Hà Nội,Quận Thanh Xuân,"Một phần tầng 1 và tầng lửng tòa nhà HH2 Dự án Khu hỗn hợp nhà ở, dịch vụ công cộng, văn phòng và trường học (tên thương mại Imperial Plaza) tại địa chỉ số 360 đường Giải Phóng, Phường Phương Liệt, Quận Thanh Xuân, Hà Nội"
Khu vực Hà Nội,Hà Nội 2,CN. Giải Phóng,Phòng giao dịch Tân Mai,Hà Nội,Quận Hoàng Mai,"Số 641, nhà H5, TT Tân Mai, Phường Tân Mai, Quận Hoàng Mai, Hà Nội"
Khu vực Hà Nội,Hà Nội 2,CN. Hà Đông,Trụ sở,Hà Nội,Quận Hà Đông,"Một phần tầng 1, tầng 2 toàn tháp Thiên niên kỷ số 4 đường Quang Trung - Phường Yết Kiêu - Quận Hà Đông - Hà Nội"
Khu vực Hà Nội,Hà Nội 2,CN. Hà Nội,Trụ sở,Hà Nội,Quận Cầu Giấy,Tầng 1 tòa nhà số 17T2 KDT Trung Hòa Nhân Chính - Phường Trung Hòa - Quận Cầu Giấy - Hà Nội
Khu vực Hà Nội,Hà Nội 2,CN. Hà Nội,Phòng giao dịch Trung Văn,Hà Nội,Quận Thanh Xuân,"Tầng 1 tòa nhà HH2 Bắc Hà, số 15 phố Tố Hữu - Phường Nhân Chính - Quận Thanh Xuân - Hà Nội"
Khu vực Hà Nội,Hà Nội 2,CN. Hà Nội,Phòng giao dịch Nam Trung Yên,Hà Nội,Quận Cầu Giấy,"Ô số 10 ( Khu tái định cư Tại chỗ) đường Trung Yên 1, KĐTM Trung Yên - Phường Yên Hòa - Quận Cầu Giấy - Hà Nội"
Khu vực Hà Nội,Hà Nội 2,CN. Hòa Lạc,Trụ sở,Hà Nội,Huyện Thạch Thất,"Tầng  1 Tòa nhà Công ty TNHH MTV Phát triển Khu CNC Hòa Lạc, Khu Công nghệ cao Hòa Lạc, Km29, Đại lộ Thăng Long - Xã Thạch Hòa - Huyện Thạch Thất - Hà Nội"
Khu vực Hà Nội,Hà Nội 2,CN. Hoài Đức,Trụ sở,Hà Nội,Huyện Hoài Đức,"Lô A38 NV 16 ô số 11 và ô số 12, khu đô thị mới hai bên đường Lê Trọng Tấn - Xã An Khánh - Huyện Hoài Đức - Hà Nội"
Khu vực Hà Nội,Hà Nội 2,CN. Hoàng Mai,Trụ sở,Hà Nội,Quận Hoàng Mai,"Tầng 1 2 ô DV-02, DV-04, DV-12, DV-14 khu chung cư @ Home thuộc dự án khu nhà ở xã hội tại ô đất C11-ODK4 - Phường Yên Sở - Quận Hoàng Mai - Hà Nội"
Khu vực Hà Nội,Hà Nội 2,CN. Hoàng Quốc Việt,Trụ sở,Hà Nội,Quận Cầu Giấy,Số 126 đường Hoàng Quốc Việt - Phường Nghĩa Tân - Quận Cầu Giấy - Hà Nội
Khu vực Hà Nội,Hà Nội 2,CN. Hoàng Quốc Việt,Phòng giao dịch Nghĩa Tân,Hà Nội,Quận Cầu Giấy,"A2 Đơn nguyên 2, đường Nguyễn Khánh Toàn - Phường Quan Hoa - Quận Cầu Giấy - Hà Nội"
Khu vực Hà Nội,Hà Nội 2,CN. Hoàng Quốc Việt,Phòng giao dịch Nam Thăng Long,Hà Nội,Quận Bắc Từ Liêm,Một phần tầng 1 tòa nhà A2 Chung cư Green Star - KĐT thành phố Giao lưu - số 232 đường Phạm Văn Đồng - Phường Cổ Nhuế 1 - Quận Bắc Từ Liêm - Hà Nội
Khu vực Hà Nội,Hà Nội 2,CN. Lê Trọng tấn,Trụ sở,Hà Nội,Quận Thanh Xuân,Số 164 Lê Trọng Tấn - Phường Khương Mai - Quận Thanh Xuân - Hà Nội
Khu vực Hà Nội,Hà Nội 2,CN. Mỹ Đình,Trụ sở,Hà Nội,Quận Nam Từ Liêm,"Tầng 1, tầng 2 nhà B, Tòa nhà HH4 SongDa TwinTower, đường Phạm Hùng - Phường Mỹ Đình 1 - Quận Nam Từ Liêm - Hà Nội"
Khu vực Hà Nội,Hà Nội 2,CN. Mỹ Đình,Phòng giao dịch Mỹ Đình I,Hà Nội,Quận Nam Từ Liêm,Kios số 03 – Lô đất 1.A.IV KĐTM Mỹ Đình 1 - Phường Cầu Diễn - Quận Nam Từ Liêm - Hà Nội
Khu vực Hà Nội,Hà Nội 2,CN. Nhân Chính,Trụ sở,Hà Nội,Quận Thanh Xuân,"Tầng 1 tòa nhà Thăng Long, Số 98 Ngụy Như Kon Tum - Phường Nhân Chính - Quận Thanh Xuân - Hà Nội"
Khu vực Hà Nội,Hà Nội 2,CN. Sơn Tây,Trụ sở,Hà Nội,Thị xã Sơn Tây,Số 135 Chùa Thông - Phường Sơn Lộc - Thị Xã Sơn Tây - Hà Nội
Khu vực Hà Nội,Hà Nội 2,CN. Sơn Tây,Phòng giao dịch Lê Lợi,Hà Nội,Thị xã Sơn Tây,Một phần diện tich tầng 1 tòa nhà số 6 Trưng Vương - Phường Lê Lợi - Thị Xã Sơn Tây - Hà Nội
Khu vực Hà Nội,Hà Nội 2,CN. Sơn Tây,Phòng giao dịch Ba Vì,Hà Nội,Huyện Ba Vì,"Thửa đất số 253, tờ bản đồ số 04, thôn Vĩnh Phệ - Xã Chu Minh - Huyện Ba Vì - Hà Nội"
Khu vực Hà Nội,Hà Nội 2,CN. Tây Hà Nội,Trụ sở,Hà Nội,Quận Hà Đông,"Tầng 1 tòa nhà Nam Cường, KM4 đường Lê Văn Lương kéo dài, KĐTM Dương Nội - Phường Dương Nội - Quận Hà Đông - Hà Nội"
Khu vực Hà Nội,Hà Nội 2,CN. Tây Hồ,Trụ sở,Hà Nội,Quận Tây Hồ,"Tầng 1, tầng 2, tầng 3, tầng 4 Số 28 đường Xuân La - Phường Xuân La - Quận Tây Hồ - Hà Nội"
Khu vực Hà Nội,Hà Nội 2,CN. Tây Hồ,Phòng giao dịch Xuân Diệu,Hà Nội,Quận Tây Hồ,Tầng 1 và một phần diện tích tầng 2 tòa nhà số 114 Xuân Diệu - Phường Tứ Liên - Quận Tây Hồ - Hà Nội
Khu vực Hà Nội,Hà Nội 2,CN. Tây Hồ,Phòng giao dịch Lạc Long Quân,Hà Nội,Quận Tây Hồ,"Tầng 1, 2 Lô đất số 06 ô D9B, khu đấu giá quyền sử dụng đất - Phường Xuân La - Quận Tây Hồ - Hà Nội"
Khu vực Hà Nội,Hà Nội 2,CN. Thăng Long,Trụ sở,Hà Nội,Quận Đống Đa,Số 34 Láng Hạ - Phường Láng Hạ - Quận Đống Đa - Hà Nội
Khu vực Hà Nội,Hà Nội 2,CN. Thành Công,Trụ sở,Hà Nội,Quận Đống Đa,"Ô số 8 tầng 1, ô số 3 tầng 8 Tòa nhà Văn phòng Sông Hồng, số 165 đường Thái Hà - Phường Láng Hạ - Quận Đống Đa - Hà Nội"
Khu vực Hà Nội,Hà Nội 2,CN. Tràng An,Trụ sở,Hà Nội,Quận Đống đa,54A đường Nguyễn Chí Thanh - Phường Láng Thượng - Quận Đống đa - Hà Nội
Khu vực Hà Nội,Hà Nội 2,CN. Từ Liêm,Trụ sở,Hà Nội,Quận Nam Từ Liêm,Số 8 Lê Đức Thọ - Phường Mỹ Đình 2 - Quận Nam Từ Liêm - Hà Nội
Khu vực Hà Nội,Hà Nội 2,CN. Văn Phú,Trụ sở,Hà Nội,Quận Hà Đông,"Một phần tầng 1 tòa nhà CT9, khu đô thị mới Văn Phú - Phường Phú La - Quận Hà Đông - Hà Nội"
Khu vực Hà Nội,Hà Nội 2,CN. Võ Chí Công,Trụ sở,Hà Nội,Quận Bắc Từ Liêm,Một phần diện tích tầng 1 tòa nhà N01-T4 Khu Đoàn ngoại giao - Phường Xuân Tảo - Quận Bắc Từ Liêm - Hà Nội
Khu vực Hà Nội,Hà Nội 2,CN. Xuân Mai,Trụ sở,Hà Nội,Huyện Chương Mỹ,"Số 51, tổ 6, khu Xuân Hà - Thị Trấn Xuân Mai - Huyện Chương Mỹ - Hà Nội"
Khu vực Hà Nội,Hà Nội 2,CN. Xuân Thủy,Trụ sở,Hà Nội,Quận Cầu Giấy,"Nhà số 3, Lô A, Khu D6, Đường Nguyễn Phong Sắc kéo dài, Khu đô thị mới Cầu Giấy - Phường Dịch Vọng - Quận Cầu Giấy - Hà Nội"
Khu vực Hà Nội,Hà Nội 2,Sở giao dịch,Trụ sở,Hà Nội,Quận Cầu Giấy,"Một phần tầng 1, tầng 2 tòa nhà số 18 Lê Văn Lương - Phường Trung Hòa - Quận Cầu Giấy - Hà Nội"
Khu vực Hà Nội,Hà Nội 2,Sở giao dịch 3,Trụ sở,Hà Nội,Quận Đống Đa,"Tầng 2, Số 21 Cát Linh - Phường Cát Linh - Quận Đống Đa - Hà Nội"
Khu vực Hà Nội,Hà Nội 2,Sở giao dịch 3,Phòng giao dịch Nguyễn Du,Hà Nội,Quận Hai Bà Trưng,"Một phần tầng 1, tầng 2 tòa nhà số 68 phố Nguyễn Du - Phường Nguyễn Du - Quận Hai Bà Trưng - Hà Nội"
Khu vực Miền Bắc,Đông Bắc Bộ,CN. Bắc Hải Phòng,Trụ sở,Hải Phòng,Quận Hồng Bàng,"Số 5 đường Trần Hưng Đạo, Phường Hoàng Văn Thụ, Hải Phòng"
Khu vực Miền Bắc,Đông Bắc Bộ,CN. Bắc Hải Phòng,Phòng giao dịch Thủy Nguyên,Hải Phòng,Huyện Thủy Nguyên,"TTTM Bắc Mật, Số 9 Bạch Đằng, Thị trấn Núi Đèo, Hải Phòng"
Khu vực Miền Bắc,Đông Bắc Bộ,CN. Bắc Hải Phòng,Phòng giao dịch Thượng Lý,Hải Phòng,Quận Hồng Bàng,"Nhà số BH01-51, Khu đô thị xi măng Hải Phòng (Khu đô thị Vinhome Imperia Hải Phòng), đường Bạch Đằng, Phường Thượng Lý, Hải Phòng"
Khu vực Miền Bắc,Đông Bắc Bộ,CN. Bắc Hải Phòng,Phòng giao dịch Quán Toan,Hải Phòng,Quận Hồng Bàng,"Số 212 đường Hùng Vương, Phường Quán Toan, Hải Phòng"
Khu vực Miền Bắc,Đông Bắc Bộ,CN. Cẩm Phả,Trụ sở,Quảng Ninh,Thành phố Cẩm Phả,"Số 705 (thửa đất số 7, 8, 9 tờ bản đồ số 22), tổ 2, khu Tân Lập 6, Phường Cẩm Thủy, Thành phố Cẩm Phả, Quảng Ninh"
Khu vực Miền Bắc,Đông Bắc Bộ,CN. Điện Biên,Trụ sở,Điện Biên,Thành phố Điện Biên Phủ,"Số nhà 930, đường Võ Nguyên Giáp, Tổ 3 - Phường Mường Thanh - TP Điện Biên Phủ - Điện Biên"
Khu vực Miền Bắc,Đông Bắc Bộ,CN. Hà Nam,Trụ sở,Hà Nam,Thành phố Phủ Lý,"Một phần tầng 1 và 2 trung tâm thương mại, dịch vụ Đại Nam Plaza, đường Lê Hoàn, Phường Hai Bà Trưng, Hà Nam"
Khu vực Miền Bắc,Đông Bắc Bộ,CN. Hà Nam,Phòng giao dịch Duy Tiên,Hà Nam,Thị xã Duy Tiên,"Thửa đất số 02 tờ bản đồ PL số 07, khu tập thể xí nghiệp Giống cây trồng Trung Ương, Phường Đồng Văn, Hà Nam"
Khu vực Miền Bắc,Đông Bắc Bộ,CN. Hà Tĩnh,Trụ sở,Hà Tĩnh,Thành phố Hà Tĩnh,"Số 80, đường Phan Đình Phùng - Phường Nam Hà - Thành phố Hà Tĩnh - Hà Tĩnh"
Khu vực Miền Bắc,Đông Bắc Bộ,CN. Hà Tĩnh,Phòng giao dịch Trần Phú,Hà Tĩnh,Thành phố Hà Tĩnh,Số 207 đường Trần Phú - Phường Trần Phú - Thành phố Hà Tĩnh - Hà Tĩnh
Khu vực Miền Bắc,Đông Bắc Bộ,CN. Hà Tĩnh,Phòng giao dịch Hồng Lĩnh,Hà Tĩnh,Thị xã Hồng Lĩnh,Tổ dân phố 8 đường Trần Phú - Phường Bắc Hồng - Thị Xã Hồng Lĩnh - Hà Tĩnh
Khu vực Miền Bắc,Đông Bắc Bộ,CN. Hải Phòng,Trụ sở,Hải Phòng,Quận Ngô Quyền,"Số 06 Lô 30A Lê Hồng Phong, Phường Lạc Viên, Hải Phòng"
Khu vực Miền Bắc,Đông Bắc Bộ,CN. Hải Phòng,Phòng giao dịch Vạn Mỹ,Hải Phòng,Quận Ngô Quyền,"Số 341 Đà Nẵng, Phường Vạn Mỹ, Hải Phòng"
Khu vực Miền Bắc,Đông Bắc Bộ,CN. Hải Phòng,Phòng giao dịch Lê Hồng Phong,Hải Phòng,Huyện Vĩnh Bảo,"Số 136 Khu phố 3/2, Thị trấn Vĩnh Bảo, Hải Phòng"
Khu vực Miền Bắc,Đông Bắc Bộ,CN. Hải Phòng,Phòng giao dịch Lạch Tray,Hải Phòng,Quận Ngô Quyền,"Số 02B Lạch Tray, Phường Lạch Tray, Hải Phòng"
Khu vực Miền Bắc,Đông Bắc Bộ,CN. Hải Phòng,Phòng giao dịch Hải An,Hải Phòng,Quận Ngô Quyền,"Số 206, 216 Văn Cao, Phường Đằng Giang, Hải Phòng"
Khu vực Miền Bắc,Đông Bắc Bộ,CN. Móng Cái,Trụ sở,Quảng Ninh,Thành phố Móng cái,"Số 02 Đường Hùng Vương, Phường Hòa Lạc, Thành phố Móng cái, Quảng Ninh"
Khu vực Miền Bắc,Đông Bắc Bộ,CN. Nam Định,Trụ sở,Nam Định,Thành phố Nam Định,"Một phần tầng 1, tầng 3 Tòa nhà đa năng, số 625 Trần Hưng Đạo - Phường Lộc Vượng - Thành phố Nam Định - Nam Định"
Khu vực Miền Bắc,Đông Bắc Bộ,CN. Nam Định,Phòng giao dịch Ý Yên,Nam Định,Huyện Ý Yên,"Thửa đất số ô M58, mặt bằng QH chi tiết cụm CN Làng Nghề TMDV Phía nam - Thị Trấn Lâm - Huyện Ý Yên - Nam Định"
Khu vực Miền Bắc,Đông Bắc Bộ,CN. Nam Định,Phòng giao dịch Thành Nam,Nam Định,Thành phố Nam Định,"Số 69, phố Lê Hồng Phong - Phường Nguyễn Du - Thành phố Nam Định - Nam Định"
Khu vực Miền Bắc,Đông Bắc Bộ,CN. Nam Định,Phòng giao dịch Hải Hậu,Nam Định,Huyện Hải Hậu,Tổ dân phố số 1 - Thị Trấn Yên Định - Huyện Hải Hậu - Nam Định
Khu vực Miền Bắc,Đông Bắc Bộ,CN. Nam Hải Phòng,Trụ sở,Hải Phòng,Quận Lê Chân,"Tầng trệt (tầng 1), tầng 3 tòa nhà Tổng công ty xây dựng Bạch Đằng, số 268 đường Trần Nguyên Hãn, Phường Niệm Nghĩa, Hải Phòng"
Khu vực Miền Bắc,Đông Bắc Bộ,CN. Nam Hải Phòng,Phòng giao dịch Võ Nguyên Giáp,Hải Phòng,Quận Lê Chân,"Tầng 1, tầng 2 Tòa nhà tại thửa đất số 512 lô HK17 Khu dự án đô thị Ven sông Lạch Tray, Phường Vĩnh Niệm, Hải Phòng"
Khu vực Miền Bắc,Đông Bắc Bộ,CN. Nam Hải Phòng,Phòng giao dịch Lê Chân,Hải Phòng,Quận Lê Chân,"Số 146 Tôn Đức Thắng, Phường Lam Sơn, Hải Phòng"
Khu vực Miền Bắc,Đông Bắc Bộ,CN. Nam Hải Phòng,Phòng giao dịch Kiến An,Hải Phòng,Quận Kiến An,"Số 01+02/NO 05 Khu đô thị và nhà ở Cựu Viên, Phường Bắc Sơn, Hải Phòng"
Khu vực Miền Bắc,Đông Bắc Bộ,CN. Nghệ An,Trụ sở,Nghệ An,Thành phố Vinh,Số 02 - Đường Nguyễn Thị Minh Khai - Phường Hưng Bình - Thành phố Vinh - Nghệ An
Khu vực Miền Bắc,Đông Bắc Bộ,CN. Nghệ An,Phòng giao dịch Trung Đô,Nghệ An,Thành phố Vinh,Số 191 đường Lê Duẩn - Phường Trung Đô - Thành phố Vinh - Nghệ An
Khu vực Miền Bắc,Đông Bắc Bộ,CN. Nghệ An,Phòng giao dịch Hà Huy Tập,Nghệ An,Thành phố Vinh,Tòa nhà Viettel - Đại lộ Lenin - Phường Hà Huy Tập - Thành phố Vinh - Nghệ An
Khu vực Miền Bắc,Đông Bắc Bộ,CN. Nghệ An,Phòng giao dịch Diễn Châu,Nghệ An,Huyện Diễn Châu,Khối 3 - Thị Trấn Diễn Châu - Huyện Diễn Châu - Nghệ An
Khu vực Miền Bắc,Đông Bắc Bộ,CN. Nghi Sơn,Trụ sở,Thanh Hoá,Thị xã Nghi Sơn,"Số nhà 100, đường Đào Duy Từ, tiểu khu 5, Phường Hải Hòa, Thị xã Nghi Sơn, Thanh Hoá"
Khu vực Miền Bắc,Đông Bắc Bộ,CN. Ninh Bình,Trụ sở,Ninh Bình,Thành phố Ninh Bình,Tầng 1 và tầng 3 tòa nhà số 848 đường Trần Hưng Đạo - Phường Tân Thành - Thành phố Ninh Bình - Ninh Bình
Khu vực Miền Bắc,Đông Bắc Bộ,CN. Ninh Bình,Phòng giao dịch Tam Điệp,Ninh Bình,Thành phố Tam Điệp,Số 146 Đồng Giao - Phường Bắc Sơn - Thành phố Tam Điệp - Ninh Bình
Khu vực Miền Bắc,Đông Bắc Bộ,CN. Ninh Bình,Phòng giao dịch Nguyễn Công Trứ,Ninh Bình,Thành phố Ninh Bình,Số 307 - 309 - 311 đường Nguyễn Công Trứ - Phường Bích Đào - Thành phố Ninh Bình - Ninh Bình
Khu vực Miền Bắc,Đông Bắc Bộ,CN. Ninh Bình,Phòng giao dịch Gia Viễn,Ninh Bình,Huyện Gia Viễn,Đường Quốc lộ 1A - Xã Gia Trấn - Huyện Gia Viễn - Ninh Bình
Khu vực Miền Bắc,Đông Bắc Bộ,CN. Quảng Ninh,Trụ sở,Quảng Ninh,Thành phố Hạ Long,"Số 156, đường Lê Thánh Tông,, Phường Bạch Đằng, Thành phố Hạ Long, Quảng Ninh"
Khu vực Miền Bắc,Đông Bắc Bộ,CN. Quảng Ninh,Phòng giao dịch Vân Đồn,Quảng Ninh,Huyện Vân Đồn,"Số 404-406, Tổ 1, khu 7,, Thị trấn Cái Rồng, Huyện Vân Đồn, Quảng Ninh"
Khu vực Miền Bắc,Đông Bắc Bộ,CN. Quảng Ninh,Phòng giao dịch Hạ Long,Quảng Ninh,Thành phố Hạ Long,"Số 328, tổ 1B, khu 6A,, Phường Hồng Hải, Thành phố Hạ Long, Quảng Ninh"
Khu vực Miền Bắc,Đông Bắc Bộ,CN. Quảng Ninh,Phòng giao dịch Bãi Cháy,Quảng Ninh,Thành phố Hạ Long,"Số nhà 489, đường Hạ Long, tổ 8, khu 9A,, Phường Bãi Cháy, Thành phố Hạ Long, Quảng Ninh"
Khu vực Miền Bắc,Đông Bắc Bộ,CN. Thái Bình,Trụ sở,Thái Bình,Thành phố Thái Bình,"Tầng 1 (tầng trệt) tòa nhà Viettel Thái Bình, Phường Trần Hưng Đạo, Thành phố Thái Bình, Thái Bình"
Khu vực Miền Bắc,Đông Bắc Bộ,CN. Thái Bình,Phòng giao dịch Thái Thụy,Thái Bình,Huyện Thái Thụy,"Tổ dân phố số 6, Thị trấn Diêm Điền, Huyện Thái Thụy, Thái Bình"
Khu vực Miền Bắc,Đông Bắc Bộ,CN. Thái Bình,Phòng giao dịch Hưng Hà,Thái Bình,Huyện Hưng Hà,"Đường 39A, Khu Nhân Cầu 1, Thị trấn Hưng Hà, Huyện Hưng Hà, Thái Bình"
Khu vực Miền Bắc,Đông Bắc Bộ,CN. Thanh Hóa,Trụ sở,Hà Nội,Quận Ba Đình,"Số 54+56+60 đường Trần Phú, Phường Điện Biên, Quận Ba Đình, Hà Nội"
Khu vực Miền Bắc,Đông Bắc Bộ,CN. Thanh Hóa,Phòng giao dịch Phan Chu Trinh,Thanh Hóa,Thành phố Thanh Hóa,"Số 15 Khu nhà ở Thương Mại, đường Phan Chu Trinh, Phường Điện Biên, Thành phố Thanh Hóa, Thanh Hóa"
Khu vực Miền Bắc,Đông Bắc Bộ,CN. Thanh Hóa,Phòng giao dịch Lam Sơn,Thanh Hoá,Huyện Thọ Xuân,"Tiểu Khu 6,, Thị trấn Lam Sơn, Huyện Thọ Xuân, Thanh Hoá"
Khu vực Miền Bắc,Đông Bắc Bộ,CN. Uông Bí,Trụ sở,Quảng Ninh,Thành phố Uông Bí,"Số 277, đường Quang Trung, Tổ 24 A, khu 7, Phường Quang Trung, Thành phố Uông Bí, Quảng Ninh"
Khu vực Miền Bắc,Đông Bắc Bộ,CN. Uông Bí,Phòng giao dịch Mạo Khê,Quảng Ninh,Thị xã Đông Triều,"Số 196 Ngã 4, khu Hoàng Hoa Thám, Phường Mạo Khê, Thị Xã Đông Triều, Quảng Ninh"
Khu vực Miền Bắc,Tây Bắc Bộ,CN. Bắc Giang,Trụ sở,Bắc Giang,Thành phố Bắc Giang,"Tầng 1 (tầng trệt) tòa nhà trụ sở Viettel Bắc Giang lô A4, làn 2, đường Nguyễn Thị Minh Khai, Phường Hoàng Văn Thụ, Thành phố Bắc Giang, Bắc Giang"
Khu vực Miền Bắc,Tây Bắc Bộ,CN. Bắc Giang,Phòng giao dịch Lục Nam,Bắc Giang,Huyện Lục Nam,"Số 375 phố Bình Minh, Thị trấn Đồi Ngô, Huyện Lục Nam, Bắc Giang"
Khu vực Miền Bắc,Tây Bắc Bộ,CN. Bắc Ninh,Trụ sở,Bắc Ninh,Thành phố Bắc Ninh,"Tầng 1, Tầng 2 và Tầng 9 Tòa nhà trụ sở Ngân hàng TMCP Quân Đội Chi nhánh Bắc Ninh, Số 24 đường Lý Thái Tổ, Phường Đại Phúc, Thành phố Bắc Ninh, Bắc Ninh"
Khu vực Miền Bắc,Tây Bắc Bộ,CN. Bắc Ninh,Phòng giao dịch Yên Phong,Bắc Ninh,Huyện Yên Phong,"Tầng 1, tầng 2, tòa nhà Ven bắc đường TL286, khu ao Dân quân, phố Chờ, Thị trấn Chờ, Huyện Yên Phong, Bắc Ninh"
Khu vực Miền Bắc,Tây Bắc Bộ,CN. Hải Dương,Trụ sở,Hải Dương,Thành phố Hải Dương,"Tầng 1, tầng 2 số 248 đại lộ Nguyễn Lương Bằng - Phường Thanh Bình - Thành phố Hải Dương - Hải Dương"
Khu vực Miền Bắc,Tây Bắc Bộ,CN. Hải Dương,Phòng giao dịch Lê Thanh Nghị,Hải Dương,Thành phố Hải Dương,Số 481 - 483 Lê Thanh Nghị - Phường Lê Thanh Nghị - Thành phố Hải Dương - Hải Dương
Khu vực Miền Bắc,Tây Bắc Bộ,CN. Hải Dương,Phòng giao dịch Kinh Môn,Hải Dương,Thị xã Kinh Môn,"Thửa đất số 226, tờ bản đồ số 05 - Phường An Lưu - Thị Xã Kinh Môn - Hải Dương"
Khu vực Miền Bắc,Tây Bắc Bộ,CN. Hải Dương,Phòng giao dịch Chí Linh,Hải Dương,Thành phố Chí Linh,"Số 10, 12 đường Thái Học 2 - Phường Sao Đỏ - Thành phố Chí Linh - Hải Dương"
Khu vực Miền Bắc,Tây Bắc Bộ,CN. Hòa Bình,Trụ sở,Hòa Bình,Thành phố Hòa Bình,"Tầng 1, tầng 2 tòa nhà Viettel, đường Trần Hưng Đạo, tổ 8, Phường Quỳnh Lâm, Thành phố Hòa Bình, Hòa Bình"
Khu vực Miền Bắc,Tây Bắc Bộ,CN. Hưng Yên,Trụ sở,Hưng Yên,Thành phố Hưng Yên,"Tầng 1, tầng 5 Tòa nhà Viettel, Số 537 đường Nguyễn Văn Linh - Phường Hiến Nam - Thành phố Hưng Yên - Hưng Yên"
Khu vực Miền Bắc,Tây Bắc Bộ,CN. Hưng Yên,Phòng giao dịch Văn Lâm,Hưng Yên,Huyện Văn Lâm,Phố Như Quỳnh - Thị Trấn Như Quỳnh - Huyện Văn Lâm - Hưng Yên
Khu vực Miền Bắc,Tây Bắc Bộ,CN. Hưng Yên,Phòng giao dịch Phố Nối,Hưng Yên,Thị xã Mỹ Hào,"Số 617 đường Nguyễn Văn Linh, Thị trần Bần Yên Nhân, Thị xã Mỹ Hào, Hưng Yên"
Khu vực Miền Bắc,Tây Bắc Bộ,CN. Hưng Yên,Phòng giao dịch Châu Giang,Hưng Yên,Huyện Khoái Châu,"Thửa đất số 123, tờ bản đồ số 06 - Thị Trấn Khoái Châu - Huyện Khoái Châu - Hưng Yên"
Khu vực Miền Bắc,Tây Bắc Bộ,CN. Lạng Sơn,Trụ sở,Lạng Sơn,Thành phố Lạng Sơn,"Số 88-90, Đường Trần Đăng Ninh, Phường Hoàng Văn Thụ, Thành phố Lạng Sơn, Lạng Sơn"
Khu vực Miền Bắc,Tây Bắc Bộ,CN. Lào Cai,Trụ sở,Lào Cai,Thành phố Lào Cai,"Số 119 Đường Hoàng Liên, Phường Cốc Lếu, Thành phố Lào Cai, Lào Cai"
Khu vực Miền Bắc,Tây Bắc Bộ,CN. Lào Cai,Phòng giao dịch Sapa,Lào Cai,Thị xã Sa Pa,"Số 196, tổ 02 Đường Thạch Sơn, Phường Sa Pa, Thị xã Sa Pa, Lào Cai"
Khu vực Miền Bắc,Tây Bắc Bộ,CN. Lào Cai,Phòng giao dịch Kim Tân,Lào Cai,Thành phố Lào Cai,"Tổ 12, Ngã 6, Phường Kim Tân, Thành phố Lào Cai, Lào Cai"
Khu vực Miền Bắc,Tây Bắc Bộ,CN. Sơn La,Trụ sở,Sơn La,Thành phố Sơn La,"Tầng 1 (tầng trệt) tòa nhà Viettel, số 1 Chu Văn Thịnh, Phường Tô Hiệu, Thành phố Sơn La, Sơn La"
Khu vực Miền Bắc,Tây Bắc Bộ,CN. Sơn La,Phòng giao dịch Mộc Châu,Sơn La,Huyện Mộc Châu,"Số 42 đường Lê Thanh Nghị, Thị trấn NT Mộc Châu, Huyện Mộc Châu, Sơn La"
Khu vực Miền Bắc,Tây Bắc Bộ,CN. Thái Nguyên,Trụ sở,Thái Nguyên,Thành phố Thái Nguyên,"Tầng 1 tầng 2 tòa nhà số 679, Đường Lương Ngọc Quyến, Phường Phan Đình Phùng, Thành phố Thái Nguyên, Thái Nguyên"
Khu vực Miền Bắc,Tây Bắc Bộ,CN. Thái Nguyên,Phòng giao dịch Trưng Vương,Thái Nguyên,Thành phố Thái Nguyên,"Tầng 1, Công trình Chợ Thái, Phường Trưng Vương, Thành phố Thái Nguyên, Thái Nguyên"
Khu vực Miền Bắc,Tây Bắc Bộ,CN. Thái Nguyên,Phòng giao dịch Phổ Yên,Thái Nguyên,Thành phố Phổ Yên,"Tổ dân phố số 2, Phường Ba Hàng, Thành phố Phổ Yên, Thái Nguyên"
Khu vực Miền Bắc,Tây Bắc Bộ,CN. Thái Nguyên,Phòng giao dịch Nam Thái Nguyên,Thái Nguyên,Thành phố Thái Nguyên,"Số 65, Đường Hoàng Văn Thụ, Phường Hoàng Văn Thụ, Thành phố Thái Nguyên, Thái Nguyên"
Khu vực Miền Bắc,Tây Bắc Bộ,CN. Từ Sơn,Trụ sở,Bắc Ninh,Thành phố Từ Sơn,"Tầng 1, Công ty TNHH Nam Hồng, đường Trần Phú, Phường Đình Bảng, Thành phố Từ Sơn, Bắc Ninh"
Khu vực Miền Bắc,Tây Bắc Bộ,CN. Tuyên Quang,Trụ sở,Tuyên Quang,Thành phố Tuyên Quang,"Số 155,Đường Bình Thuận, Tổ 8, Phường Tân Quang, Thành Phố Tuyên Quang, Tuyên Quang"
Khu vực Miền Bắc,Tây Bắc Bộ,CN. Việt Trì,Trụ sở,Phú Thọ,Thành phố Việt Trì,Số 1596 đường Hùng Vương - Phường Gia Cẩm - Thành phố Việt Trì - Phú Thọ
Khu vực Miền Bắc,Tây Bắc Bộ,CN. Việt Trì,Phòng giao dịch Phú Hộ,Phú Thọ,Thị xã Phú Thọ,"Số 63, Khu 12 - Xã Phú Hộ - Thị Xã Phú Thọ - Phú Thọ"
Khu vực Miền Bắc,Tây Bắc Bộ,CN. Việt Trì,Phòng giao dịch Nam Việt Trì,Phú Thọ,Thành phố Việt Trì,Số 779 Đại Lộ Hùng Vương - Phường Bến Gót - Thành phố Việt Trì - Phú Thọ
Khu vực Miền Bắc,Tây Bắc Bộ,CN. Việt Trì,Phòng giao dịch Lâm Thao,Phú Thọ,Huyện Lâm Thao,"Một phần tầng 1, Số nhà 179, khu 5,, Thị trấn Hùng Sơn, Huyện Lâm Thao, Phú Thọ"
Khu vực Miền Bắc,Tây Bắc Bộ,CN. Việt Trì,Phòng giao dịch Đền Hùng,Phú Thọ,Thành phố Việt Trì,"Trạm khách T44, quân Khu II, khu 1 - Phường Vân Phú - Thành phố Việt Trì - Phú Thọ"
Khu vực Miền Bắc,Tây Bắc Bộ,CN. Vĩnh Phúc,Trụ sở,Vĩnh Phúc,Thành phố Vĩnh Yên,"Một phần tầng 1
Tòa nhà Viettel Vĩnh Phúc- KĐT Chùa Hà Tiên, Phường Liên Bảo, Thành phố Vĩnh Yên, Vĩnh Phúc"
Khu vực Miền Bắc,Tây Bắc Bộ,CN. Vĩnh Phúc,Phòng giao dịch Yên Lạc,Vĩnh Phúc,Huyện Yên Lạc,"194 Dương Tĩnh, tổ dân phố 3 Đoài, Thị trấn Yên Lạc, Huyện Yên Lạc, Vĩnh Phúc"
Khu vực Miền Bắc,Tây Bắc Bộ,CN. Vĩnh Phúc,Phòng giao dịch Phúc Yên,Vĩnh Phúc,Thành phố Phúc Yên,"Số 65 đường Trần Hưng Đạo, Phường Hùng Vương, Vĩnh Phúc"
Khu vực Miền Bắc,Tây Bắc Bộ,CN. Yên Bái,Trụ sở,Yên Bái,Thành phố Yên Bái,"Số 736 đường Điện Biên, tổ 8, Phường Minh Tân, Thành phố Yên Bái, Yên Bái"
Khu vực Miền Nam,Đông Nam Bộ,CN. Bà Rịa,Trụ sở,Bà Rịa - Vũng Tàu,Thành phố Bà Rịa,Số 86 - 88 đường Bạch Đằng - Phường Phước Trung - Thành phố Bà Rịa - Bà Rịa - Vũng Tàu
Khu vực Miền Nam,Đông Nam Bộ,CN. Bà Rịa,Phòng giao dịch Phú Mỹ,Bà Rịa - Vũng Tàu,Thị xã Phú Mỹ,"Số 280 - 282 đường Độc Lập, Phường Phú Mỹ, Quận 7, Bà Rịa - Vũng Tàu"
Khu vực Miền Nam,Đông Nam Bộ,CN. Bảo Lộc,Trụ sở,Lâm Đồng,Thành phố Bảo Lộc,Số 249 Đường Trần Phú - Phường 1 - Thành phố Bảo Lộc - Lâm Đồng
Khu vực Miền Nam,Đông Nam Bộ,CN. Bảo Lộc,Phòng giao dịch Di Linh,Lâm Đồng,Huyện Di Linh,Số 725 đường Hùng Vương - Thị Trấn Di Linh - Huyện Di Linh - Lâm Đồng
Khu vực Miền Nam,Đông Nam Bộ,CN. Bình Dương,Trụ sở,Bình Dương,Thành phố Thủ Dầu Một,"Số 306 Đại lộ Bình Dương, Phường Phú Hòa, Thành phố Thủ Dầu Một, Bình Dương"
Khu vực Miền Nam,Đông Nam Bộ,CN. Bình Dương,Phòng giao dịch Uyên Hưng,Bình Dương,Thành phố Tân Uyên,Thửa đất số 53 tờ bản đồ 10 - Phường Uyên Hưng - Thành phố Tân Uyên - Bình Dương
Khu vực Miền Nam,Đông Nam Bộ,CN. Bình Dương,Phòng giao dịch Thuận An,Bình Dương,Thành phố Thuận An,Số 9 đường Nguyễn Văn Tiết - Phường Lái Thiêu - Thành phố Thuận An - Bình Dương
Khu vực Miền Nam,Đông Nam Bộ,CN. Bình Dương,Phòng giao dịch Bến Cát,Bình Dương,Thị xã Bến Cát,Số 432 đường 30/4 khu phố 2 - Phường Mỹ Phước - Thị Xã Bến Cát - Bình Dương
Khu vực Miền Nam,Đông Nam Bộ,CN. Bình Phước,Trụ sở,Bình Phước,Thành phố Đồng Xoài,"Thửa đất số 225; 226, tờ bản đồ số 45, đường Phú Riềng Đỏ, Phường Tân Thiện, Thành phố Đồng Xoài, Bình Phước"
Khu vực Miền Nam,Đông Nam Bộ,CN. Bình Phước,Phòng giao dịch Phước Long,Bình Phước,Thị xã Phước Long,"Thửa đất số 16, tờ bản đồ số 03, khu phố 5 - Phường Long Phước - Thị xã  Phước Long - Bình Phước"
Khu vực Miền Nam,Đông Nam Bộ,CN. Bình Phước,Phòng giao dịch Chơn Thành,Bình Phước,Thị xã Chơn Thành,"Thửa đất số 30, tờ bản đồ số 47, Ấp 4 - Phường Minh Thành - Thị xã Chơn Thành - Bình Phước"
Khu vực Miền Nam,Đông Nam Bộ,CN. Bình Phước,Phòng giao dịch Bình Long,Bình Phước,Thị xã Bình Long,"Thửa đất số 204, Tờ bản đồ 35, khu phố Phú Trung - Phường An Lộc - Thị Xã Bình Long - Bình Phước"
Khu vực Miền Nam,Đông Nam Bộ,CN. Bình Thuận,Trụ sở,Bình Thuận,Thành phố Phan Thiết,"Tầng 1( tầng trệt) tòa nhà Viettel Bình Thuận, Khu dân cư Hùng Vương, đường Tôn Đức Thắng, Phường Phú Thủy, Thành phố  Phan Thiết, Bình Thuận"
Khu vực Miền Nam,Đông Nam Bộ,CN. Bình Thuận,Phòng giao dịch Bắc Bình,Bình Thuận,Huyện Bắc Bình,Số 433 đường Nguyễn Tất Thành khu phố Xuân Hội - Thị Trấn Chợ Lầu - Huyện Bắc Bình - Bình Thuận
Khu vực Miền Nam,Đông Nam Bộ,CN. Đồng Nai,Trụ sở,Đồng Nai,Thành phố Biên Hòa,Số K23 đường Võ Thị Sáu - Phường Thống Nhất - Thành phố Biên Hòa - Đồng Nai
Khu vực Miền Nam,Đông Nam Bộ,CN. Đồng Nai,Phòng giao dịch Trảng Bom,Đồng Nai,Huyện Trảng Bom,Số 8/3A ấp Thanh Hóa - Xã Hố Nai 3 - Huyện Trảng Bom - Đồng Nai
Khu vực Miền Nam,Đông Nam Bộ,CN. Đồng Nai,Phòng giao dịch Tân Hòa,Đồng Nai,Thành phố Biên Hòa,Số 78/16 Khu phố 8 - Phường Tân Hòa - Thành phố Biên Hòa - Đồng Nai
Khu vực Miền Nam,Đông Nam Bộ,CN. Đồng Nai,Phòng giao dịch Tam Hiệp,Đồng Nai,Thành phố Biên Hòa,Số 76/8 đường Phạm Văn Thuận - Phường Tam Hiệp - Thành phố Biên Hòa - Đồng Nai
Khu vực Miền Nam,Đông Nam Bộ,CN. Lâm Đồng,Trụ sở,Lâm Đồng,Thành phố Đà Lạt,Số 26 Phan Đình Phùng - Phường 1 - Thành phố Đà Lạt - Lâm Đồng
Khu vực Miền Nam,Đông Nam Bộ,CN. Lâm Đồng,Phòng giao dịch Lâm Hà,Lâm Đồng,Huyện Lâm Hà,Số 750 Hùng Vương - Thị Trấn Đinh Văn - Huyện Lâm Hà - Lâm Đồng
Khu vực Miền Nam,Đông Nam Bộ,CN. Lâm Đồng,Phòng giao dịch Đức Trọng,Lâm Đồng,Huyện Đức Trọng,"Số 691 Quốc lộ 20, khu phố 1 - Thị Trấn Liên Nghĩa - Huyện Đức Trọng - Lâm Đồng"
Khu vực Miền Nam,Đông Nam Bộ,CN. Long Khánh,Trụ sở,Đồng Nai,Thành phố Long Khánh,"Số 21 - 23 đường Nguyễn Trãi, Khu phố 3, Phường Xuân Hòa, Thành phố Long khánh, Đồng Nai"
Khu vực Miền Nam,Đông Nam Bộ,CN. Long Khánh,Phòng giao dịch Xuân Lộc,Đồng Nai,Huyện Xuân Lộc,"Số 132, đường Hùng Vương, khu phố 5, Thị trấn Gia Ray, Huyện Xuân Lộc, Đồng Nai"
Khu vực Miền Nam,Đông Nam Bộ,CN. Long Thành,Trụ sở,Đồng Nai,Huyện Long Thành,"Thửa đất số 49, tờ bản đồ số 57 (11-3) - Số 301, Lê Duẩn, khu Phước Hải, Thị trấn Long Thành, Huyện Long Thành, Đồng Nai"
Khu vực Miền Nam,Đông Nam Bộ,CN. Long Thành,Phòng giao dịch Nhơn Trạch,Đồng Nai,Huyện Nhơn Trạch,"Lô B-1, B-2, B-3, khu dân cư Thăng Long Home Hiệp Phước, đường TL25B, ấp 3, Xã Hiệp Phước, Huyện Nhơn Trạch, Đồng Nai"
Khu vực Miền Nam,Đông Nam Bộ,CN. Nam Bình Dương,Trụ sở,Bình Dương,Thành phố Dĩ An,"Số 01 và số 03 đường D3 khu đô thị thương mại dịch vụ Sóng Thần, khu phố Thống Nhất 1 - Phường Dĩ An - Thành phố  Dĩ An - Bình Dương"
Khu vực Miền Nam,Đông Nam Bộ,CN. Nam Bình Dương,Phòng giao dịch Sóng Thần,Bình Dương,Thành phố Dĩ An,20 Nguyễn An Ninh KP Nhị Đồng 2 - Phường Dĩ An - Thành phố  Dĩ An - Bình Dương
Khu vực Miền Nam,Đông Nam Bộ,CN. Tân Uyên,Trụ sở,Bình Dương,Thành phố Tân Uyên,Số 63/2 đường DT 746 Khu phố Bình Hòa 1 - Phường Tân Phước Khánh - Thành phố Tân Uyên - Bình Dương
Khu vực Miền Nam,Đông Nam Bộ,CN. Tây Ninh,Trụ sở,Tây Ninh,Thành phố Tây Ninh,"Số 225 Đường 30/4, Khu phố 1 - Phường 1 - Thành phố Tây Ninh - Tây Ninh"
Khu vực Miền Nam,Đông Nam Bộ,CN. Tây Ninh,Phòng giao dịch Tân Châu 1,Tây Ninh,Huyện Tân Châu,"Số 95 Trần Văn Trà, khu phố 2 - Thị Trấn Tân Châu - Huyện Tân Châu - Tây Ninh"
Khu vực Miền Nam,Đông Nam Bộ,CN. Tây Ninh,Phòng giao dịch Tân Biên,Tây Ninh,Huyện Tân Biên,"Số 45 đường Nguyễn Văn Linh, khu phố 3 - Thị Trấn Tân Biên - Huyện Tân Biên - Tây Ninh"
Khu vực Miền Nam,Đông Nam Bộ,CN. Tây Ninh,Phòng giao dịch Gò Dầu,Tây Ninh,Huyện Gò Dầu,"Số 195 đường Xuyên Á, Khu phố Nội Ô B - Thị Trấn Gò Dầu - Huyện Gò Dầu - Tây Ninh"
Khu vực Miền Nam,Đông Nam Bộ,CN. Vũng Tàu,Trụ sở,Bà Rịa - Vũng Tàu,Thành phố Vũng Tàu,Số 81 Nguyễn Thái Học - Phường 7 - Thành phố Vũng Tàu - Bà Rịa - Vũng Tàu
Khu vực Miền Nam,Đông Nam Bộ,CN. Vũng Tàu,Phòng giao dịch Rạch Dừa,Bà Rịa - Vũng Tàu,Thành phố Vũng Tàu,Số 478 đường 30/4 - Phường Rạch Dừa - Thành phố Vũng Tàu - Bà Rịa - Vũng Tàu
Khu vực Miền Nam,Đông Nam Bộ,CN. Vũng Tàu,Phòng giao dịch Nam Kỳ Khởi nghĩa,Bà Rịa - Vũng Tàu,Thành phố Vũng Tàu,Số 153 155 đường Nam Kỳ Khởi Nghĩa - Phường 3 - Thành phố Vũng Tàu - Bà Rịa - Vũng Tàu
Khu vực Miền Nam,Đông Nam Bộ,CN. Vũng Tàu,Phòng giao dịch Long Điền,Bà Rịa - Vũng Tàu,Huyện Long Điền,"Số 48 tổ 6, ấp lò vôi - Xã Phước Hưng - Huyện Long Điền - Bà Rịa - Vũng Tàu"
Khu vực Miền Nam,Tây Nam Bộ,CN. An Giang,Trụ sở,An Giang,Thành phố Long Xuyên,128 - 130 Nguyễn Trãi - Phường Mỹ Long - Thành phố Long Xuyên - An Giang
Khu vực Miền Nam,Tây Nam Bộ,CN. An Giang,Phòng giao dịch Tân Châu 2,An Giang,Thị xã Tân Châu,"Số 166 đường Tôn Đức Thắng, khóm Long Thị D - Phường Long Thạnh - Thị Xã Tân Châu - An Giang"
Khu vực Miền Nam,Tây Nam Bộ,CN. An Giang,Phòng giao dịch Chợ Mới,An Giang,Huyện Chợ Mới,"Tỉnh lộ 942, ấp Thị - Thị Trấn Chợ Mới - Huyện Chợ Mới - An Giang"
Khu vực Miền Nam,Tây Nam Bộ,CN. An Giang,Phòng giao dịch Châu Phú,An Giang,Huyện Châu Phú,"Số nhà 534A, đường Quốc lộ 91, tổ 3, khóm Vĩnh Lộc - Thị Trấn Cái Dầu - Huyện Châu Phú - An Giang"
Khu vực Miền Nam,Tây Nam Bộ,CN. Bạc Liêu,Trụ sở,Bạc Liêu,Thành phố Bạc Liêu,"Số 370 - 372 Trần Phú, Phường 7, Thành Phố Bạc Liêu, Bạc Liêu"
Khu vực Miền Nam,Tây Nam Bộ,CN. Bến Tre,Trụ sở,Bến Tre,Thành phố Bến Tre,"Thửa đất số 266, Tờ bản đồ số 38, Phường Phú Khương, Thành phố Bến Tre, Bến Tre"
Khu vực Miền Nam,Tây Nam Bộ,CN. Cà Mau,Trụ sở,Cà Mau,Thành phố Cà Mau,"Số 44-46, đường Hùng Vương, Phường 5, Thành phố Cà Mau, Cà Mau"
Khu vực Miền Nam,Tây Nam Bộ,CN. Cần Thơ,Trụ sở,Cần Thơ,Quận Ninh Kiều,"Tầng 1, tầng 2 và tầng 7 tòa nhà Ngân hàng TMCP Quân Đội – Chi nhánh Cần Thơ, số 77, 77B Võ Văn Tần, Phường Tân An, Quận Ninh Kiều, Cần Thơ"
Khu vực Miền Nam,Tây Nam Bộ,CN. Cần Thơ,Phòng giao dịch Thốt Nốt,Cần Thơ,Quận Thốt Nốt,"553 QL91, KV Phụng Thạnh 1 - Phường Thốt Nốt - Quận Thốt Nốt - Cần Thơ"
Khu vực Miền Nam,Tây Nam Bộ,CN. Cần Thơ,Phòng giao dịch Ô Môn,Cần Thơ,Quận Ô Môn,Số 1177 đường Tôn Đức Thắng (QL91) khu vực 11 - Phường Châu Văn Liêm - Quận Ô Môn - Cần Thơ
Khu vực Miền Nam,Tây Nam Bộ,CN. Cần Thơ,Phòng giao dịch Ninh Kiều,Cần Thơ,Quận Ninh Kiều,Số 122 đường 3/2 - Phường Hưng Lợi - Quận Ninh Kiều - Cần Thơ
Khu vực Miền Nam,Tây Nam Bộ,CN. Đồng Tháp,Trụ sở,Đồng Tháp,Thành phố Cao Lãnh,Số 204-206 đường Nguyễn Huệ - Phường 2 - Thành phố Cao Lãnh - Đồng Tháp
Khu vực Miền Nam,Tây Nam Bộ,CN. Đồng Tháp,Phòng giao dịch Hồng Ngự,Đồng Tháp,Thành phố Hồng Ngự,Số 66 - 68 đường Võ Văn Kiệt - Phường An Thạnh - Thành phố Hồng Ngự - Đồng Tháp
Khu vực Miền Nam,Tây Nam Bộ,CN. Kiên Giang,Trụ sở,Kiên Giang,Thành phố Rạch Giá,"Số 24, 26, 28 đường Trần Phú - Phường Vĩnh Thanh - Thành phố Rạch Giá - Kiên Giang"
Khu vực Miền Nam,Tây Nam Bộ,CN. Kiên Giang,Phòng giao dịch Châu Thành,Kiên Giang,Huyện Tân Hiệp,Số 103 ấp Đông Hưng - Thị Trấn Tân Hiệp - Huyện Tân Hiệp - Kiên Giang
Khu vực Miền Nam,Tây Nam Bộ,CN. Long An,Trụ sở,Long An,Thành phố Tân An,Số 122-124 Hùng Vương - Phường 6 - Thành phố Tân An - Long An
Khu vực Miền Nam,Tây Nam Bộ,CN. Long An,Phòng giao dịch Đức Hòa,Long An,Huyện Đức Hòa,"Số 789E tổ 5, ấp 5 - Xã Đức Hòa Đông - Huyện Đức Hòa - Long An"
Khu vực Miền Nam,Tây Nam Bộ,CN. Long An,Phòng giao dịch Bến Lức,Long An,Huyện Bến Lức,Số 239 đường Nguyễn Hữu Thọ Khu phố 2 - Thị trấn Bến Lức - Huyện Bến Lức - Long An
Khu vực Miền Nam,Tây Nam Bộ,CN. Phú Quốc,Trụ sở,Kiên Giang,Huyện Phú Quốc,Số 249-251 Nguyễn Trung Trực Khu phố 5 - Phường Dương Đông - Thành phố Phú Quốc - Kiên Giang
Khu vực Miền Nam,Tây Nam Bộ,CN. Phú Quốc,Phòng giao dịch An Thới,Kiên Giang,Huyện Phú Quốc,Số 249-251 Nguyễn Trung Trực Khu phố 5 - Phường Dương Đông - Thành phố Phú Quốc - Kiên Giang
Khu vực Miền Nam,Tây Nam Bộ,CN. Sóc Trăng,Trụ sở,Sóc Trăng,Thành phố Sóc Trăng,Số 26 Lê Duẩn khóm 7 - Phường 3 - Thành phố Sóc Trăng - Sóc Trăng
Khu vực Miền Nam,Tây Nam Bộ,CN. Tây Đô,Trụ sở,Cần Thơ,Quận Bình Thuỷ,"Số 43 Đường CMT8, Phường An Thới, Quận Bình Thuỷ, Cần Thơ"
Khu vực Miền Nam,Tây Nam Bộ,CN. Tiền Giang,Trụ sở,Tiền Giang,Thành phố Mỹ Tho,Số 116 đường Nam Kỳ Khởi Nghĩa - Phường 1 - Thành phố Mỹ Tho - Tiền Giang
Khu vực Miền Nam,Tây Nam Bộ,CN. Tiền Giang,Phòng giao dịch Mỹ Tho,Tiền Giang,Thành phố Mỹ Tho,"Tầng 1 tòa nhà Viettel Tiền Giang, số 66 khu phố 5, đường Đinh Bộ Lĩnh - Phường 9 - Thành phố Mỹ Tho - Tiền Giang"
Khu vực Miền Nam,Tây Nam Bộ,CN. Tiền Giang,Phòng giao dịch Cai Lậy,Tiền Giang,Thị xã Cai Lậy,"Tầng trệt tầng 2 tòa nhà công ty Cổ phần Dược phẩm CALAPHARCO, Quốc lộ 1 - Phường 4 - Thị Xã Cai Lậy - Tiền Giang"
Khu vực Miền Nam,Tây Nam Bộ,CN. Trà Vinh,Trụ sở,Trà Vinh,Thành phố Trà Vinh,"Số TRV-PG2-05 TRV-PG2-05A, TRV-PG2-06, khóm 3 - Phường 2 - Thành phố Trà Vinh - Trà Vinh"
Khu vực Miền Nam,Tây Nam Bộ,CN. Vĩnh Long,Trụ sở,Vĩnh Long,Thành phố Vĩnh Long,Số 1D - 1E đường Hoàng Thái Hiếu - Phường 1 - Thành phố Vĩnh Long - Vĩnh Long
Khu vực Miền Nam,Tây Nam Bộ,CN. Vĩnh Long,Phòng giao dịch Bình Minh,Vĩnh Long,Thị xã Bình Minh,"Số 79A - 79B đường Nguyễn Văn Thảnh, tổ 6, Khóm 2 - Phường Cái Vồn - Thị Xã Bình Minh - Vĩnh Long"
Khu vực Miền Trung,Miền Trung,CN. Bắc Đà Nẵng,Trụ sở,Đà Nẵng,Quận Liên Chiểu,"563 đường Tôn Đức Thắng, tổ 50, Phường Hòa Khánh Nam, Quận Liên Chiểu, Đà Nẵng"
Khu vực Miền Trung,Miền Trung,CN. Bình Định,Trụ sở,Bình Định,Thành phố Quy Nhơn,"Tầng 1, tầng 2 và tầng 3 tòa nhà Ngân hàng TMCP Quân Đội, số nhà 322 đường Nguyễn Thái Học - Phường Ngô Mây - Thành phố Quy Nhơn - Bình Định"
Khu vực Miền Trung,Miền Trung,CN. Bình Định,Phòng giao dịch Diêu Trì,Bình Định,Thành phố Quy Nhơn,Số 50-52 đường Lạc Long Quân - Phường Trần Quang Diệu - Thành phố Quy Nhơn - Bình Định
Khu vực Miền Trung,Miền Trung,CN. Bình Định,Phòng giao dịch An Nhơn,Bình Định,Thị xã An Nhơn,Số 285 - Phường Trần Hưng Đạo - Thành phố Quy Nhơn - Bình Định
Khu vực Miền Trung,Miền Trung,CN. Đà Nẵng,Trụ sở,Đà Nẵng,Quận Hải Châu,"Tầng trệt, tầng lửng, tầng 6 số 174 Lê Đình Lý - Phường Hòa Thuận Tây - Quận Hải Châu - Đà Nẵng"
Khu vực Miền Trung,Miền Trung,CN. Đà Nẵng,Phòng giao dịch Sông Hàn,Đà Nẵng,Quận Hải Châu,"Tầng 1, 2, 3 tòa nhà Lô 14-15 đường Nguyễn Văn Linh nối dài - Phường Hòa Thuận Tây - Quận Hải Châu - Đà Nẵng"
Khu vực Miền Trung,Miền Trung,CN. Đà Nẵng,Phòng giao dịch Hòa Thọ,Đà Nẵng,Quận Cẩm Lệ,Số 142 đường Ông Ích Đường - Phường Khuê Trung - Quận Cẩm Lệ - Đà Nẵng
Khu vực Miền Trung,Miền Trung,CN. Đăk Lăk,Trụ sở,Đắk Lắk,Thành phố Buôn Ma Thuột,"Số 37 Hai Bà Trưng, Phường Thắng Lợi, TP.Buôn Ma Thuột, Đắk Lắk"
Khu vực Miền Trung,Miền Trung,CN. Đăk Lăk,Phòng giao dịch Eakar,Đắk Lắk,Huyện Eakar,Số 148 đường Nguyễn Tất Thành - Thị Trấn EaKar - Huyện Eakar - Đắk Lắk
Khu vực Miền Trung,Miền Trung,CN. Đăk Lăk,Phòng giao dịch Cư M'gar,Đắk Lắk,Huyện Cư M'Gar,"Số 66, đường Hùng Vương - Thị Trấn Quảng Phú - Huyện Cư M'Gar - Đắk Lắk"
Khu vực Miền Trung,Miền Trung,CN. Đăk Lăk,Phòng giao dịch Buôn Hồ,Đắk Lắk,Thị xã Buôn Hồ,Số 683 - 685 đường Hùng Vương - Phường An Lạc - Thị Xã Buôn Hồ - Đắk Lắk
Khu vực Miền Trung,Miền Trung,CN. Gia Lai,Trụ sở,Gia Lai,Thành phố Pleiku,"Số 08 Lê Lai, Phường Tây Sơn, Thành phố  Pleiku, Gia Lai"
Khu vực Miền Trung,Miền Trung,CN. Gia Lai,Phòng giao dịch Pleiku,Gia Lai,Thành phố Pleiku,"Số 07 Nguyễn Tất Thành, Phường Hoa Lư, Thành phố  Pleiku, Gia Lai"
Khu vực Miền Trung,Miền Trung,CN. Gia Lai,Phòng giao dịch Chư Sê,Gia Lai,Huyện Chư Sê,"Số 868 đường Hùng Vương, Thị trấn Chư Sê, Huyện Chư Sê, Gia Lai"
Khu vực Miền Trung,Miền Trung,CN. Hội An,Trụ sở,Quảng Nam,Thành phố Hội An,"Số 594 Hai Bà Trưng, Phường Cẩm Phô, Thành phố Hội An, Quảng Nam"
Khu vực Miền Trung,Miền Trung,CN. Huế,Trụ sở,Huế,Thành phố Huế,"Một phần tầng 1,2,3, Tòa nhà số 07 Nguyễn Tri Phương - Phường Phú Hội - Thành phố Huế - Thừa Thiên - Huế"
Khu vực Miền Trung,Miền Trung,CN. Huế,Phòng giao dịch Nam Vĩ Dạ,Huế,Thành phố Huế,Số 109 Phạm Văn Đồng - Phường Vỹ Dạ - Thành phố Huế - Thừa Thiên - Huế
Khu vực Miền Trung,Miền Trung,CN. Huế,Phòng giao dịch Nam Trường Tiền,Huế,Thành phố Huế,Số 11 Lý Thường Kiệt - Phường Phú Nhuận - Thành phố Huế - Thừa Thiên - Huế
Khu vực Miền Trung,Miền Trung,CN. Huế,Phòng giao dịch Hương Thủy,Huế,Thị xã Hương Thủy,"Số 1068 đường Nguyễn Tất Thành, Phường Phú Bài, Thị xã Hương Thuỷ, Thừa Thiên - Huế"
Khu vực Miền Trung,Miền Trung,CN. Khánh Hòa,Trụ sở,Khánh Hòa,Thành phố Nha Trang,Số 09 đường Lê Thánh Tôn - Phường Lộc Thọ - Thành phố Nha Trang - Khánh Hòa
Khu vực Miền Trung,Miền Trung,CN. Khánh Hòa,Phòng giao dịch Vĩnh Hải,Khánh Hòa,Thành phố Nha Trang,Số 554 đường 2 tháng 4 - Phường Vĩnh Phước - Thành phố Nha Trang - Khánh Hòa
Khu vực Miền Trung,Miền Trung,CN. Khánh Hòa,Phòng giao dịch Nha Trang,Khánh Hòa,Thành phố Nha Trang,"Lô số 199, khu dân cư Nam và Bắc đường Phong Châu - Phường Phước Hải - Thành phố Nha Trang - Khánh Hòa"
Khu vực Miền Trung,Miền Trung,CN. Khánh Hòa,Phòng giao dịch Hoàng Diệu,Khánh Hòa,Thành phố Nha Trang,27/21 đường 7B - Phường Phước Long - Thành phố Nha Trang - Khánh Hòa
Khu vực Miền Trung,Miền Trung,CN. Nam Đà Nẵng,Trụ sở,Đà Nẵng,Quận Hải Châu,"Số 152 đường 2/9, Phường Hòa Thuận Đông, Quận Hải Châu, Đà Nẵng"
Khu vực Miền Trung,Miền Trung,CN. Nam Đà Nẵng,Phòng giao dịch Sơn Trà,Đà Nẵng,Quận Ngũ Hành Sơn,"Tầng 1, tầng lửng Tòa nhà số 222-224 đường Ngũ Hành Sơn, Phường Mỹ An, Quận Ngũ Hành Sơn, Đà Nẵng"
Khu vực Miền Trung,Miền Trung,CN. Nam Đà Nẵng,Phòng giao dịch Hải Châu,Đà Nẵng,Quận Hải Châu,"Số 199 đường Đống Đa, Phường Thạch Thang, Quận Hải Châu, Đà Nẵng"
Khu vực Miền Trung,Miền Trung,CN. Nam Đà Nẵng,Phòng giao dịch Cẩm Lệ,Đà Nẵng,Quận Cẩm Lệ,"Tầng 1 tòa nhà Công ty cổ phần xây dựng công trình 545, số 324 Nguyễn Hữu Thọ, Phường Khuê Trung, Quận Cẩm Lệ, Đà Nẵng"
Khu vực Miền Trung,Miền Trung,CN. Nam Khánh Hòa,Trụ sở,Khánh Hòa,Thành phố Cam Ranh,"Số 151 đường Nguyễn Chí Thanh, Phường Cam Nghĩa, Thành phố Cam Ranh, Khánh Hòa"
Khu vực Miền Trung,Miền Trung,CN. Nam Khánh Hòa,Phòng giao dịch Hùng Vương,Khánh Hòa,Thành phố Cam Ranh,"Số 2216 đại lộ Hùng Vương, Phường Ba Ngòi, Thành phố Cam Ranh, Khánh Hòa"
Khu vực Miền Trung,Miền Trung,CN. Ninh Thuận,Trụ sở,Ninh Thuận,Thành phố Phan Rang - Tháp Chàm,"Số 398 đường Thống Nhất, Phường Mỹ Hương, TP. Phan Rang-Tháp Chàm, Ninh Thuận"
Khu vực Miền Trung,Miền Trung,CN. Phú Yên,Trụ sở,Phú Yên,Thành phố Tuy Hòa,"Số 99A - 101 đường Hùng Vương, Phường 6, TP Tuy Hòa, Phú Yên"
Khu vực Miền Trung,Miền Trung,CN. Quảng Bình,Trụ sở,Quảng Bình,Thành phố Đồng Hới,"Số 58 đường Quang Trung, Phường Đồng Hải, Thành phố Đồng Hới, Quảng Bình"
Khu vực Miền Trung,Miền Trung,CN. Quảng Nam,Trụ sở,Quảng Nam,Thành phố Tam Kỳ,"Số 284 Phan Chu Trinh, Phường An Xuân, Thành phố Tam Kỳ, Quảng Nam"
Khu vực Miền Trung,Miền Trung,CN. Quảng Nam,Phòng giao dịch Núi Thành,Quảng Nam,Huyện Núi Thành,"Số 204 Phạm Văn Đồng, khối phố 2, Thị trấn Núi Thành, Huyện Núi Thành, Quảng Nam"
Khu vực Miền Trung,Miền Trung,CN. Quảng Nam,Phòng giao dịch Duy Xuyên,Quảng Nam,Huyện Duy Xuyên,"Số 74 - 76 Điện Biên Phủ, khối phố Long Xuyên 2, Thị trấn Nam Phước, Huyện Duy Xuyên, Quảng Nam"
Khu vực Miền Trung,Miền Trung,CN. Quảng Ngãi,Trụ sở,Quảng Ngãi,Thành phố Quảng Ngãi,"Nhà khách T50, số 168 đường Hùng Vương - Phường Trần Phú - Thành phố Quảng Ngãi - Quảng Ngãi"
Khu vực Miền Trung,Miền Trung,CN. Quảng Ngãi,Phòng giao dịch Trà Khúc,Quảng Ngãi,Thành phố Quảng Ngãi,Số 24 Quang Trung - Phường Lê Hồng Phong - Thành phố Quảng Ngãi - Quảng Ngãi
Khu vực Miền Trung,Miền Trung,CN. Quảng Ngãi,Phòng giao dịch Nam Quảng Ngãi,Quảng Ngãi,Huyện Mộ Đức,Thôn Thạch Trụ Tây - Xã Đức Lân - Huyện Mộ Đức - Quảng Ngãi
Khu vực Miền Trung,Miền Trung,CN. Quảng Ngãi,Phòng giao dịch Bắc Quảng Ngãi,Quảng Ngãi,Huyện Bình Sơn,"Số 448 Phạm Văn Đồng, Tổ dân phố 4 - Thị Trấn Châu Ổ - Huyện Bình Sơn - Quảng Ngãi"
Khu vực Miền Trung,Miền Trung,CN. Quảng Trị,Trụ sở,Quảng Trị,Thành phố Đông Hà,"Số 134, quốc lộ 9, Phường 1, Thành phố Đông Hà, Quảng Trị"
Khu vực Miền Trung,Miền Trung,CN. Quảng Trị,Phòng giao dịch Khe Sanh,Quảng Trị,Huyện Hướng Hoá,"Số 144 Lê Duẩn, Thị trấn Khe Sanh, Huyện Hướng Hoá, Quảng Trị"
Khu vực TP Hồ Chí Minh,Hồ Chí Minh 1,CN. An Phú,Trụ sở,TP Hồ Chí Minh,Thành phố Thủ Đức,", Thành phố Thủ Đức, TP Hồ Chí Minh"
Khu vực TP Hồ Chí Minh,Hồ Chí Minh 1,CN. Bến Thành,Trụ sở,TP Hồ Chí Minh,Quận 3,"Số 414C-414D Nguyễn Thị Minh Khai, Phường 5, Quận 3, TP Hồ Chí Minh"
Khu vực TP Hồ Chí Minh,Hồ Chí Minh 1,CN. Bình Chánh,Trụ sở,TP Hồ Chí Minh,Huyện Bình Chánh,"Số 207 – 209 đường số 9A, khu dân cư Trung Sơn, ấp 4 - Xã Bình Hưng - Huyện Bình Chánh - TP Hồ Chí Minh"
Khu vực TP Hồ Chí Minh,Hồ Chí Minh 1,CN. Độc Lập,Trụ sở,TP Hồ Chí Minh,Quận 1,"Một phần tầng trệt và tầng 4, số 07 đường Nguyễn Thị Minh Khai - Phường Bến Nghé - Quận 1 - TP Hồ Chí Minh"
Khu vực TP Hồ Chí Minh,Hồ Chí Minh 1,CN. Hàm Nghi,Trụ sở,TP Hồ Chí Minh,Quận 1,"Tầng trệt (tầng 1), tầng 2 tòa nhà Beta số 55 Nam Kỳ Khởi Nghĩa - Phường Nguyễn Thái Bình - Quận 1 - TP Hồ Chí Minh"
Khu vực TP Hồ Chí Minh,Hồ Chí Minh 1,CN. Khánh Hội,Trụ sở,TP Hồ Chí Minh,Quận 4,"Số 192, 194 đường Khánh Hội, Phường 6, Quận 4, TP Hồ Chí Minh"
Khu vực TP Hồ Chí Minh,Hồ Chí Minh 1,CN. Lê Đại Hành,Trụ sở,TP Hồ Chí Minh,Quận 11,"Số 357A, 357C Lê Đại Hành - Phường 11 - Quận 11 - TP Hồ Chí Minh"
Khu vực TP Hồ Chí Minh,Hồ Chí Minh 1,CN. Nam Bình Chánh,Trụ sở,TP Hồ Chí Minh,Huyện Bình Chánh,"Số 139 đường Nguyễn Hữu Trí, Khu phố 5 - Thị Trấn Tân Túc - Huyện Bình Chánh - TP Hồ Chí Minh"
Khu vực TP Hồ Chí Minh,Hồ Chí Minh 1,CN. Nam Hồ Chí Minh,Trụ sở,TP Hồ Chí Minh,Huyện Nhà Bè,"Shophouse 88 - 90 - 92, The Park Residence - Phân khu 12 đường Nguyễn Hữu Thọ, Xã Phước Kiển, Huyện Nhà Bè, TP Hồ Chí Minh"
Khu vực TP Hồ Chí Minh,Hồ Chí Minh 1,CN. Nam Sài Gòn,Trụ sở,TP Hồ Chí Minh,Quận 7,"Tầng trệt, Tòa nhà M Building, số 09 đường số 08, Khu A, Đô thị Mới Nam Thành phố, Phường Tân Phú, Quận 7, TP Hồ Chí Minh"
Khu vực TP Hồ Chí Minh,Hồ Chí Minh 1,CN. Nam Sài Gòn,Phòng giao dịch Hiệp Phước,TP Hồ Chí Minh,Huyện Nhà Bè,"Số 470 Nguyễn Văn Tạo, ấp 2, Xã Long Thới, Huyện Nhà Bè, TP Hồ Chí Minh"
Khu vực TP Hồ Chí Minh,Hồ Chí Minh 1,CN. Nguyễn Tri Phương,Trụ sở,TP Hồ Chí Minh,Quận 10,"431-433 Nguyễn Tri Phương, Phường 08, Quận 10, TP Hồ Chí Minh"
Khu vực TP Hồ Chí Minh,Hồ Chí Minh 1,CN. Phú Xuân,Trụ sở,TP Hồ Chí Minh,Huyện Nhà Bè,"Số 2049 Huỳnh Tấn Phát, khu phố 6, Thị Trấn Nhà Bè, Huyện Nhà Bè, TP Hồ Chí Minh"
Khu vực TP Hồ Chí Minh,Hồ Chí Minh 1,CN. Quận 3,Trụ sở,TP Hồ Chí Minh,Quận 3,"Một phần diện tích tầng 1 và toàn bộ tầng 2 tòa nhà Số 161, 163 đường Trần Quốc Thảo, Phường 9, Quận 3, TP Hồ Chí Minh"
Khu vực TP Hồ Chí Minh,Hồ Chí Minh 1,CN. Quận 5,Trụ sở,TP Hồ Chí Minh,Quận 5,"Tầng trệt, tầng 1 và tầng 2 số 353 – 355 đường An Dương Vương, Phường 3, Quận 5, TP Hồ Chí Minh"
Khu vực TP Hồ Chí Minh,Hồ Chí Minh 1,CN. Quận 6,Trụ sở,TP Hồ Chí Minh,Quận 6,"Số 10 – 12 đường Hậu Giang, Phường 2, Quận 6, TP Hồ Chí Minh"
Khu vực TP Hồ Chí Minh,Hồ Chí Minh 1,CN. Quận 8,Trụ sở,TP Hồ Chí Minh,Quận 8,"Số 829 - 829A đường Tạ Quang Bửu, Phường 5, Quận 8, TP Hồ Chí Minh"
Khu vực TP Hồ Chí Minh,Hồ Chí Minh 1,CN. Quận 9,Trụ sở,TP Hồ Chí Minh,Quận 9,"Tầng 1 (tầng trệt), tầng 2, số 25B Lê Văn Việt, Phường Hiệp Phú, Quận 9, TP Hồ Chí Minh"
Khu vực TP Hồ Chí Minh,Hồ Chí Minh 1,CN. Sài Gòn,Trụ sở,TP Hồ Chí Minh,Quận 1,"Số 172 Hai Bà Trưng, Phường Đa Kao, Quận 1, TP Hồ Chí Minh"
Khu vực TP Hồ Chí Minh,Hồ Chí Minh 1,CN. Tân Cảng,Trụ sở,TP Hồ Chí Minh,Quận Bình Thạnh,150-150A đường Nguyễn Gia Trí - Phường 25 - Quận Bình Thạnh - TP Hồ Chí Minh
Khu vực TP Hồ Chí Minh,Hồ Chí Minh 1,CN. Tân Tạo,Trụ sở,TP Hồ Chí Minh,Huyện Bình Chánh,"Số B3/16 - B3/17, quốc lộ 1A, ấp 2, Xã Tân Kiên, Huyện Bình Chánh, TP Hồ Chí Minh"
Khu vực TP Hồ Chí Minh,Hồ Chí Minh 1,CN. Tân Tạo,Phòng giao dịch Đông Bình Chánh,TP Hồ Chí Minh,Huyện Bình Chánh,"Số 495 đường Quốc Lộ 50, Ấp 1, Xã Bình Hưng, Huyện Bình Chánh, TP Hồ Chí Minh"
Khu vực TP Hồ Chí Minh,Hồ Chí Minh 1,CN. Tân Thuận,Trụ sở,TP Hồ Chí Minh,Quận 7,"Tầng trệt, tầng lửng, tầng 1 , tầng 2 và tầng 3 tòa nhà số 300, 300A, 300B đường Huỳnh Tấn Phát, Phường Tân Thuận Tây, Quận 7, TP Hồ Chí Minh"
Khu vực TP Hồ Chí Minh,Hồ Chí Minh 1,CN. Thảo Điền,Trụ sở,TP Hồ Chí Minh,Thành phố Thủ Đức,Một phần tầng 1 - Số 12 Quốc Hương - Phường Thảo Điền - Thành phố Thủ Đức - TP Hồ Chí Minh
Khu vực TP Hồ Chí Minh,Hồ Chí Minh 1,CN. Thủ Đức,Trụ sở,TP Hồ Chí Minh,Thành phố Thủ Đức,Số 282 Võ Văn Ngân - Phường Bình Thọ - Thành phố Thủ Đức - TP Hồ Chí Minh
Khu vực TP Hồ Chí Minh,Hồ Chí Minh 1,CN. Vĩnh Lộc,Trụ sở,TP Hồ Chí Minh,Huyện Bình Chánh,"Số D3/11A đường Nguyễn Thị Tú, ấp 4 - Xã Vĩnh Lộc B - Huyện Bình Chánh - TP Hồ Chí Minh"
Khu vực TP Hồ Chí Minh,Hồ Chí Minh 1,Sở giao dịch 2,Trụ sở,TP Hồ Chí Minh,Quận 1,"Tầng 1 (tầng trệt), tầng 2 Tòa Nhà Sunny ToWer, Số 259 Trần Hưng Đạo - Phường Cô Giang - Quận 1 - TP Hồ Chí Minh"
Khu vực TP Hồ Chí Minh,Hồ Chí Minh 2,CN. 3 tháng 2,Trụ sở,TP Hồ Chí Minh,Quận 10,"Tầng 1, tầng 2 tòa nhà 198A đường 3/2, Phường 12, Quận 10, TP Hồ Chí Minh"
Khu vực TP Hồ Chí Minh,Hồ Chí Minh 2,CN. Bắc Sài Gòn,Trụ sở,TP Hồ Chí Minh,Quận Gò Vấp,"Số 3 Nguyễn Oanh, Phường 10, Quận Gò Vấp, TP Hồ Chí Minh"
Khu vực TP Hồ Chí Minh,Hồ Chí Minh 2,CN. Bình Tân,Trụ sở,TP Hồ Chí Minh,Huyện Bình Chánh,"Số D3/11A đường Nguyễn Thị Tú, ấp 4 - Xã Vĩnh Lộc B - Huyện Bình Chánh - TP Hồ Chí Minh"
Khu vực TP Hồ Chí Minh,Hồ Chí Minh 2,CN. Bình Thạnh,Trụ sở,TP Hồ Chí Minh,Quận Bình Thạnh,"Tầng 1, tầng lửng và tầng 2 số 310 đường Lê Quang Định, Phường 11, Quận Bình Thạnh, TP Hồ Chí Minh"
Khu vực TP Hồ Chí Minh,Hồ Chí Minh 2,CN. Củ Chi,Trụ sở,TP Hồ Chí Minh,Huyện Củ Chi,"Thửa đất số 71 và 72, tờ bản đồ số 19 - Thị Trấn Củ Chi - Huyện Củ Chi - TP Hồ Chí Minh"
Khu vực TP Hồ Chí Minh,Hồ Chí Minh 2,CN. Củ Chi,Phòng giao dịch Tân Quy,TP Hồ Chí Minh,Huyện Củ Chi,"Thửa đất số 16, Tờ bản đồ số 26 - Xã Tân Thạnh Tây - Huyện Củ Chi - TP Hồ Chí Minh"
Khu vực TP Hồ Chí Minh,Hồ Chí Minh 2,CN. Đinh Tiên Hoàng,Trụ sở,TP Hồ Chí Minh,Quận Bình Thạnh,"Tầng trệt, tầng lửng, tầng 1 số 86, 88 Đinh Tiên Hoàng, Phường 1, Quận Bình Thạnh, TP Hồ Chí Minh"
Khu vực TP Hồ Chí Minh,Hồ Chí Minh 2,CN. Đông Sài Gòn,Trụ sở,TP Hồ Chí Minh,Quận 3,Tầng trệt tòa nhà Số 538 đường CMT8 - Phường 11 - Quận 3 - TP Hồ Chí Minh
Khu vực TP Hồ Chí Minh,Hồ Chí Minh 2,CN. Gia Định,Trụ sở,TP Hồ Chí Minh,Quận Bình Thạnh,"Số 3 Hoàng Hoa Thám, Phường 6, Quận Bình Thạnh, TP Hồ Chí Minh"
Khu vực TP Hồ Chí Minh,Hồ Chí Minh 2,CN. Hồ Chí Minh,Trụ sở,TP Hồ Chí Minh,Quận Tân Bình,"Số 18B đường Cộng Hòa, Phường 4, Quận Tân Bình, TP Hồ Chí Minh"
Khu vực TP Hồ Chí Minh,Hồ Chí Minh 2,CN. Lê Văn Sỹ,Trụ sở,TP Hồ Chí Minh,Quận Phú Nhuận,"Tầng trệt, tầng 1, tầng 2 và tầng 3 số 67 Lê Văn Sỹ, Phường 13, Quận Phú Nhuận, TP Hồ Chí Minh"
Khu vực TP Hồ Chí Minh,Hồ Chí Minh 2,CN. Nguyễn Đình Chiểu,Trụ sở,TP Hồ Chí Minh,Quận 3,"Số 569 Nguyễn Đình Chiểu, Phường 2, Quận 3, TP Hồ Chí Minh"
Khu vực TP Hồ Chí Minh,Hồ Chí Minh 2,CN. Phú Nhuận,Trụ sở,TP Hồ Chí Minh,Quận Phú Nhuận,"Một phần tầng Trệt tòa nhà Prince Residence, số 19 - 21 đường Nguyễn Văn Trỗi, Phường 12, Quận Phú Nhuận, TP Hồ Chí Minh"
Khu vực TP Hồ Chí Minh,Hồ Chí Minh 2,CN. Quận 10,Trụ sở,TP Hồ Chí Minh,Quận 10,"Tầng trệt, tầng 1 tầng 2 số 327-329 Tô Hiến Thành, Phường 13, Quận 10, TP Hồ Chí Minh"
Khu vực TP Hồ Chí Minh,Hồ Chí Minh 2,CN. Quận 12,Trụ sở,TP Hồ Chí Minh,Quận 12,"Số 312 đường Nguyễn Ảnh Thủ, khu phố 3, phường Hiệp Thành, Quận 12, TP Hồ Chí Minh"
Khu vực TP Hồ Chí Minh,Hồ Chí Minh 2,CN. Quang Trung,Trụ sở,TP Hồ Chí Minh,Quận Gò Vấp,"Số 170 Quang Trung, Phường 10, Quận Gò Vấp, TP Hồ Chí Minh"
Khu vực TP Hồ Chí Minh,Hồ Chí Minh 2,CN. Tân Định,Trụ sở,TP Hồ Chí Minh,Quận 1,"192 đường Trần Quang Khải, Phường Tân Định, Quận 1, TP Hồ Chí Minh"
Khu vực TP Hồ Chí Minh,Hồ Chí Minh 2,CN. Tân Hương,Trụ sở,TP Hồ Chí Minh,Quận Tân phú,"Số 229 đường Tân Hương, Phường Tân Quý, Quận Tân phú, TP Hồ Chí Minh"
Khu vực TP Hồ Chí Minh,Hồ Chí Minh 2,CN. Tân Phú,Trụ sở,TP Hồ Chí Minh,Quận Tân phú,"Số 835 – 837 đường Lũy Bán Bích, Phường Tân Thành, Quận Tân phú, TP Hồ Chí Minh"
Khu vực TP Hồ Chí Minh,Hồ Chí Minh 2,CN. Tân Sơn Nhất,Trụ sở,TP Hồ Chí Minh,Quận Phú Nhuận,"Một phần tầng 1 tòa nhà Garden Gate, số 08 Hoàng Minh Giám, Phường 9, Quận Phú Nhuận, TP Hồ Chí Minh"
Khu vực TP Hồ Chí Minh,Hồ Chí Minh 2,CN. Tây Sài Gòn,Trụ sở,TP Hồ Chí Minh,Huyện Hóc Môn,"Số 246 đường Tô Ký, ấp Tam Đông 1 - Xã Thới Tam Thôn - Huyện Hóc Môn - TP Hồ Chí Minh"
Khu vực TP Hồ Chí Minh,Hồ Chí Minh 2,CN. Tây Sài Gòn,Phòng giao dịch Lý Thường Kiệt,TP Hồ Chí Minh,Huyện Hóc Môn,Số 27/2B đường Lý Thường Kiệt - Thị Trấn Hóc Môn - Huyện Hóc Môn - TP Hồ Chí Minh
Khu vực TP Hồ Chí Minh,Hồ Chí Minh 2,CN. Tây Sài Gòn,Phòng giao dịch Bà Điểm,TP Hồ Chí Minh,Huyện Hóc Môn,"Số 10/2A đường Nguyễn Ảnh Thủ, ấp Hưng Lân - Xã Bà Điểm - Huyện Hóc Môn - TP Hồ Chí Minh"
Khu vực TP Hồ Chí Minh,Hồ Chí Minh 2,CN. Thống Nhất,Trụ sở,TP Hồ Chí Minh,Quận Tân Bình,"Tầng trệt, tầng lửng, tầng 2 số 102-104-106 Bàu Cát, Phường 14, Quận Tân Bình, TP Hồ Chí Minh"
Khu vực TP Hồ Chí Minh,Hồ Chí Minh 2,CN. Trường Chinh,Trụ sở,TP Hồ Chí Minh,Quận 12,"318 Trường Chinh, khu phố 6, Phường Tân Hưng Thuận, Quận 12, TP Hồ Chí Minh"
"""