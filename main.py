import os

nombreTrabajador = input("Ingrese nombre del trabajador: ")
sueldoBasico = float (input('Ingrese el valor del sueldo basico: '))
diasFalta = float (input('Ingrese los dias de falta: '))
minutosTardanza = float (input('Ingrese los minutos de tardanza: '))
horasExtras = float (input('Ingrese las horas extras: '))
Movilidad = 1000
bonificacionSuplementaria = 0.03*sueldoBasico
pagoHorasExtra = 1.5*horasExtras*(sueldoBasico/240)
bonificaciones = Movilidad + bonificacionSuplementaria + pagoHorasExtra
remuneracionComputable = sueldoBasico + Movilidad + bonificacionSuplementaria
remuneracionMinima = sueldoBasico + bonificaciones
DescuentoFaltas = (remuneracionComputable/30)*diasFalta
DescuentoTardanzas = (remuneracionComputable/14400)*minutosTardanza
descuentos = DescuentoFaltas+DescuentoTardanzas
sueldoNeto = sueldoBasico + bonificaciones-descuentos

os.system ('pause')

print('                         Boleta de pago de '+ nombreTrabajador)
print('El sueldo basico es:                   +' + repr (sueldoBasico))
print('La bonificacion suplementario es:      +' + repr (bonificacionSuplementaria))
print('La bonificacion por movilidad es:      +' + repr (Movilidad))
HorasExtra = round(pagoHorasExtra, 2)
print('El pago por horas extras es:           +' + repr (HorasExtra))
Faltas = round(DescuentoFaltas, 2)
print('Los descuentos por faltas son:         -' + repr (Faltas))
Tardanzas = round(DescuentoTardanzas, 2)
print('Los descuentos por tardanzas son:      -' + repr (Tardanzas))
Sueldo = round(sueldoNeto, 2)
print('El sueldo neto es:                     =' + repr (Sueldo))