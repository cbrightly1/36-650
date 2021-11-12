# You have list of Agile story statuses (“Ready”, “In Progress”, “Blocked”,
# “Completed”). You would like to store these values in your application and they
# will be accessed and searched several times but they won’t be changed. Which
# built-in data structure can be used? List or Tuple? And Why?

# A tuple would be best in this situation because its pros and cons are favorable for this problem.
# For instance, normally the fact that a tuple is immutable is problematic. But since we know that 
# the list of stories won't change, it isn't a problem that the data type is immutable. Then, we 
# know that we want the data type to be super efficient and tuples are more efficient than lists
# because they cannot be changed. Therefore, a tuple is best here because it is more efficient 
# than lists and it's immutable attribute is not a problem.