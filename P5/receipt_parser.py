import re
import json

a = open("/storage/emulated/0/Download/raw.txt", "r", encoding="utf-8").read()
b = re.findall(r"\d+,\d{2}", a)
for i in range(len(b)):
	b[i] = re.sub(r"\s", "", b[i])
	b[i] = re.sub(",", ".", b[i])
	b[i] = float(b[i])
	
c = re.findall(r"\d+\.\n(.+)", a)

d = re.findall(r"x [\d]+,\d{2}\n([\d]+,\d{2})", a)
for i in range(len(d)):
	d[i] = re.sub(r"\s", "", d[i])
	d[i] = re.sub(",", ".", d[i])
	d[i] = float(d[i])

e = re.search(r"Время:\s(\d{2}\.\d{2}\.\d{4})\s(\d{2}:\d{2}:\d{2})", a)

f = re.search(r"(Банковская карта|Наличные)", a)

t = {
    "product_names": c,
    "all_prices": b,
    "calculated_total": sum(d),
    "date": e.group()[7:17],
    "time": e.group()[18:],
    "payment_method": f.group()
}
print(json.dumps(t, ensure_ascii=False, indent=2))