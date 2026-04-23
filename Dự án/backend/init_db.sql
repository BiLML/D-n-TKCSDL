-- ============================================================
-- Database Schema: Hệ thống Quản lý Đào tạo
-- Dựa trên Mô hình quan hệ (ER Diagram)
-- DBMS: PostgreSQL 15
-- ============================================================

-- 1. Bảng Môn Học
CREATE TABLE IF NOT EXISTS mon_hoc (
    ma_mon      VARCHAR(20)     PRIMARY KEY,
    ten_mon_hoc VARCHAR(100)    NOT NULL,
    so_tin_chi  INTEGER         NOT NULL CHECK (so_tin_chi > 0)
);

COMMENT ON TABLE  mon_hoc             IS 'Bảng lưu thông tin các môn học';
COMMENT ON COLUMN mon_hoc.ma_mon      IS 'Mã môn học (khóa chính)';
COMMENT ON COLUMN mon_hoc.ten_mon_hoc IS 'Tên môn học';
COMMENT ON COLUMN mon_hoc.so_tin_chi  IS 'Số tín chỉ';

-- 2. Bảng Giảng Viên
CREATE TABLE IF NOT EXISTS giang_vien (
    ma_gv   VARCHAR(20)     PRIMARY KEY,
    ten_gv  VARCHAR(100)    NOT NULL,
    khoa    VARCHAR(100),
    email   VARCHAR(150)    UNIQUE,
    sdt     VARCHAR(15)
);

COMMENT ON TABLE  giang_vien          IS 'Bảng lưu thông tin giảng viên';
COMMENT ON COLUMN giang_vien.ma_gv    IS 'Mã giảng viên (khóa chính)';
COMMENT ON COLUMN giang_vien.ten_gv   IS 'Tên giảng viên';
COMMENT ON COLUMN giang_vien.khoa     IS 'Khoa';
COMMENT ON COLUMN giang_vien.email    IS 'Email';
COMMENT ON COLUMN giang_vien.sdt      IS 'Số điện thoại';

-- 3. Bảng Sinh Viên
CREATE TABLE IF NOT EXISTS sinh_vien (
    ma_sv       VARCHAR(20)     PRIMARY KEY,
    ten_sv      VARCHAR(100)    NOT NULL,
    ngay_sinh   DATE,
    gioi_tinh   VARCHAR(10),
    dia_chi     VARCHAR(255),
    email       VARCHAR(150)    UNIQUE,
    sdt         VARCHAR(15),
    nganh_hoc   VARCHAR(100),
    khoa        VARCHAR(100)
);

COMMENT ON TABLE  sinh_vien              IS 'Bảng lưu thông tin sinh viên';
COMMENT ON COLUMN sinh_vien.ma_sv        IS 'Mã sinh viên (khóa chính)';
COMMENT ON COLUMN sinh_vien.ten_sv       IS 'Tên sinh viên';
COMMENT ON COLUMN sinh_vien.ngay_sinh    IS 'Ngày sinh';
COMMENT ON COLUMN sinh_vien.gioi_tinh    IS 'Giới tính';
COMMENT ON COLUMN sinh_vien.dia_chi      IS 'Địa chỉ';
COMMENT ON COLUMN sinh_vien.email        IS 'Email';
COMMENT ON COLUMN sinh_vien.sdt          IS 'Số điện thoại';
COMMENT ON COLUMN sinh_vien.nganh_hoc    IS 'Ngành học';
COMMENT ON COLUMN sinh_vien.khoa         IS 'Khoa';

-- 4. Bảng Lớp Học Phần
CREATE TABLE IF NOT EXISTS lop_hp (
    ma_lop          VARCHAR(20)     PRIMARY KEY,
    ma_mon_hoc      VARCHAR(20)     NOT NULL REFERENCES mon_hoc(ma_mon) ON DELETE CASCADE,
    ma_gv           VARCHAR(20)     REFERENCES giang_vien(ma_gv) ON DELETE SET NULL,
    thoi_gian_hoc   VARCHAR(100),
    dia_diem_hoc    VARCHAR(200)
);

COMMENT ON TABLE  lop_hp                  IS 'Bảng lưu thông tin lớp học phần';
COMMENT ON COLUMN lop_hp.ma_lop           IS 'Mã lớp học phần (khóa chính)';
COMMENT ON COLUMN lop_hp.ma_mon_hoc       IS 'Mã môn học (khóa ngoại)';
COMMENT ON COLUMN lop_hp.ma_gv            IS 'Mã giảng viên phụ trách (khóa ngoại)';
COMMENT ON COLUMN lop_hp.thoi_gian_hoc    IS 'Thời gian học';
COMMENT ON COLUMN lop_hp.dia_diem_hoc     IS 'Địa điểm học';

-- 5. Bảng Kết Quả Học Tập (Bảng trung gian: SinhVien ↔ LopHP)
CREATE TABLE IF NOT EXISTS kqht (
    ma_sv       VARCHAR(20)     NOT NULL REFERENCES sinh_vien(ma_sv) ON DELETE CASCADE,
    ma_lop      VARCHAR(20)     NOT NULL REFERENCES lop_hp(ma_lop) ON DELETE CASCADE,
    diem_so     FLOAT,
    CONSTRAINT pk_kqht PRIMARY KEY (ma_sv, ma_lop)
);

COMMENT ON TABLE  kqht           IS 'Bảng kết quả học tập – quan hệ N-N giữa SinhVien và LopHP';
COMMENT ON COLUMN kqht.ma_sv     IS 'Mã sinh viên (khóa ngoại, phần của khóa chính)';
COMMENT ON COLUMN kqht.ma_lop    IS 'Mã lớp học phần (khóa ngoại, phần của khóa chính)';
COMMENT ON COLUMN kqht.diem_so   IS 'Điểm số';

-- 6. Bảng Giảng Dạy (Bảng trung gian: GiangVien ↔ MonHoc)
CREATE TABLE IF NOT EXISTS giang_day (
    ma_gv       VARCHAR(20)     NOT NULL REFERENCES giang_vien(ma_gv) ON DELETE CASCADE,
    ma_mon      VARCHAR(20)     NOT NULL REFERENCES mon_hoc(ma_mon) ON DELETE CASCADE,
    CONSTRAINT pk_giang_day PRIMARY KEY (ma_gv, ma_mon)
);

COMMENT ON TABLE  giang_day          IS 'Bảng trung gian giảng dạy – quan hệ N-N giữa GiangVien và MonHoc';
COMMENT ON COLUMN giang_day.ma_gv    IS 'Mã giảng viên (khóa ngoại, phần của khóa chính)';
COMMENT ON COLUMN giang_day.ma_mon   IS 'Mã môn học (khóa ngoại, phần của khóa chính)';

-- ============================================================
-- Indexes (tối ưu truy vấn)
-- ============================================================
CREATE INDEX IF NOT EXISTS idx_lop_hp_ma_mon  ON lop_hp(ma_mon_hoc);
CREATE INDEX IF NOT EXISTS idx_lop_hp_ma_gv   ON lop_hp(ma_gv);
CREATE INDEX IF NOT EXISTS idx_kqht_ma_sv     ON kqht(ma_sv);
CREATE INDEX IF NOT EXISTS idx_kqht_ma_lop    ON kqht(ma_lop);

-- ============================================================
-- Sample Data (Dữ liệu mẫu)
-- ============================================================

-- Môn học
INSERT INTO mon_hoc (ma_mon, ten_mon_hoc, so_tin_chi) VALUES
    ('MH001', 'Thiết kế Cơ sở dữ liệu', 3),
    ('MH002', 'Lập trình Web', 4),
    ('MH003', 'Cấu trúc dữ liệu và Giải thuật', 3),
    ('MH004', 'Mạng máy tính', 3),
    ('MH005', 'Trí tuệ nhân tạo', 3)
ON CONFLICT DO NOTHING;

-- Giảng viên
INSERT INTO giang_vien (ma_gv, ten_gv, khoa, email, sdt) VALUES
    ('GV001', 'Nguyễn Văn An',  'Công nghệ Thông tin', 'an.nv@university.edu.vn',  '0901000001'),
    ('GV002', 'Trần Thị Bình',  'Công nghệ Thông tin', 'binh.tt@university.edu.vn', '0901000002'),
    ('GV003', 'Lê Hoàng Cường', 'Khoa học Máy tính',   'cuong.lh@university.edu.vn','0901000003')
ON CONFLICT DO NOTHING;

-- Sinh viên
INSERT INTO sinh_vien (ma_sv, ten_sv, ngay_sinh, gioi_tinh, dia_chi, email, sdt, nganh_hoc, khoa) VALUES
    ('SV001', 'Phạm Minh Đức',  '2004-03-15', 'Nam',  'Hà Nội',      'duc.pm@student.edu.vn',  '0912000001', 'CNTT', 'Công nghệ Thông tin'),
    ('SV002', 'Ngô Thị Hương',  '2004-07-22', 'Nữ',   'TP.HCM',      'huong.nt@student.edu.vn','0912000002', 'CNTT', 'Công nghệ Thông tin'),
    ('SV003', 'Vũ Quốc Khánh',  '2003-11-10', 'Nam',  'Đà Nẵng',     'khanh.vq@student.edu.vn','0912000003', 'KHMT', 'Khoa học Máy tính'),
    ('SV004', 'Đỗ Lan Phương',  '2004-01-05', 'Nữ',   'Hải Phòng',   'phuong.dl@student.edu.vn','0912000004','CNTT', 'Công nghệ Thông tin'),
    ('SV005', 'Bùi Thanh Sơn',  '2003-09-28', 'Nam',  'Cần Thơ',     'son.bt@student.edu.vn',  '0912000005', 'KHMT', 'Khoa học Máy tính')
ON CONFLICT DO NOTHING;

-- Lớp học phần
INSERT INTO lop_hp (ma_lop, ma_mon_hoc, ma_gv, thoi_gian_hoc, dia_diem_hoc) VALUES
    ('LOP001', 'MH001', 'GV001', 'Thứ 2, 7:30-9:30',   'Phòng A101'),
    ('LOP002', 'MH002', 'GV002', 'Thứ 4, 13:00-15:00',  'Phòng B203'),
    ('LOP003', 'MH003', 'GV003', 'Thứ 6, 9:30-11:30',   'Phòng A305'),
    ('LOP004', 'MH001', 'GV002', 'Thứ 3, 15:00-17:00',  'Phòng C102'),
    ('LOP005', 'MH005', 'GV001', 'Thứ 5, 7:30-9:30',    'Phòng B101')
ON CONFLICT DO NOTHING;

-- Kết quả học tập
INSERT INTO kqht (ma_sv, ma_lop, diem_so) VALUES
    ('SV001', 'LOP001', 8.5),
    ('SV001', 'LOP002', 7.0),
    ('SV002', 'LOP001', 9.0),
    ('SV002', 'LOP003', 8.0),
    ('SV003', 'LOP003', 6.5),
    ('SV003', 'LOP005', 7.5),
    ('SV004', 'LOP002', 9.5),
    ('SV004', 'LOP004', 8.0),
    ('SV005', 'LOP005', 7.0),
    ('SV005', 'LOP001', 8.5)
ON CONFLICT DO NOTHING;

-- Giảng dạy (GiangVien ↔ MonHoc)
INSERT INTO giang_day (ma_gv, ma_mon) VALUES
    ('GV001', 'MH001'),
    ('GV001', 'MH005'),
    ('GV002', 'MH001'),
    ('GV002', 'MH002'),
    ('GV003', 'MH003'),
    ('GV003', 'MH004')
ON CONFLICT DO NOTHING;
