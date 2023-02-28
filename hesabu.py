from database import Hesabu

hesabu = Hesabu.select()
for hesabu in hesabu:
    print(hesabu.principal, hesabu.rate, hesabu.time)
