import pickle
amount=0
f = open("holidaynumber.dat", "wb")
pickle.dump(amount, f)
f.close
