MESES = 20

importe = 10

total_pagado = 0

for i in range(MESES):

    print(f"Tasa a pagar por mes {i + 1} = ", importe)

    total_pagado += importe

    importe *= 2

print(f"total pagado por {MESES} meses = {total_pagado}")