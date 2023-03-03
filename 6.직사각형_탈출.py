x, y, w, h = input().split()

x = int(x)
y = int(y)
w = int(w)
h = int(h)

A = w - x;
B = h - y;

print(min(A, B, x, y))

# input은 문자열로 받으므로 int로 변환 필요
# split은 문자열로 쪼개므로 각각을 int로 변환 필요