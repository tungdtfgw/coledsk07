from toan import tong, can, binhphuong

a = int(input("Nhap so a: "))
b = int(input("Nhap so b: "))

print(f'{a} + {b} = {tong(a, b)}')
print(f'Can bac hai cua {a} la: {can(a)}')
print(f'Binh phuong cua {b} la: {binhphuong(b)}')