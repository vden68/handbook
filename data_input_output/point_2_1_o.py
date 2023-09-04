p_n = int(input())
p_m = int(input())
p_t = int(input())

p_s_m = (p_t % 60 + p_m) % 60
p_s_n = (p_t // 60 + p_n + ((p_t % 60 + p_m) // 60)) % 24

print(f"{p_s_n:0>2}" + ":" + f"{p_s_m:0>2}")