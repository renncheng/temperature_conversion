# Temperature Conversion 

ask_type = input ('Would you like to use 1.F to C or 2.C to F ?')
ask_type = int(ask_type)

if ask_type == 1:
	temper_input_F = input ('Please key in Temperature(F)')
	temper_input_F = float(temper_input_F)
	temper_input_C = (temper_input_F - 32)*5/9
	print ('The temperature is ', temper_input_C, 'C')
else:
	temper_input_C = input ('Please key in Temperature(C)')
	temper_input_C = float(temper_input_C)
	temper_input_F = temper_input_C *9/5 + 32
	print ('The temperature is ', temper_input_F, 'F')