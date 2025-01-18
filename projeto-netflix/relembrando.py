import random
caracteres = "AdChEyDanBcPpXvRtyszxoqw#@"
password = ''.join(random.choice(caracteres) for _ in range(8))
print("password generated:", password)
