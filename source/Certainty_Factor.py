w2cf = {
	"defi": 0.6, 
	"prob": 0.6, 
	"mayb": 0.4
}

base = 100

def mix(a, b) :
	if a > 0.0 and b > 0.0 :
		return a + b - a * b
	elif a * b < 0.0 :
		return (a + b) / (1 - min(abs(a), abs(b)) + 1e-4)
	else :
		return a + b + a * b

def get_ratio(token) :
	if (token == 'mayb') :
		return 0.7
	elif (token == 'unknown') :
		return 0.0
	return 1.0
