import statistics

def getLowerQuartile(values):
	n = len(values)
	pos_lower_quartile = (n+1)/4
	fractionary, lower_value, upper_value = getFracionaryLowerAndUpper(values, n, pos_lower_quartile)
	return getQuartile(fractionary=fractionary, lower_value=lower_value, upper_value=upper_value)

def getUpperQuartile(values):
	n = len(values)
	pos_upper_quartile = (3*(n+1))/4
	fractionary, lower_value, upper_value = getFracionaryLowerAndUpper(values, n, pos_upper_quartile)
	return getQuartile(fractionary=fractionary, lower_value=lower_value, upper_value=upper_value)

def getFracionaryLowerAndUpper(values, n, pos):
	fractional_part = pos % 1
	integer_part = int(pos // 1)
	lower_value = values[integer_part-1]
	upper_value = values[integer_part]
	return fractional_part, lower_value, upper_value

def getQuartile(fractionary, lower_value, upper_value):
	return lower_value + fractionary*(upper_value - lower_value)

def getIQR(values):
	return getUpperQuartile(values) - getLowerQuartile(values)

def getUpperLimit(values):
	return statistics.mean(values) + 1.5*(getIQR(values)) 

def getLowerLimit(values):
	return statistics.mean(values) - 1.5*(getIQR(values)) 

def getOutliers(values):
	values.sort()
	outliers = []
	for value in values:
		if value > getUpperLimit(values) or value < getLowerLimit(values):
			outliers.append(value)
	return outliers