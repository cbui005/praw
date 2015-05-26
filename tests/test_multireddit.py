"""Tests for Multireddit class."""

from __future__ import print_function, unicode_literals
from praw import errors
from .helper import PRAWTest, betamax


class MultiredditTest(PRAWTest):

    def betamax_init(self):
        self.r.login(self.un, self.un_pswd, disable_warning=True)

    @betamax
    def test_create_and_delete_multireddit(self):
        name = 'PRAW_{0}'.format(self.r.modhash)[:15]
        multi = self.r.create_multireddit(name)
        self.assertEqual(name.lower(), multi.name.lower())
        self.assertEqual([], multi.subreddits)

        multi.delete()
        self.assertRaises(errors.NotFound, self.r.user.get_multireddit, name)

    @betamax
    def test_get_my_multis(self):
        multi = self.r.get_my_multireddits()[0]
        self.assertEqual('publicempty', multi.display_name)
        self.assertEqual([], multi.subreddits)

    @betamax
    def test_get_multireddit_from_user(self):
        multi = self.r.user.get_multireddit('publicempty')
        self.assertEqual(self.r.user, multi.author)

    @betamax
    def test_multireddit_get_new(self):
        multi = self.r.user.get_multireddit('publicempty')
        self.assertEqual([], list(multi.get_new()))