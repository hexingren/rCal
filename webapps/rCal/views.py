# Create your views here.

from django.shortcuts import render
import operator

ops = {'+': operator.add,                            # operations
	   '-': operator.sub,
	   '*': operator.mul,
	   '/': operator.div,
	   }

def calculator(request):

    
	disp = '0'                                        # disp is the number displayed on the screen
	val = '0'                                         # val is the other stored operator
	op = ''                                           # op is the operation
	flg = '1'                                         # flg is an indicator that tells if last input is a num or an
	                                                  # operation
	errmsg = ''                                       # errmsg gives out the message
	pre = '0'                                         # if input in {+, -, *, /}, pre='1'


	if 'disp' in request.POST:
		disp = request.POST['disp']
	if 'val' in request.POST:
		val = request.POST['val']
	if 'op' in request.POST:
		op = request.POST['op']
	if 'flg' in request.POST:
		flg = request.POST['flg']
	if 'pre' in request.POST:
		pre = request.POST['pre']
		
	if 'opt' in request.POST:
		if pre == '1':                                 # malformed: {+, -, *, /} * {+, -, *, /, =}
			disp = '0'
			val = '0'
			op = ''
			flg = '1'
			errmsg = 'error: malformed input'
			pre = '0'
		
		else:
			flg = '1'
			optype = request.POST['opt']
			if optype != '=':
				pre = '1'                               # if operations appear twice and the former one is not '=', error.
				if op != '':
					if int(disp) == 0 and op == '/':
						errmsg = 'error: divided by zero'
					else:
						disp = ops[op](int(val), int(disp))
				op = optype
				val = disp
				
			else:
				if int(disp) == 0 and op == '/':
					errmsg = 'error: divided by zero'
				elif op == '':                               # '=' appears twice. {=} * {=}             
					pass   
				else:
					disp = ops[op](int(val), int(disp)) 
				op = ''
			
		
	elif 'num' in request.POST:
		if flg == '1' or disp == '0':
			disp = request.POST['num']
		elif flg == '0':
			disp = disp + request.POST['num']
		if int(disp) == 0:
			disp = '0' 
		flg = '0'
		pre = '0'
	
	if int(disp) > 999999 or int(disp) < -999999:
		errmsg = 'error: out of bound'                          # bound is (-1000000, 1000000)
		flg = '1'
		
			
	context = {'display':disp, 'variable':val, 'operation':op, 'flag':flg, 'errmsg':errmsg, 'preop':pre}
	return render(request, 'calculator/calculator.html', context)







	







	
