def morganAndString(a, b):
    output = ''

    a += 'z'
    b += 'z'
    len_a = len(a)
    len_b = len(b)
    a_letters = len_a
    b_letters = len_b
    for _ in range(len_a + len_b - 2):
        if a <= b:
            output += a[0]
            a = a[1::]
            a_letters -= 1
        else:
            output += b[0]
            b = b[1::]
            b_letters -= 1

        if a_letters == 0:
            output += b
            break

        if b_letters == 0:
            output += a
            break

    return output


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr = open('output/output.txt', 'w')
    t = int(input())

    for t_itr in range(t):
        a = input()

        b = input()

        result = morganAndString(a, b)

        fptr.write(result + '\n')

    fptr.close()
