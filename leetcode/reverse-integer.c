// https://leetcode.com/problems/reverse-integer

int reverse(int32_t x) {
    if (x == -0b10000000000000000000000000000000) {
        return 0;
    }

    int64_t y = 0;

    short int isNegative = x < 0;

    if (isNegative) {
        x = -x;
    }

    while (x > 0) {
        y *= 10;
        y += x % 10;
        x /= 10;
    }

    if (y >= 0b10000000000000000000000000000000) {
        return 0;
    }

    if (isNegative) {
        y = -y;
    }

    return y;
}
