p_n1 = int(input())
p_n2 = int(input())

p_n1_1 = p_n1 // 100
p_n1_2 = p_n1 // 10 - p_n1_1 * 10
p_n1_3 = p_n1 - p_n1_1 * 100 - p_n1_2 * 10

p_n2_1 = p_n2 // 100
p_n2_2 = p_n2 // 10 - p_n2_1 * 10
p_n2_3 = p_n2 - p_n2_1 * 100 - p_n2_2 * 10

p_z1 = (p_n1_1 + p_n2_1) % 10
p_z2 = (p_n1_2 + p_n2_2) % 10
p_z3 = (p_n1_3 + p_n2_3) % 10

print(p_z1 * 100 + p_z2 * 10 + p_z3)

