from libra.models import ModelFactory
from libra.types import ModelLabel

if __name__ == "__main__":
    
    tools = [
        {
            "type": "function",
            "function": {
                "name": "add",
                "description": "Add two numbers together. Use this when you need to perform addition.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "num1": {
                            "type": "number",
                            "description": "The first number to add."
                        },
                        "num2": {
                            "type": "number",
                            "description": "The second number to add."
                        }
                    },
                    "required": ["num1", "num2"],
                    "additionalProperties": False
                }
            }
        },
        {
            "type": "function",
            "function": {
                "name": "multiply",
                "description": "Multiply two numbers together. Use this when you need to perform multiplication.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "num1": {
                            "type": "number",
                            "description": "The first number to multiply."
                        },
                        "num2": {
                            "type": "number",
                            "description": "The second number to multiply."
                        }
                    },
                    "required": ["num1", "num2"],
                    "additionalProperties": False
                }
            }
        }
    ]
    
    from dotenv import load_dotenv
    
    load_dotenv(override=True)
    
    from libra.models.model_factory import ModelFactory
    from libra.config import ChatGPTConfig
    
    model = ModelFactory.create(
        model_label=ModelLabel.GPT_4o,
        model_config_dict=ChatGPTConfig(stream=True, temperature=0.0).__dict__,
    )
    
    
    document = f"""Topic: Thông điệp của Tổng Giám đốc MB
Content: Năm 2024, MB tiếp tục kiên định với tầm nhìn đến năm 2026 “Trở thành Doanh nghiệp số, Tập đoàn tài chính dẫn đầu” cùng mục tiêu chiến lược nằm trong “Top 3 thị trường về hiệu quả, hướng đến Top đầu châu Á.” Chiến lược của MB được xây dựng trên cơ sở Tập trung vào trải nghiệm của khách hàng; Sáng tạo ra các giá trị mới phục vụ khách hàng từ đó gia tăng giá trị cho MB. Xuyên suốt theo đó là một văn hóa quản trị thống nhất, lấy triết lý “Khách hàng là trung tâm” dựa trên các yếu tố: (1) Hấp dẫn khách hàng: Xây dựng trải nghiệm xuất sắc - Xuất phát từ nhu cầu và vươn tới kỳ vọng của khách hàng. (2) Linh hoạt, nhanh nhạy: Đón bắt nhanh - Tận dụng triệt để - Khai thác hiệu quả công nghệ, thị trường, nhu cầu khách hàng. (3) Hiệp lực tập đoàn: Toàn Tập đoàn kết nối, xây dựng trải nghiệm số One ID; đề xuất giá trị tập đoàn xuất sắc.

 Trong bối cảnh nền kinh tế toàn cầu năm 2023 đối mặt với 
những thách thức không nhỏ từ sự suy giảm kinh tế toàn 
cầu, Ngân hàng TMCP Quân Đội (MB) không chỉ vững vàng 
vượt qua khó khăn mà còn tạo ra những đột phá trong chiến 
lược chuyển đổi số – thể hiện qua cú nhảy vọt về quy mô 
khách hàng, lũy kế đến năm 2023 đạt 26,5 triệu khách hàng, 
tăng gấp 8 lần so với năm 2017 và là ngân hàng có số lượng 
khách hàng lớn nhất Việt Nam.
 Đến cuối năm 2023, tổng tài sản MB tăng 29% đạt xấp xỉ 950 
nghìn tỷ đồng; tín dụng tăng hơn 28,8% đạt 615 nghìn tỷ dư 
nợ cho vay đối với nền kinh tế; lợi nhuận toàn tập đoàn đạt 
hơn 26 nghìn tỷ đồng. 
MB là ngân hàng top đầu về việc cung cấp dịch vụ và sản 
phẩm đa dạng, an toàn; sở hữu hạ tầng công nghệ thông 
tin hiện đại; mở rộng mạnh mẽ các phân khúc thị trường 
mới bên cạnh thị trường truyền thống của một ngân hàng 
thương mại. Với lợi thế đó, MB đã kết nối dịch vụ BaaS 
đến doanh nghiệp từ đa dạng các lĩnh vực như: Tài chính, 
logistics, chứng khoán… thông qua hơn 600 bộ APIs - một 
trong những ngân hàng sở hữu lượng API đa dạng nhất. 
Chúng tôi kỳ vọng dịch vụ BaaS của MB sẽ từng bước chuyển 
mình mạnh mẽ, khẳng định cam kết đồng hành cùng doanh 
nghiệp trong quá trình chuyển đổi số.
 Bên cạnh đó, đội ngũ MB đã tập trung xây dựng và phát triển 
Chợ ứng dụng Mini App (MB Market Place) với mục tiêu góp 
phần chuyển đổi App MBBank thành một nền tảng siêu ứng 
dụng, tích hợp nhiều dịch vụ non-bank (phi ngân hàng) trên 
một nền tảng để phục vụ các nhu cầu khác nhau hàng ngày 
của hơn 20 triệu người dùng. 
Trong bối cảnh chuyển đổi số hóa mạnh mẽ, MB không chỉ 
đặt mục tiêu tăng trưởng kinh doanh mà còn chú trọng đến 
vai trò của doanh nghiệp đối với xã hội và môi trường. Đầu 
năm 2023, ngân hàng đã thể hiện cam kết mạnh mẽ đối với 
chiến lược ESG (Môi trường, Xã hội và Quản trị), tuân theo 
các chuẩn đo lường quốc tế, nhấn mạnh vào việc tạo ra tác 
động tích cực cho khách hàng và môi trường.
 Theo định hướng của Chính phủ và Ngân hàng Nhà nước, 
MB đã nghiên cứu và hoàn thiện cơ chế chính sách tín dụng 
gắn với quản lý môi trường - xã hội, hướng tới mục tiêu 
ngân hàng xanh, tín dụng xanh, cung cấp dịch vụ tín dụng 
và thanh toán trong các lĩnh vực thân thiện với môi trường. 
MB đã đạt được những bước tiến lớn trong việc phát triển 
tín dụng xanh, với tổng giá trị đạt 56,829 tỷ đồng, tăng 22% 
so với năm 2022. Điều này tập trung vào các lĩnh vực năng 
lượng sạch, tái tạo và công nghiệp, phản ánh rõ ràng sự 
chuyển hướng mạnh mẽ của ngân hàng đối với các hoạt 
động tài chính bền vững. MB cũng đã áp dụng số hoá trong 
90% hoạt động nội bộ, giảm bớt sự phụ thuộc vào giấy tờ 
và hướng tới một môi trường làm việc xanh, với mục tiêu đạt 
tỷ lệ 100%. 
Vào cuối năm 2023, MB đã phát động chiến dịch Hi-Green, 
chiến dịch trách nhiệm xã hội cộng hưởng thuộc chiến lược 
ESG của ngân hàng. HiGreen thu hút người tham gia vận 
động thể thao, ủng hộ trực tiếp và tích luỹ thiện nguyện 
thông minh. Theo đó, với mỗi km chạy bộ hoặc đi bộ hợp lệ, 
MB sẽ ủng hộ 3.000 VNĐ từ quỹ Từ thiện xã hội của tập đoàn 
tài trợ cho các đơn vị biến đổi các bãi rác tự phát thành 
không gian sinh thái cộng đồng, sân chơi công cộng. Sau 
khoảng 2 tháng, chiến dịch đã hoàn thành mục tiêu 8,1 tỷ để 
biến bãi rác tự phát thành sân chơi sinh thái cho cộng đồng. 
Với những bước phát triển mạnh mẽ và bền vững trong năm 
2023, uy tín thương hiệu của MB tiếp tục được khẳng định ở 
những bảng xếp hạng và giải thưởng uy tín trong và ngoài 
nước. MB là một trong 6 ngân hàng được tạp chí Forbes xếp 
hạng là 6 ngân hàng niêm yết tốt nhất Việt Nam trong 3 năm 
liền (2021-2023) dựa theo các tiêu chí về hiệu quả hoạt động 
và lợi nhuận. Bên cạnh đó, mô hình ngân hàng tự động MB 
SmartBank được nhận hai giải thưởng quốc tế từ The Asset 
Tripple A Award - Best Digital Branch Project và The Global 
Economics - Digital Transformation Bank of the Year – đây 
là minh chứng rõ nét cho những nỗ lực chuyển đổi số, đặt 
khách hàng làm trung tâm của MB. 
Năm 2024, MB tiếp tục kiên định với tầm nhìn đến năm 2026 
“Trở thành Doanh nghiệp số, Tập đoàn tài chính dẫn đầu” 
cùng mục tiêu chiến lược nằm trong “Top 3 thị trường về hiệu 
quả, hướng đến Top đầu châu Á.” 
Chiến lược của MB được xây dựng trên cơ sở Tập trung vào 
trải nghiệm của khách hàng; Sáng tạo ra các giá trị mới 
phục vụ khách hàng từ đó gia tăng giá trị cho MB. Xuyên 
suốt theo đó là một văn hóa quản trị thống nhất, lấy triết lý 
“Khách hàng là trung tâm” dựa trên các yếu tố:
 (1) Hấp dẫn khách hàng: Xây dựng trải nghiệm xuất sắc - 
Xuất phát từ nhu cầu và vươn tới kỳ vọng của khách hàng. 
(2) Linh hoạt, nhanh nhạy: Đón bắt nhanh - Tận dụng triệt để - Khai thác hiệu quả công nghệ, thị trường, nhu cầu khách hàng.
 (3) Hiệp lực tập đoàn: Toàn Tập đoàn kết nối, xây dựng trải 
nghiệm số One ID; đề xuất giá trị tập đoàn xuất sắc.
 Với mục tiêu phục vụ 30 triệu khách hàng vào năm 2024, lợi 
nhuận hợp nhất dự kiến đạt 30.000 tỷ và tổng tài sản đạt 1 
triệu tỷ, MB đang hướng tới việc không chỉ là ngân hàng dẫn 
đầu trong lĩnh vực số hóa mà còn là ngân hàng tiên phong 
trong việc phát triển bền vững và có trách nhiệm xã hội. MB, 
với những bước tiến mạnh mẽ và chiến lược đổi mới, đang 
khẳng định vị thế của mình trên thị trường tài chính và sẵn 
sàng đón nhận những cơ hội mới trong tương lai của ngành 
ngân hàng số.

Topic: Thông điệp của Chủ tịch Hội đồng Quản trị MB
Content: Năm 2024 là một năm đặc 
biệt khi MB đón chào tuổi 30 với những thử thách lớn hơn và giấc mơ lớn 
hơn với thông điệp Move for Big – Tiến bước vững vàng. Đồng thời, cũng 
là năm nhiệm kỳ mới HĐQT, BKS giai đoạn 2024 – 2029. Theo đó, MB đặt 
ra các mục tiêu cụ thể là: Top 3 ngân hàng về hiệu quả và an toàn, phấn đấu 
lợi nhuận trước thuế Tập đoàn đạt 30 nghìn tỷ đồng, chinh phục cột mốc 30 
triệu khách hàng. Ngân hàng MB sẽ triển khai nhiều chương trình, dự án 
hướng đến các nhóm đối tượng: Đất nước và Cộng đồng: Move for Big 
Vietnam – Tiến bước vì một Việt Nam hùng cường; CBNV: Move for Big 
Ambition - Tiến bước Diệu kỳ; Khách hàng: Move for Big Generation - 
Tiến bước Thành công. Đồng thời, MB sẽ tiếp tục hoàn thiện và triển khai 
mạnh mẽ, tối ưu các Sáng kiến Chiến lược thuộc Chiến lược tập đoàn giai 
đoạn 2022 - 2026, đẩy mạnh “Hiệp lực Tập đoàn”.  

Kính gửi Quý Cổ đông, Nhà đầu tư và Đối tác,
 Năm 2023 là một năm khó chung cho nền kinh tế thế giới, 
với sự giảm sút mạnh về tăng trưởng GDP, thương mại và 
đầu tư toàn cầu; trong khi nợ xấu tăng, lạm phát vẫn duy trì 
ở mức cao. Kinh tế Việt Nam bị ảnh hưởng bởi tình hình kinh 
tế thế giới; tuy nhiên với các xu hướng tích cực trong các 
tháng cuối năm 2023 đã giúp tăng trưởng kinh tế nước ta 
cả năm đạt mức ~5,05%, tăng trưởng khá cao so với nhiều 
nước trên thế giới và khu vực. Lạm phát được kiểm soát, CPI 
bình quân ước tăng ~3,5%. Sức hấp thụ vốn và cầu tín dụng 
toàn hệ thống ~13,5%, so với chỉ tiêu định hướng đầu năm 
~14%; tăng trưởng huy động vốn ~10,85%, thanh khoản nền 
kinh tế gặp khó khăn cục bộ tại khu vực bất động sản, thị 
trường trái phiếu doanh nghiệp. Nhiều chủ trương và chính 
sách mới của Đảng, Nhà nước tiếp tục được triển khai sâu 
rộng, NHNN điều hành chủ động linh hoạt để ổn định kinh tế 
vĩ mô, hỗ trợ phục hồi tăng trưởng kinh tế. 
Năm 2023 đánh dấu sự chuyển giao thế hệ của MB. Theo đó, 
được sự tin tưởng của Quân ủy trung ương, Bộ Quốc phòng, 
Hội đồng Quản trị (HĐQT) và người tiền nhiệm - Nguyên 
Thứ trưởng BQP - Thượng tướng Lê Hữu Đức, tôi đã được 
giao trọng trách giữ chức Chủ tịch HĐQT; Thượng tá Phạm 
Như Ánh được giao nhiệm vụ giữ chức Tổng Giám đốc MB. 
Kế thừa và tiếp nối các giá trị của thế hệ lãnh đạo đi trước, 
MB tiếp tục 01 mục tiêu chiến lược “Trở thành Doanh nghiệp 
số - Tập đoàn Tài chính dẫn đầu”, 06 giá trị cốt lõi, 08 định 
hướng chiến lược và 08 phương pháp làm việc khoa học với 
kỳ vọng đưa MB trở thành tổ chức phát triển bền vững, là tổ 
chức mang lại giá trị cho khách hàng, mang lại hạnh phúc 
cho CBNV. Với sự đoàn kết, đồng lòng trong quản trị - điều 
hành của Hội đồng Quản trị, Ban Kiểm soát, Ban Điều hành, 
Tập đoàn MB đã từng bước hiện thực hóa Chiến lược Phát 
triển giai đoạn 2022 – 2026 với những dấu ấn: Lợi nhuận 
trước thuế (LNTT) Tập đoàn đạt 26.306 tỷ đồng; LNTT riêng 
Ngân hàng ước đạt 24.688 tỷ đồng; LNTT các công ty thành 
viên đạt 2.046 tỷ đồng. Duy trì vị thế Top đầu các chỉ tiêu 
hiệu quả như ROE ~25%. Trích lập dự phòng đầy đủ và đảm 
bảo quy định pháp luật. Vị thế và uy tín của ngân hàng ngày 
càng nâng cao. MB đứng đầu về tăng trưởng quy mô, Top 3 
về Lợi nhuận trước thuế trong các ngân hàng thương mại; 
MB thu hút thêm 6,2 triệu khách hàng mới (lũy kế quy mô 
khách hàng đạt trên 26,5 triệu) với tỷ lệ giao dịch trên kênh 
số đạt trên 96,7%. 
Bên cạnh hoàn thành xuất sắc kế hoạch kinh doanh, HĐQT 
đã triển khai hiệu quả các quyết nghị của ĐHĐCĐ năm 2023 
giao phó, thực hiện đầy đủ các quyền của cổ đông theo quy 
định của pháp luật. 
MB đã đóng góp tích cực cho Ngân sách nhà nước với tổng 
số tiền ~7.518 tỷ đồng, thực hiện công tác an sinh xã hội, đền 
ơn đáp nghĩa với hơn 100 chương trình, tổng kinh phí thực 
hiện là ~200 tỷ đồng. Phát động chiến dịch HiGreen - Bình 
Minh Xanh - chiến dịch “Trách nhiệm xã hội cộng hưởng 
(Participatory CSR)”, nhằm truyền tải thông điệp sống bền 
vững, quan tâm tới môi trường và cộng đồng đến khách 
hàng và xã hội. 
Năm 2024 là một năm đặc biệt khi MB đón chào tuổi 30 với 
những thử thách lớn hơn và giấc mơ lớn hơn với thông điệp 
Move for Big – Tiến bước vững vàng. Đồng thời, cũng là năm 
nhiệm kỳ mới HĐQT, BKS giai đoạn 2024 – 2029. Theo đó, MB 
đặt ra các mục tiêu cụ thể là: Top 3 ngân hàng về hiệu quả 
và an toàn, phấn đấu lợi nhuận trước thuế Tập đoàn đạt 
30 nghìn tỷ đồng, chinh phục cột mốc 30 triệu khách hàng.  
Ngân hàng MB sẽ triển khai nhiều chương trình,  
dự án hướng đến các nhóm đối tượng: Đất nước và Cộng 
đồng: Move for Big Vietnam – Tiến bước vì một Việt Nam 
hùng cường; CBNV: Move for Big Ambition - Tiến bước 
Diệu kỳ; Khách hàng: Move for Big Generation - Tiến bước 
Thành công. Đồng thời, MB sẽ tiếp tục hoàn thiện và triển 
khai mạnh mẽ, tối ưu các Sáng kiến Chiến lược thuộc Chiến 
lược tập đoàn giai đoạn 2022 - 2026, đẩy mạnh “Hiệp lực 
Tập đoàn”.
 Tuy chặng đường phía trước còn nhiều khó khăn với các 
vấn đề nóng về biến đổi khí hậu, rủi ro địa chính trị, và các 
rủi ro chuyển đổi mới nổi khác, MB sẽ tiếp tục nghiên cứu 
và triển khai các giải pháp đóng góp gián tiếp cho lộ trình 
thực hiện cam kết đạt lượng phát thải ròng bằng 0 vào năm 
2050 của quốc gia. 

Topic: THÔNG ĐIỆP CỦA LÃNH ĐẠO VỀ PHÁT TRIỂN BỀN VỮNG
Content: - Năm 2023, nền kinh tế hậu Covid – 19 toàn cầu còn nhiều khó khăn, bên cạnh chiến tranh địa - chính trị chưa có hồi kết gây ra khủng hoảng năng lượng toàn cầu, hành tinh chúng ta phải chịu các tác động cực đoan do biến đổi khí hậu cộng hưởng với El Niño từ giữa mùa hè 2023 gây ra mức nhiệt cao kỷ lục, hay mưa lũ cực đoan ở nhiều vùng lãnh thổ trên thế giới. Hậu quả của El Niño 2023 được ước tính gây thiệt hại lên tới 3.000 tỷ USD đối với nền kinh tế toàn cầu, khiến GDP giảm tác động tiêu cực đến sản xuất nông nghiệp và công nghiệp, đặc biệt tại các quốc gia dễ bị tổn thương do khí hậu, trong đó có Việt Nam.
- Từ COP 26 cho tới COP 28, Chính phủ Việt Nam đã nâng mức cam kết giảm phát thải khí nhà kính (theo Đóng góp quốc gia tự quyết định - NDC 2022), quyết liệt triển khai các chương trình hành động về ứng phó với biến đổi khí hậu, chuyển đổi năng lượng và kêu gọi các quốc gia đoàn kết, nỗ lực, đẩy mạnh hợp tác, đầu tư có trách nhiệm cùng đưa phát thải ròng bằng ‘’0’’ vào năm 2050. Các tổ chức tài chính nói chung, và hệ thống ngân hàng nói riêng được xác định là kênh huy động và cung ứng nguồn lực tài chính chủ chốt nhằm thực thi các hành động tài chính về thích ứng, giảm thiểu tác động của biến đổi khí hậu, bên cạnh việc thúc đẩy các hoạt động phát triển bền vững và tăng trưởng xanh trong bối cảnh nền kinh tế hiện nay.
- Năm 2023 là năm thứ 2 trên chặng đường triển khai Chiến lược 2022 – 2026, sự chuyển giao nhân sự cấp cao đã mở ra chương mới cho MB trên hành trình chiến lược ‘’Trở thành doanh nghiệp số - Tập đoàn tài chính dẫn đầu’’, giữ vững quyết tâm theo đuổi, hoàn thành tốt những nhiệm vụ đã được phân giao, đóng góp tích cực vào mục tiêu phát triển bền vững khi đi đầu trong chuyển đổi số; tăng cường tín dụng xanh với tỷ trọng tín dụng xanh chiếm 11% tổng dư nợ, tăng trưởng qua các năm và gấp 3,8 lần so với 2020, bên cạnh việc không ngừng hoàn thiện bộ máy, nâng cao năng lực quản trị về ESG. Nhận thức biến đổi khí hậu là một vấn đề của thế giới hiện đại ngày nay, dưới định hướng, chỉ đạo từ Chủ tịch HĐQT, cùng sự đoàn kết, nỗ lực, quyết tâm cao, triển khai đồng bộ nhiều giải pháp của các đơn vị trên toàn hệ thống, MB giữ hoạt động kinh doanh an toàn, hiệu quả, tăng trưởng trên mọi mặt, đi đầu tài trợ lĩnh vực năng lượng xanh – năng lượng tái tạo trong ngành; hoạt động chuyển đổi số mạnh mẽ tạo ra các giá trị vượt trội cho khách hàng tiếp tục được đẩy mạnh, tạo đà tăng trưởng đột phá, khẳng định vị thế top đầu về tăng trưởng quy mô.
- Văn hóa doanh nghiệp bền vững với con người là nòng cốt tạo nền tảng cho tăng trưởng kinh doanh bền vững thúc đẩy MB nỗ lực thực hiện các chương trình nâng cao chất lượng nguồn lực, thu hút và giữ chân nhân tài; cùng với các công ty thành viên tích cực thực hiện kinh doanh có trách nhiệm, lan tỏa giá trị bền vững thông qua các chương trình CSR thiết thực cho xã hội và cộng đồng.
- Một năm nhìn lại, MB tự hào khẳng định vị thế của một định chế tài chính ‘’Bản lĩnh – vững vàng’’ – tạo đà cho một MB tăng tốc số, đón chào tuổi 30 nhiều kỳ vọng, bứt phá mới. Bước sang năm 2024, MB cùng các công ty thành viên sẽ tiếp tục nâng cao và hoàn thiện cấu trúc, mô hình quản trị bền vững, chủ động, sáng tạo, tăng cường gắn kết các bên liên quan tạo ra các sản phẩm, dịch vụ vượt trội hướng tới mục tiêu giảm phát thải, thúc đẩy phát triển bền vững.

Topic: HÀNH TRÌNH CHUYỂN ĐỔI SỐ VỚI KHÁCH HÀNG LÀ TRỌNG TÂM
Content: 1. Chiến lược phát triển ngân hàng số:
- Chiến lược:
Xây dựng mô hình ngân hàng số tự phục vụ (self-serving), năm 2023 MB tập trung mục tiêu đẩy mạnh giao dịch trên
kênh số lên 96,7%; phát triển sản phẩm dịch vụ đặc thù chỉ có trên kênh số 100% online.
APP MBBank hướng tới mục tiêu siêu ứng dụng tài chính mang tính cá nhân hóa (all-in-one App): MB tiên phong triển
khai nền tảng mini Apps trong lĩnh vực ngân hàng, nâng cao trải nghiệm khách hàng với mô hình Apps-in-App. Chỉ
bằng một vài thao tác đơn giản, người dùng APP MBBank có thể hoàn tất thao tác mua sắm online, di chuyển, đặt vé
máy bay, đặt khách sạn, ship hàng, mua voucher giải trí, ẩm thực,... cùng hệ thống thanh toán bảo mật hàng đầu tại
Việt Nam. Hiện tại số lượng Mini-Apps cung cấp cho khách hàng đã lên tới 154 mini Apps.
Năm 2024, MB dự kiến chinh phục 30 triệu khách hàng, mừng dấu ấn tròn 30 tuổi. MB sẽ tiếp tục tăng tốc số hấp dẫn
khách hàng, hiệp lực tập đoàn, an toàn bền vững, thực hiện ESG một cách bài bản. Thực hiện chuyển đổi App Flutter cá nhân hóa cho từng tệp khách hàng với nhiều tính năng thuận tiện. Tiếp tục đẩy mạnh mô hình kinh doanh BaaS tập trung vào mô hình cung cấp sản phẩm dịch vụ tài chính cho Khách hàng doanh nghiệp trên nền tảng của đối tác.
- Kết quả thực hiện 2023:
Tính đến hết 2023, MB ghi nhận 2,3 tỷ giao dịch trên kênh số với giá trị giao dịch đạt xấp xỉ 10 triệu tỷ đồng. Trong đó,
riêng APP MBBank ghi nhận 6 triệu giao dịch/ngày. Quy mô giao dịch trên nền tảng số duy trì ở mức cao 96,7%, tương
đương các ngân hàng TOP đầu châu Á. Đồng thời, MB là ngân hàng góp mặt trong TOP đầu ứng dụng sở hữu gần
12 triệu người dùng đang hoạt động tại Việt Nam.
- Các dự án Công nghệ năm 2023 giúp cải tiến hệ thống và nâng cao trải nghiệm khách hàng:
+ Sử dụng công nghệ Mini-App trên MyMB và tích hợp
eKYC, NFC hỗ trợ chuyên viên UB/RM định danh khách
hàng tại quầy, đơn giản thuận tiện và hạn chế rủi ro.
+ Xây mới ứng dụng MB Bank trên nền tảng Flutter,
chuyển đổi hơn 400 tính năng từ App cũ sang App
mới; tối ưu hóa trải nghiệm theo từng phân khúc khách
hàng; nâng cao bảo mật.
+ Xây dựng một hệ thống trung gian thanh toán, cho
phép hợp nhất cách thức giao tiếp truyền, nhận và
xử lý dữ liệu khác nhau trong cùng một nền tảng
trung tâm, giúp hoàn thiện hệ thống thanh toán nội
bộ, nâng cao tốc độ xử trong hệ thống.
+ Xây dựng hệ thống đối soát tập trung cho các sản
phẩm dịch vụ khách hàng.
+ Xây dựng nền tảng MBSM thay thế giải pháp PCSM
mua của hãng (nước ngoài).
+ Chuyển đổi toàn bộ quy trình tín dụng từ BPM new sang
BPM Smart.
+ Xây dựng hệ thống Moffice 2.0 APP và WEB trên nền
tảng Flutter; áp dụng chữ ký số MB và Cloud CA mang
đến cho người dùng trải nghiệm hiện đại và thuận tiện
hơn.
+ Hệ thống lãi phí tập trung tự phát triển phù hợp và linh
hoạt với chính sách của MB, giúp giảm thiểu rủi ro cho
hoạt động vận hành và phê duyệt.
+ Triển khai Active Active multisite giúp tăng tính sẵn
sàng, khả năng chịu tải và khả năng chống chịu lỗi đảm
bảo tính liên tục của hệ thống công nghệ thông tin cung
cấp dịch vụ cho Khách hàng ngay cả trong trường hợp
một site gặp vấn đề.
- Các chương trình hỗ trợ khách hàng chuyển đổi số tiêu biểu trong năm 2023:
+ MB Hi Collection:
Năm 2022, MB cho ra mắt thẻ MB Hi Collection là dòng thẻ đa năng giúp khách hàng cá nhân hóa nhu cầu sử dụng và thể hiện
phong cách riêng thông qua các mẫu thẻ bắt mắt, phù hợp với nhiều lứa tuổi gồm: ACE - bộ sưu tập với biểu tượng của những
lá bài Tây; Zodiac - bộ sưu tập lấy cảm hứng từ cung hoàng đạo; Summer Paradise - bộ sưu tập ngập tràn màu sắc của mùa hè.
Tiếp theo, các dòng thẻ chuyên biệt cũng gây ấn tượng mạnh với người dùng như thẻ Hi - Slaydy dành cho phái đẹp, Hi - Shopee Food với ưu đãi đặc biệt khi đặt đồ ăn online, Hi - LOL MasterCard cho các game thủ. Đặc biệt, thẻ Hi tích hợp thẻ membership fandom đầu tiên dành cho fan của ca sĩ Sơn Tùng - MTP “Be the sky” gây được tiếng vang lớn trong giới showbiz, dòng thẻ ESG sử dụng chất liệu thân thiện môi trường với thiết kế truyền cảm hứng khuyến khích lối sống xanh và bền vững, gắn hoạt động chi tiêu cá nhân với trách nhiệm với môi trường và xã hội. Tính đến nay tổng số lượng thẻ Hi bán ra trên thị trường là 2.333.611 thẻ.
+ Vòng thời trang thanh toán MB Stellar:
Năm 2023, MB tung ra sản phẩm vòng thời trang thanh toán MB Stellar với gần 20 kiểu dáng và màu sắc khác nhau. Vòng tay
tích hợp bên trong chip contactless, không có thông tin số thẻ hay tên chủ thẻ, đảm bảo an toàn, bảo mật tối đa cho khách hàng;
đồng thời sử dụng linh hoạt nguồn tiền từ tài khoản thanh toán và tùy chọn hạn mức tín dụng. Số lượng vòng tay Stellar đã bán là
1.922 chiếc.
+ Chuỗi thanh toán không dùng tiền mặt:
Golive 18 khách hàng doanh nghiệp lớn sử dụng các giải pháp thanh toán không dùng tiền mặt (thu hộ qua mã định danh, mã VA, VietQR)
- Phản hồi từ khách hàng đối với chuyển đổi số:
+ Kết quả phân tích về phản hồi của khách hàng trong hành trình trải nghiệm chuyển đổi số:
Các phương án tinh chỉnh hành trình trải nghiệm khách hàng được MB cập nhật liên tục thông qua các chỉ số chất
lượng được đo lường và khảo sát hàng ngày từ Khách hàng. Các chỉ số chất lượng dịch vụ được tham khảo để cải
tiến hành trình bao gồm:
► Chỉ số NPS – Chỉ số trung thành của khách hàng với MB
► Chỉ số CSAT – Chỉ số hài lòng khách hàng đối với chất lượng phục vụ của MB
► Chỉ số CES – Chỉ số đo mức độ thuận tiện của sản phẩm - dịch vụ đối với khách hàng MB
Sự tham vấn trực tiếp với các nhóm khách hàng trong quá trình thiết kế, phát triển sản phẩm:
Việc thiết kế, phát triển và nâng cấp luôn căn cứ tham vấn của Khách hàng, cụ thể:
► Với kênh điện thoại: căn cứ các chỉ số tiếp cận CES, chỉ số trung thành NPS và chỉ số hài lòng.
► Với kênh App: căn cứ vào tỉ lệ voting sau mỗi phiên hỗ trợ kết hợp các ý kiến riêng biệt khách hàng để lại góp ý
qua các kênh hỗ trợ khách hàng của MB247.
Tăng 4,3 Tăng 8,5 Tăng 12,8 điểm điểm điểm

Thực hiện thu thập ý kiến của khách hàng trong quá trình thử nghiệm sản phẩm/dịch vụ mới:
Mỗi một sản phẩm dịch vụ trước khi ra đời đều được chạy thử nghiệm trên 1 tập nhỏ nhằm đánh giá và tinh chỉnh
trước khi ứng dụng diện rộng trên toàn bộ khách hàng MB. Tỉ lệ đạt với các trải nghiệm và kịch bản thử nghiệm cần
vượt qua 80% mới đủ điều kiện ứng dụng trên toàn bộ khách hàng. Sau khi ứng dụng, công tác lắng nghe ý kiến
khách hàng và điều chỉnh thông qua các chỉ số vận hành cũng là yếu tố then chốt của dịch vụ.
Các kênh khảo sát được thực hiện bao gồm và không giới hạn:
► Phỏng vấn trực tiếp qua điện thoại.
► Khảo sát ý kiến qua email.
► Lắng nghe góp ý điều chỉnh qua các thông tin tại kênh MBChat, mạng xã hội fanpage MBBank, các góp ý để lại
trên chợ ứng dụng cũng như các nền tảng xã hội có đề cập thông tin đến MB.
Một số dự án tiêu biểu trong năm nhận được mức độ hài lòng cao của khách hàng:
► Dự án chatbot: triển khai ứng dụng hỗ trợ khách hàng qua kênh chatbot.
► Dự án tổng đài thông minh smart IVR: triển khai ứng dụng điều hướng cuộc gọi qua giọng nói.
► Dự án Voice Brandname: hiển thị thông tin thương hiệu MB khi gọi đến khách hàng. Gia tăng yếu tố tin cậy và
giảm thiểu rủi ro mạo danh MB liên hệ tới khách hàng.
► Dự án các kênh tra soát tự động gửi và tiếp nhận: tạo thêm kênh tiếp nhận và chủ động theo dõi tra soát cho
khách hàng của MB.
+ Đảm bảo an toàn thông tin khách hàng: Định hướng chung về đảm bảo an toàn thông tin khách hàng MB
Với tư duy khách hàng là trọng tâm trong giai đoạn chuyển đổi số mạnh mẽ, việc đảm bảo an toàn thông tin cho khách
hàng được tiếp cận theo các khía cạnh Con người – Quy trình – Công nghệ.
Các hoạt động triển khai trong năm 2023 tập trung vào 03 nhóm khía cạnh về Con người – Quy trình – Công nghệ, là cơ
sở đưa ra các kế hoạch đảm bảo các mục tiêu sau: Con người: Triển khai đào tạo nhân thức An toàn
thông tin CBNV MB, Truyền thông, đào tạo nhận thức khách hàng về các rủi ro An toàn thông tin;  Quy trình: Cải tiến tính chi tiết, chặt chẽ và hiệu quả của các quy trình hiện tại, Tuân thủ quy trình quy định An toàn thông tin, chủ động đánh giá an ninh, rà soát liên tục các dịch vụ số phục vụ khách hàng, giám sát, cập nhật các thông tin tình báo, các rủi ro nhắm vào khách hàng MB; Công nghệ: Nâng cao, tối ưu biện pháp xác thực, bảo vệ danh tính khách hàng MB, bao gồm người dùng nội bộ và khách hàng ngoài, tối ưu mô hình kiến trúc ATTT và làm chủ giải pháp hệ thống an toàn thông tin."""
    
    # Prepare the input messages
    messages = [
        {"role": "system", "content": f"Trả lời câu hỏi dựa theo tài liệu được cung cấp: {document}"},
        {"role": "user", "content": "Tổng giám đốc MB là ai ?"}
    ]

    # Run the model with the input messages
    # response = model.stream(messages=messages, tools=tools)
    response = model.run(messages=messages) # type: ignore
    
    import json
    
    if model.stream:
        for chunk in response: # type: ignore
            content = chunk.choices[0].delta.content
            if content:
                print(content, end='')
    else:
        print(response.choices[0].message.content) # type: ignore
    
    print()