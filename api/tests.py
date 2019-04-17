

from django.test import TestCase

from .censor import censor


class API(TestCase):

	def expect_censor(self, sentence, expected):
		censored = censor(sentence)
		self.assertEqual(expected, censored)


	def test_fine_with_proper(self):
		self.expect_censor(
			"Fine.", "Fine.")


	def test_blocks_fuck(self):
		self.expect_censor(
			"Fuck,", "****,")


	def test_strips(self):
		self.expect_censor(
			"     blank     fuck  ", "blank     ****")


	def test_long_500(self):
		self.expect_censor(
			"fuck "*100, ("**** "*100).strip())
