import Poke_Core

poke_core = Poke_Core.Poke_Core()

def ask(text, options) :
	print(text)
	print(options)
	ans = input()
	return ans

ans = 'start'
while True :
	text, options = poke_core.proc(ans)
	if len(options) == 0 :
		break
	ans = ask(text, options)
