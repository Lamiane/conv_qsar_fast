from __future__ import print_function
import numpy as np

def q(y_true, y_pred):
	'''q value as described in Tropsha, Gramatica, Gombar:
	The Importance of Being Earnest'''
	y_true = np.array(y_true)
	y_pred = np.array(y_pred)
	y_mean = np.mean(y_true)
	return 1 - np.sum((y_true - y_pred) ** 2) / np.sum((y_true - y_mean) ** 2)

def linreg(x, y):
	'''Computes a linear regression through the origin using OLS'''
	x = np.array(x)
	y = np.array(y)
	x = x[:, np.newaxis]
	a, _, _, _ = np.linalg.lstsq(x, y, rcond=-1.)
	r2 = q(y, (x * a)[:, 0])
	return (r2, a)