from database import engine
from model import Base

def main():
    Base.metadata.create_all(bind=engine)
    print("Tạo bảng thành công!")

if __name__ == "__main__":
    main()