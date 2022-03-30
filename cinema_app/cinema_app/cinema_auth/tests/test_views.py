from django import test as django_test


class SignUpViewTests(django_test.TestCase):
    def test_get__correct_template__expect_correct_template(self):
        pass

    def test_get__context__expect_form_in_context(self):
        pass

    def test_post__valid_data_given__expect_form_to_be_valid(self):
        pass

    def test_post__create_user__expect_to_create_user_and_login(self):
        pass

    def test_post__redirect__expect_to_redirect(self):
        pass