// https://leetcode.com/problems/reverse-integer

int reverse(int32_t x) {
    if (x == -0b10000000000000000000000000000000) {
        return 0;
    }

    short int isNegative = x < 0;

    if (isNegative) {
        x = -x;
    }

    uint64_t y = 0;

    while (x > 0) {
        y *= 10;
        y += x % 10;
        x /= 10;
    }

    if (y >= 0b01111111111111111111111111111111) {
        return 0;
    }

    return isNegative ? -y : y;
}
