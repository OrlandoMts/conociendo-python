class Singleton():
	instance = None

	@staticmethod
	def get_instance():
		if Singleton.instance is None:
			Singleton()
		return Singleton.instance
	
	def __init__(self):
		if Singleton.instance is None:
			Singleton.instance = self

singleton = Singleton()
print(singleton)

singleton = Singleton.get_instance()
print(singleton)

singleton = Singleton.get_instance()
print(singleton)

singleton2 = Singleton.get_instance()
print(singleton2)