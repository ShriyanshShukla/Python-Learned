for i in range(2,21):
    with open(f'Multiplication tables/Table_of_{i}', 'w') as f:
        for j in range(1,11):
            f.write(f"{i} x {j} = {i*j}")
            if j<10:
                f.write('\n')