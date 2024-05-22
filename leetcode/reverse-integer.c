int reverse(int x) {
    if (x == -2147483648) {
        return 0;
    }

    int y = 0;

    short int isNegative = x < 0;

    if (isNegative) {
        x = -x;
    }

    while (x > 0) {
        if (y > 214748364 || (y == 214748364 && x > 7)) {
            return 0;
        }

        y *= 10;
        y += x % 10;
        x /= 10;
    }

    if (isNegative) {
        y = -y;
    }

    return y;
}

int main() {
}
