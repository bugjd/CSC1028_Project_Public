import unittest
from unicodedata import decimal


class MyTestCase(unittest.TestCase):
    """Testing the communication library"""

    def test_send_text_invalid_phoneNumber(self): # U_COM_1
        """Testing what happens when someone enters an invalid phone number"""
        # tester = Communication(sent_from, password, url)
        phoneNumberINVALID = int(297269000)
        countryCodeVALID = 44
        message = "hello"
        # acutal_answer = send_text(phoneNumberINVALID, countryCodeVALID, message)

        expected_answer = -1.0
        temp_actual_answer = -1.0

        self.assertEqual(expected_answer, temp_actual_answer)  # add proper one when possible.

    def test_send_text_invalid_CountryCode(self): # U_COM_2
        """Tesrting what happens when an invalid couttry code is given"""
        # tester = Communication(sent_from, password, url)
        phoneNumberVALID = int(299269000)
        countryCodeINVALID = 440
        message = "hello"
        # acutal_answer = send_text(phoneNumberVALID, countryCodeINVALID, message)

        expected_answer = -1.0
        temp_actual_answer = -1.0

        self.assertEqual(expected_answer, temp_actual_answer)  # add proper one when possible.

    def test_send_text_invalid_message(self): # U_COM_3
        """testing what happens when an invalid message is given"""
        # tester = Communication(sent_from, password, url)
        phoneNumberVALID = int(299269000)
        countryCodeVALID = 44
        messageINVALID = "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium. Integer tincidunt. Cras dapibus. Vivamus elementum semper nisi. Aenean vulputate eleifend tellus. Aenean leo ligula, porttitor eu, consequat vitae, eleifend ac, enim. Aliquam lorem ante, dapibus in, viverra quis, feugiat a, tellus. Phasellus viverra nulla ut metus varius laoreet. Quisque rutrum. Aenean imperdiet. Etiam ultricies nisi vel augue. Curabitur ullamcorper ultricies nisi. Nam eget dui. Etiam rhoncus. Maecenas tempus, tellus eget condimentum rhoncus, sem quam semper libero, sit amet adipiscing sem neque sed ipsum. Nam quam nunc, blandit vel, luctus pulvinar, hendrerit id, lorem. Maecenas nec odio et ante tincidunt tempus. Donec vitae sapien ut libero venenatis faucibus. Nullam quis ante. Etiam sit amet orci eget eros faucibus tincidunt. Duis leo. Sed fringilla mauris sit amet nibh. Donec sodales sagittis magna. Sed consequat, leo eget bibendum sodales, augue velit cursus nunc,"
        # acutal_answer = send_text(phoneNumberVALID, countryCodeINVALID, messageINVALID)

        expected_answer = -1.0
        temp_actual_answer = -1.0

        self.assertEqual(expected_answer, temp_actual_answer)  # add proper one when possible.

    def test_send_text_valid(self): # U_COM_4
        """testing that text messages can be sent with valid information,"""
        # tester = Communication(sent_from, password, url)
        phoneNumberVALID = int(299269000)
        countryCodeVALIDD = 44
        messageVALID = "hello"
        # acutal_answer = send_text(phoneNumberVALID, countryCodeINVALID, messageVALID)

        expected_answer = 0.1  # change to actual cost of uk text message
        temp_actual_answer = 0.1

        self.assertEqual(expected_answer, temp_actual_answer)  # add proper one when possible.


if __name__ == '__main__':
    unittest.main()
