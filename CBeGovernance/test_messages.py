from rasa_nlu.model import Interpreter

def run_nlu():
	interpreter = Interpreter.load('./models/nlu/default/cbeg_nlu')
	print(interpreter.parse(u"nothing"))
	
if __name__ == '__main__':
	run_nlu()  #for testing intent and their confidence only