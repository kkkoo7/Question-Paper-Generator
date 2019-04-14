import random
import json
import os 

def get_all_possible_question_combination_for_each_type(question_arr, target_sum, output_arr, partial_sum = []):
	"""
	params:
		question_arr: array of all possible question of any type in form [{"question_id": 1, "marks": 2}]
		target_sum: sum of marks for which question has to be selected
		partial_sum: used as part of recursion
		output_arr: stores all the possible combination of questions which adds up to target sum
	"""
	s = sum(map(lambda x : x['marks'], partial_sum))

	if s > target_sum:
		return;
	if s == target_sum:
		output_arr.append(partial_sum)

	for i in range(len(question_arr)):
		n = question_arr[i]
		get_all_possible_question_combination_for_each_type(question_arr[i + 1:], target_sum, output_arr, partial_sum + [n])

def get_random_set_of_a_type(output_arr):
	"""
	params:
		output_arr: stores all the possible combination of questions which adds up to target sum

	returns any random possible set of question
	"""
	return output_arr[random.randint(0, len(output_arr)-1)]

def get_question_bank(path):
	try:
		with open(path) as json_file:
			question_bank = json.load(json_file)
			return question_bank
	except ValueError:
			print 'Invalid Json File'
			return None

def create_questions(questions):
	easy_question_marks = question_bank['criteria']['easy'] * question_bank['criteria']['total'] / 100
	medium_question_marks = question_bank['criteria']['medium'] * question_bank['criteria']['total'] / 100
	hard_question_marks = question_bank['criteria']['hard'] * question_bank['criteria']['total'] / 100
	get_all_possible_question_combination_for_each_type(question_bank['question_set']['easy'],easy_question_marks, easy_question_set)
	medium_question_set = []
	get_all_possible_question_combination_for_each_type(question_bank['question_set']['medium'], medium_question_marks, medium_question_set)
	hard_question_set = []
	get_all_possible_question_combination_for_each_type(question_bank['question_set']['hard'], hard_question_marks, hard_question_set)
	if len(easy_question_set) and len(medium_question_set) and len(hard_question_set):
		questions = []
		questions.extend(get_random_set_of_a_type(easy_question_set))
		questions.extend(get_random_set_of_a_type(medium_question_set))
		questions.extend(get_random_set_of_a_type(hard_question_set))
		print map(lambda x : x['question_id'], questions)
	else:
		print "Invalid Parameters"


if __name__ == '__main__':
	easy_question_set = []
	path = os.path.join(os.getcwd(), 'question.json')
	if os.path.exists(path):
		question_bank = get_question_bank(path)
		if question_bank:
			create_questions(question_bank)
	else:
		print "Input File not Found"