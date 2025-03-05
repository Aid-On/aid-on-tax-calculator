import math
import argparse

# 税込→税抜を誤差なく計算する関数
def inclusive_to_exclusive(tax_inclusive_price, tax_rate=0.1):
    tax_exclusive = math.floor(tax_inclusive_price / (1 + tax_rate))
    recalculated_tax_inclusive = math.floor(tax_exclusive * (1 + tax_rate))

    if recalculated_tax_inclusive < tax_inclusive_price:
        tax_exclusive += 1

    tax_amount = tax_inclusive_price - tax_exclusive

    return tax_exclusive, tax_amount, tax_inclusive_price

# 税抜→税込計算関数
def exclusive_to_inclusive(tax_exclusive_price, tax_rate=0.1):
    tax_amount = math.floor(tax_exclusive_price * tax_rate)
    tax_inclusive_price = tax_exclusive_price + tax_amount

    return tax_exclusive_price, tax_amount, tax_inclusive_price


def main():
    parser = argparse.ArgumentParser(description="税抜⇔税込 計算ツール")
    parser.add_argument("mode", choices=["1", "2"], help="1: 税込→税抜, 2: 税抜→税込")
    parser.add_argument("price", help="金額（カンマ入力可）")

    args = parser.parse_args()

    mode = args.mode
    price = int(args.price.replace(",", ""))

    if mode == "1":
        tax_exclusive, tax_amount, tax_inclusive = inclusive_to_exclusive(price)
    else:
        tax_exclusive, tax_amount, tax_inclusive = exclusive_to_inclusive(price)

    print(f"税抜価格: ¥{tax_exclusive:,} ({tax_exclusive})")
    print(f"消費税額: ¥{tax_amount:,} ({tax_amount})")
    print(f"税込価格: ¥{tax_inclusive:,} ({tax_inclusive})")


if __name__ == '__main__':
    main()