cpu_price_usd = float(input())
video_price_usd = float(input())
ram_price_usd = float(input())
ram_quantity = int(input())
discount = float(input())

cpu_price_bgn = cpu_price_usd * 1.57
video_price_bgn = video_price_usd * 1.57
ram_price_bgn = ram_price_usd * 1.57
discount = discount * 100

needed_bgn = ram_price_bgn * ram_quantity + cpu_price_bgn * ((100 - discount) / 100) + video_price_bgn * ((100 - discount) / 100)
print(f"Money needed - {needed_bgn:.2f} leva.")
